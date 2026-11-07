import os,tempfile,pytest
from pathlib import Path
os.environ["IRIS_DB_PATH"]=str(Path(tempfile.mkdtemp())/"test.db")
from iris_runtime import *
def setup_function(): init_db()
def test_checkpoint_handoff_resume_continue_e2e():
 create_work("W-E2E","resume and handoff")
 assert run_step("W-E2E",1,"a","a")["status"]=="PASSED"
 s=resume_work("W-E2E"); assert s["next_step"]==2 and s["checkpoint_id"]
 h=create_handoff("W-E2E","agent-A","agent-B")
 with pytest.raises(PermissionError): accept_handoff(h["handoff_id"],"wrong-agent")
 a=accept_handoff(h["handoff_id"],"agent-B"); assert a["status"]=="ACCEPTED" and a["resume_state"]["next_step"]==2
 for n in range(2,6): run_step("W-E2E",n,f"s{n}",f"s{n}")
 assert final_verify("W-E2E","done","done")["status"]=="VERIFIED"
 assert resume_work("W-E2E")["next_action"]=="STOP"
 r=get_work("W-E2E"); assert r["work"]["status"]=="DELIVERED"
 assert any(x["action"]=="HANDOFF_ACCEPTED" for x in r["audit"])
def test_failed_step_resume_same_step():
 create_work("W-FAIL","retry")
 with pytest.raises(RuntimeError): run_step("W-FAIL",1,"x","y",max_attempts=1)
 s=resume_work("W-FAIL"); assert s["next_step"]==1 and s["checkpoint_state"]=="FAILED"
 assert len(get_work("W-FAIL")["errors"])==1
def test_final_mismatch_persists_error_checkpoint():
 create_work("W-MISMATCH","mismatch")
 for n in range(1,6): run_step("W-MISMATCH",n,"x","x")
 assert final_verify("W-MISMATCH","A","B")["status"]=="MISMATCH"
 r=get_work("W-MISMATCH"); assert r["verifications"][-1]["status"]=="MISMATCH"
 assert r["errors"][-1]["error_type"]=="FINAL_VERIFICATION_MISMATCH"
 assert r["checkpoints"][-1]["state"]=="FINAL_MISMATCH" and r["work"]["status"]!="DELIVERED"
