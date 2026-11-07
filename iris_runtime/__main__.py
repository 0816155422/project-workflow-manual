"""MCP stdio entry point. Requires the MCP Python SDK."""
import json, asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from . import init_db,db_path,connect,create_work,run_step,final_verify,get_work,resume_work,create_handoff,accept_handoff
server=Server("iris-controller-working-branch")
TOOLS=[
Tool(name="health",description="Initialize and verify configured SQLite store.",inputSchema={"type":"object","properties":{}}),
Tool(name="create_work",description="Create a work unit.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"title":{"type":"string"}},"required":["work_id","title"]}),
Tool(name="run_step",description="Run the next gated step.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"step":{"type":"integer","minimum":1,"maximum":5},"expected":{"type":"string"},"actual":{"type":"string"},"note":{"type":"string"},"max_attempts":{"type":"integer","minimum":1,"maximum":10}},"required":["work_id","step","expected","actual"]}),
Tool(name="final_verify",description="Verify delivery after all five latest steps pass.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"expected":{"type":"string"},"actual":{"type":"string"},"note":{"type":"string"}},"required":["work_id","expected","actual"]}),
Tool(name="get_work_status",description="Read full work and audit history.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"}},"required":["work_id"]}),
Tool(name="resume_work",description="Derive next safe step from persisted state and checkpoint.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"}},"required":["work_id"]}),
Tool(name="create_handoff",description="Persist a pending handoff packet.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"from_actor":{"type":"string"},"to_actor":{"type":"string"},"note":{"type":"string"}},"required":["work_id","from_actor","to_actor"]}),
Tool(name="accept_handoff",description="Accept handoff as designated recipient and return current resume position.",inputSchema={"type":"object","properties":{"handoff_id":{"type":"string"},"actor":{"type":"string"}},"required":["handoff_id","actor"]})]
def reply(x): return [TextContent(type="text",text=json.dumps(x,ensure_ascii=False,default=str))]
@server.list_tools()
async def list_tools(): return TOOLS
@server.call_tool()
async def call_tool(name,arguments):
 try:
  if name=="health":
   init_db()
   with connect() as c: c.execute("SELECT 1").fetchone()
   return reply({"status":"OK","database":"ok","db_path":str(db_path())})
  if name=="create_work": return reply({"status":"OK",**create_work(arguments["work_id"],arguments["title"])})
  if name=="run_step": return reply({"status":"OK",**run_step(arguments["work_id"],int(arguments["step"]),arguments["expected"],arguments["actual"],arguments.get("note",""),int(arguments.get("max_attempts",10)))})
  if name=="final_verify": return reply({"status":"OK",**final_verify(arguments["work_id"],arguments["expected"],arguments["actual"],arguments.get("note",""))})
  if name=="get_work_status":
   r=get_work(arguments["work_id"]); return reply({"status":"OK",**r}) if r else reply({"status":"ERROR","error_type":"NOT_FOUND","message":"work not found"})
  if name=="resume_work": return reply({"status":"OK",**resume_work(arguments["work_id"])})
  if name=="create_handoff": return reply({"status":"OK",**create_handoff(arguments["work_id"],arguments["from_actor"],arguments["to_actor"],arguments.get("note",""))})
  if name=="accept_handoff": return reply({"status":"OK",**accept_handoff(arguments["handoff_id"],arguments["actor"])})
  return reply({"status":"ERROR","error_type":"UNKNOWN_TOOL","message":name})
 except Exception as e: return reply({"status":"ERROR","error_type":type(e).__name__,"message":str(e)})
async def main():
 init_db()
 async with stdio_server() as (r,w): await server.run(r,w,server.create_initialization_options())
if __name__=="__main__": asyncio.run(main())
