"""SQLite-backed IRIS lifecycle kernel with resume and handoff."""
import json, os, sqlite3, uuid
from pathlib import Path
def db_path(): return Path(os.environ.get("IRIS_DB_PATH", Path(__file__).parent/"data"/"iris.db"))
def connect():
 p=db_path(); p.parent.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(p); c.row_factory=sqlite3.Row; c.execute("PRAGMA foreign_keys=ON"); return c
SCHEMA="""
CREATE TABLE IF NOT EXISTS work_units(id TEXT PRIMARY KEY,title TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'CREATED',current_step INTEGER NOT NULL DEFAULT 0,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS step_runs(id INTEGER PRIMARY KEY AUTOINCREMENT,work_id TEXT NOT NULL REFERENCES work_units(id),step INTEGER NOT NULL,attempt INTEGER NOT NULL,status TEXT NOT NULL,expected TEXT,actual TEXT,note TEXT,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS errors(id INTEGER PRIMARY KEY AUTOINCREMENT,work_id TEXT NOT NULL REFERENCES work_units(id),step INTEGER NOT NULL,attempt INTEGER NOT NULL,error_type TEXT NOT NULL,message TEXT NOT NULL,expected TEXT,actual TEXT,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS checkpoints(id INTEGER PRIMARY KEY AUTOINCREMENT,work_id TEXT NOT NULL REFERENCES work_units(id),step INTEGER NOT NULL,state TEXT NOT NULL,snapshot TEXT NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS verifications(id INTEGER PRIMARY KEY AUTOINCREMENT,work_id TEXT NOT NULL REFERENCES work_units(id),expected TEXT NOT NULL,actual TEXT NOT NULL,status TEXT NOT NULL,note TEXT,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS audit_log(id INTEGER PRIMARY KEY AUTOINCREMENT,work_id TEXT NOT NULL REFERENCES work_units(id),action TEXT NOT NULL,details TEXT NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS handoffs(id TEXT PRIMARY KEY,work_id TEXT NOT NULL REFERENCES work_units(id),checkpoint_id INTEGER,from_actor TEXT NOT NULL,to_actor TEXT NOT NULL,status TEXT NOT NULL,resume_state TEXT NOT NULL,note TEXT NOT NULL DEFAULT '',created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,accepted_at TEXT);
"""
def init_db():
 with connect() as c: c.executescript(SCHEMA)
def one(sql,args=()):
 with connect() as c:
  r=c.execute(sql,args).fetchone(); return dict(r) if r else None
def many(sql,args=()):
 with connect() as c: return [dict(x) for x in c.execute(sql,args).fetchall()]
def _audit(c,w,a,d): c.execute("INSERT INTO audit_log(work_id,action,details) VALUES(?,?,?)",(w,a,d))
def _checkpoint(c,w,s,state,snapshot):
 cur=c.execute("INSERT INTO checkpoints(work_id,step,state,snapshot) VALUES(?,?,?,?)",(w,s,state,json.dumps(snapshot,ensure_ascii=False,sort_keys=True)))
 _audit(c,w,"CHECKPOINT",f"checkpoint_id={cur.lastrowid};step={s};state={state}"); return cur.lastrowid
def create_work(work_id,title):
 w=str(work_id).strip(); t=str(title).strip()
 if not w or not t: raise ValueError("work_id and title are required")
 with connect() as c: c.execute("INSERT INTO work_units(id,title) VALUES(?,?)",(w,t)); _audit(c,w,"WORK_CREATED",t)
 return {"work_id":w,"status":"CREATED","current_step":0}
def get_work(w):
 work=one("SELECT * FROM work_units WHERE id=?",(w,))
 if not work: return None
 return {"work":work,"steps":many("SELECT * FROM step_runs WHERE work_id=? ORDER BY id",(w,)),"errors":many("SELECT * FROM errors WHERE work_id=? ORDER BY id",(w,)),"checkpoints":many("SELECT * FROM checkpoints WHERE work_id=? ORDER BY id",(w,)),"audit":many("SELECT * FROM audit_log WHERE work_id=? ORDER BY id",(w,)),"verifications":many("SELECT * FROM verifications WHERE work_id=? ORDER BY id",(w,))}
def resume_work(w):
 r=get_work(w)
 if not r: raise KeyError("work not found")
 cp=r["checkpoints"][-1] if r["checkpoints"] else None
 if r["work"]["status"]=="DELIVERED": return {"work_id":w,"state":"DELIVERED","next_action":"STOP","next_step":None,"checkpoint_id":cp["id"] if cp else None}
 latest={}
 for row in r["steps"]: latest[row["step"]]=row
 nxt=1
 for n in range(1,6):
  if not latest.get(n) or latest[n]["status"]!="PASSED": nxt=n; break
  nxt=n+1
 action="FINAL_VERIFY" if nxt>5 else "RETRY_OR_EXECUTE_STEP"; row=latest.get(nxt) if nxt<=5 else None
 return {"work_id":w,"state":row["status"] if row else r["work"]["status"],"next_action":action,"next_step":nxt if nxt<=5 else None,"checkpoint_id":cp["id"] if cp else None,"checkpoint_state":cp["state"] if cp else None,"reason":"Derived from persisted latest step run; caller supplies fresh expected/actual values."}
def run_step(w,step,expected,actual,note="",max_attempts=10):
 if step not in range(1,6): raise ValueError("step must be 1..5")
 if not one("SELECT id FROM work_units WHERE id=?",(w,)): raise KeyError("work not found")
 if not isinstance(max_attempts,int) or not 1<=max_attempts<=10: raise ValueError("max_attempts must be 1..10")
 state=resume_work(w)
 if state["next_action"]=="STOP": raise ValueError("delivered work is terminal")
 if state["next_action"]=="FINAL_VERIFY" or state["next_step"]!=step: raise ValueError(f"resume gate requires step {state['next_step'] or 'final verification'}")
 for attempt in range(1,max_attempts+1):
  with connect() as c:
   for status in ("CHECKING","WORKING","VERIFYING"):
    c.execute("INSERT INTO step_runs(work_id,step,attempt,status,expected,actual,note) VALUES(?,?,?,?,?,?,?)",(w,step,attempt,status,str(expected),str(actual),note))
    c.execute("UPDATE work_units SET current_step=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",(step,status,w)); _audit(c,w,"STEP_"+status,f"step={step};attempt={attempt}")
   passed=str(expected).strip()==str(actual).strip(); status="PASSED" if passed else "FAILED"
   c.execute("INSERT INTO step_runs(work_id,step,attempt,status,expected,actual,note) VALUES(?,?,?,?,?,?,?)",(w,step,attempt,status,str(expected),str(actual),note))
   c.execute("UPDATE work_units SET current_step=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",(step,status,w)); _audit(c,w,"STEP_"+status,f"step={step};attempt={attempt}")
   if passed:
    cp=_checkpoint(c,w,step,status,{"attempt":attempt,"expected":str(expected),"actual":str(actual)})
    return {"step":step,"status":status,"attempt":attempt,"checkpoint_id":cp}
   c.execute("INSERT INTO errors(work_id,step,attempt,error_type,message,expected,actual) VALUES(?,?,?,?,?,?,?)",(w,step,attempt,"MISMATCH","expected and actual do not match",str(expected),str(actual)))
   _audit(c,w,"ERROR_RECORDED",f"step={step};attempt={attempt};type=MISMATCH"); _checkpoint(c,w,step,"FAILED",{"attempt":attempt,"expected":str(expected),"actual":str(actual)})
 raise RuntimeError(f"step {step} did not pass within {max_attempts} attempts")
def final_verify(w,expected,actual,note=""):
 r=get_work(w)
 if not r: raise KeyError("work not found")
 if resume_work(w)["next_action"]!="FINAL_VERIFY": raise ValueError("all five latest step runs must be PASSED")
 ok=str(expected).strip()==str(actual).strip(); status="VERIFIED" if ok else "MISMATCH"
 with connect() as c:
  c.execute("INSERT INTO verifications(work_id,expected,actual,status,note) VALUES(?,?,?,?,?)",(w,str(expected),str(actual),status,note)); _audit(c,w,"FINAL_VERIFICATION",status)
  if ok: c.execute("UPDATE work_units SET status='DELIVERED',updated_at=CURRENT_TIMESTAMP WHERE id=?",(w,))
  else:
   c.execute("INSERT INTO errors(work_id,step,attempt,error_type,message,expected,actual) VALUES(?,?,?,?,?,?,?)",(w,0,0,"FINAL_VERIFICATION_MISMATCH","final expected and actual do not match",str(expected),str(actual)))
   _checkpoint(c,w,0,"FINAL_MISMATCH",{"expected":str(expected),"actual":str(actual)})
 return {"status":status,"delivered":ok}
def create_handoff(w,from_actor,to_actor,note=""):
 state=resume_work(w)
 if state["state"]=="DELIVERED": raise ValueError("delivered work cannot be handed off")
 if not str(from_actor).strip() or not str(to_actor).strip(): raise ValueError("from_actor and to_actor required")
 hid="HOF-"+uuid.uuid4().hex
 with connect() as c:
  c.execute("INSERT INTO handoffs(id,work_id,checkpoint_id,from_actor,to_actor,status,resume_state,note) VALUES(?,?,?,?,?,?,?,?)",(hid,w,state["checkpoint_id"],from_actor,to_actor,"PENDING",json.dumps(state,ensure_ascii=False,sort_keys=True),note)); _audit(c,w,"HANDOFF_CREATED",hid)
 return {"handoff_id":hid,"status":"PENDING","resume_state":state}
def accept_handoff(hid,actor):
 h=one("SELECT * FROM handoffs WHERE id=?",(hid,))
 if not h: raise KeyError("handoff not found")
 if h["status"]!="PENDING": raise ValueError("handoff is not pending")
 if actor!=h["to_actor"]: raise PermissionError("actor does not match designated recipient")
 with connect() as c:
  cur=c.execute("UPDATE handoffs SET status='ACCEPTED',accepted_at=CURRENT_TIMESTAMP WHERE id=? AND status='PENDING'",(hid,))
  if cur.rowcount!=1: raise ValueError("handoff acceptance race; reload state")
  _audit(c,h["work_id"],"HANDOFF_ACCEPTED",f"{hid};actor={actor}")
 return {"handoff_id":hid,"status":"ACCEPTED","resume_state":resume_work(h["work_id"])}
