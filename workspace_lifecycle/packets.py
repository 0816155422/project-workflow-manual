"""Packet construction and validation. Packets carry references, never whole-system payloads."""
from .models import WorkPacket, ResultPacket, new_id, utcnow

def create_work_packet(*, work_id, cycle_id, source_state_reference, parent_checkpoint_id,
 target_platform, target_workspace_reference, requested_action, allowed_scope,
 required_references, expected_result_type, persistence_policy, checkpoint_policy,
 return_destination, created_by):
    if not work_id or not cycle_id or not source_state_reference or not requested_action:
        raise ValueError("work_id, cycle_id, source_state_reference and requested_action are required")
    if not allowed_scope: raise ValueError("allowed_scope must be explicit and non-empty")
    if any(not isinstance(x,str) or not x for x in required_references): raise ValueError("references must be non-empty strings")
    return WorkPacket(new_id("WPK"),work_id,cycle_id,source_state_reference,parent_checkpoint_id,
      target_platform,target_workspace_reference,requested_action,list(allowed_scope),list(required_references),
      expected_result_type,persistence_policy,checkpoint_policy,return_destination,created_by,utcnow())

def create_result_packet(*, packet, session, result_status, action_performed, result_references=None,
 created_references=None, modified_references=None, test_results=None, errors=None,
 limitations=None, proposed_resulting_state=None, continuation=None):
    allowed=set(packet.allowed_scope)
    touched=set(created_references or []) | set(modified_references or [])
    if not touched.issubset(allowed):
        raise PermissionError(f"result references outside allowed scope: {sorted(touched-allowed)}")
    return ResultPacket(new_id("RPK"),packet.packet_id,session.workspace_session_id,packet.work_id,
      session.platform,action_performed,result_status,list(result_references or []),
      list(created_references or []),list(modified_references or []),list(test_results or []),
      list(errors or []),list(limitations or []),proposed_resulting_state,continuation,utcnow())
