"""Cross-platform handoff validation; actor labels are not authority proofs."""
from .models import HandoffPacket, HandoffStatus, new_id

def create_handoff(session, *, to_platform, to_workspace_reference, required_references,
 allowed_scope, pending_action, return_contract, checkpoint_reference=None):
    if session.status.value not in ("RESULT_RECEIVED","ACTIVE","DISPATCHED"):
        raise ValueError("source session is not in a handoff-capable state")
    if not set(required_references).issubset(set(session.resolved_references)):
        raise PermissionError("handoff requests unresolved references")
    if not set(allowed_scope).issubset(set(session.allowed_scope)):
        raise PermissionError("handoff scope exceeds source session scope")
    return HandoffPacket(new_id("HOF"),session.workspace_session_id,to_platform,to_workspace_reference,
      session.work_id,session.current_state_reference,checkpoint_reference,list(required_references),
      list(allowed_scope),pending_action,return_contract,HandoffStatus.PENDING)

def accept_handoff(packet, *, target_platform, target_workspace_reference, allowed_scope,
 authority_check):
    if packet.status is not HandoffStatus.PENDING: raise ValueError("handoff is not pending")
    if target_platform!=packet.to_platform or target_workspace_reference!=packet.to_workspace_reference:
        packet.status=HandoffStatus.REJECTED
        raise PermissionError("handoff target mismatch")
    if not set(packet.allowed_scope).issubset(set(allowed_scope)):
        packet.status=HandoffStatus.REJECTED
        raise PermissionError("target adapter scope does not cover handoff scope")
    if not authority_check(packet):
        packet.status=HandoffStatus.REJECTED
        raise PermissionError("authority not established by supplied authorization check")
    packet.status=HandoffStatus.ACCEPTED
    return packet
