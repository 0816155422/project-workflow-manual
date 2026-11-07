"""Logical ChatGPT conversation adapter. No claim of host API or context deletion."""
from ..models import AdapterResult, OperationStatus, OutputStatus, new_id
from ..packets import create_result_packet

class ChatGPTWorkspaceAdapter:
    adapter_id="chatgpt-logical-session-v1"
    platform="chatgpt"
    def __init__(self):
        self.sessions={}
        self.results={}
    def create_session(self, packet):
        sid=new_id("WSS")
        self.sessions[sid]={"packet_id":packet.packet_id,"work_id":packet.work_id,
          "source_state_reference":packet.source_state_reference,"allowed_scope":list(packet.allowed_scope),
          "requested_references":list(packet.required_references),"work_packet":packet,"status":"CREATED",
          "result_packet":None,"active_references":list(packet.required_references)}
        return AdapterResult(self.adapter_id,self.platform,"chatgpt://current-conversation", "create_session",OperationStatus.SUCCESS,sid)
    def resolve_workspace(self, reference):
        return AdapterResult(self.adapter_id,self.platform,reference,"resolve_workspace",
          OperationStatus.SUCCESS if reference in (None,"chatgpt://current-conversation") else OperationStatus.NOT_FOUND,
          reference,error=None if reference in (None,"chatgpt://current-conversation") else "Conversation reference not registered by this adapter.")
    def dispatch_work(self, session, packet):
        if session.workspace_session_id not in self.sessions:
            return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"dispatch_work",OperationStatus.NOT_FOUND,error="Logical session not found.")
        record=self.sessions[session.workspace_session_id]
        if packet.packet_id!=record["packet_id"] or packet.allowed_scope!=record["allowed_scope"]:
            return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"dispatch_work",OperationStatus.BLOCKED,error="Packet/session scope mismatch.")
        record["status"]="ACTIVE"
        return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"dispatch_work",OperationStatus.SUCCESS,session.workspace_session_id)
    def record_result_candidate(self, session, packet, *, action_performed, result_references=None,
        created_references=None, modified_references=None, test_results=None, errors=None,
        limitations=None, proposed_resulting_state=None, continuation=None, valid=True):
        record=self.sessions[session.workspace_session_id]
        result=create_result_packet(packet=packet,session=session,
          result_status=OutputStatus.OUTPUT_VALID if valid else OutputStatus.OUTPUT_INVALID,
          action_performed=action_performed,result_references=result_references,
          created_references=created_references,modified_references=modified_references,
          test_results=test_results,errors=errors,limitations=limitations,
          proposed_resulting_state=proposed_resulting_state,continuation=continuation)
        record["result_packet"]=result; record["status"]="RESULT_RECEIVED"
        self.results[result.result_packet_id]=result
        return result
    def get_session_status(self, session):
        record=self.sessions.get(session.workspace_session_id)
        if not record: return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"get_session_status",OperationStatus.NOT_FOUND)
        return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"get_session_status",OperationStatus.SUCCESS,session.workspace_session_id,result_reference=getattr(record.get("result_packet"),"result_packet_id",None))
    def receive_result(self, session):
        record=self.sessions.get(session.workspace_session_id)
        if not record: return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"receive_result",OperationStatus.NOT_FOUND,error="Logical session not found.")
        result=record.get("result_packet")
        if result is None: return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"receive_result",OperationStatus.UNKNOWN,error="No Result Candidate has been submitted.")
        return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"receive_result",OperationStatus.SUCCESS,session.workspace_session_id,result.result_packet_id)
    def get_result_packet(self, session):
        record=self.sessions.get(session.workspace_session_id)
        return record.get("result_packet") if record else None
    def close_session(self, session):
        record=self.sessions.get(session.workspace_session_id)
        if not record: return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"close_session",OperationStatus.NOT_FOUND)
        record["status"]="CLOSED"; record["active_references"]=[]
        # Logical closure only. ChatGPT platform context is not deleted.
        return AdapterResult(self.adapter_id,self.platform,session.workspace_reference,"close_session",OperationStatus.SUCCESS,session.workspace_session_id,
          error="Logical session closed; platform conversational context deletion is not supported or claimed.")
