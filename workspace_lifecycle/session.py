"""IRIS coordinator for state/action/state workspace rounds."""
from .models import WorkspaceSession, SessionStatus, OperationStatus
from .transitions import transition
from .models import new_id

class WorkspaceCoordinator:
    def __init__(self, adapters, reference_resolver=None):
        self.adapters=dict(adapters); self.reference_resolver=reference_resolver or (lambda refs,scope: list(refs))
        self.sessions={}
    def open_session(self, packet, actor):
        adapter=self.adapters.get(packet.target_platform)
        if adapter is None: raise LookupError(f"no adapter registered for {packet.target_platform}")
        created=adapter.create_session(packet)
        if created.operation_status is not OperationStatus.SUCCESS:
            raise RuntimeError(f"adapter create_session: {created.operation_status.value}: {created.error}")
        sid=created.external_reference
        session=WorkspaceSession(sid,packet.work_id,packet.cycle_id,packet.source_state_reference,
          packet.parent_checkpoint_id,packet.target_platform,"platform-workspace",packet.target_workspace_reference,
          actor,list(packet.allowed_scope),packet.requested_action,list(packet.required_references))
        self.sessions[sid]=session
        resolved=self.reference_resolver(packet.required_references,packet.allowed_scope)
        if set(resolved)!=set(packet.required_references):
            transition(session,SessionStatus.BLOCKED,error="Reference resolution incomplete or scope rejected.")
            raise PermissionError("required references could not be resolved within Allowed Scope")
        session.resolved_references=list(resolved); session.active_references=list(resolved)
        transition(session,SessionStatus.REFERENCES_RESOLVED)
        return session
    def dispatch(self, session, packet):
        if session.status is not SessionStatus.REFERENCES_RESOLVED: raise ValueError("session is not ready for dispatch")
        adapter=self.adapters[session.platform]
        result=adapter.dispatch_work(session,packet)
        if result.operation_status is not OperationStatus.SUCCESS:
            transition(session,SessionStatus.BLOCKED,error=result.error or result.operation_status.value)
            return result
        transition(session,SessionStatus.DISPATCHED)
        transition(session,SessionStatus.ACTIVE)
        return result
    def receive(self, session):
        if session.status is not SessionStatus.ACTIVE: raise ValueError("session is not active")
        adapter=self.adapters[session.platform]
        result=adapter.receive_result(session)
        if result.operation_status is OperationStatus.SUCCESS:
            packet=adapter.get_result_packet(session) if hasattr(adapter,"get_result_packet") else None
            if packet is not None:
                session.result_reference=packet.result_packet_id
                session.resulting_state_reference=packet.proposed_resulting_state
            transition(session,SessionStatus.RESULT_RECEIVED)
        elif result.operation_status in (OperationStatus.BLOCKED,OperationStatus.NOT_ACCESSIBLE):
            transition(session,SessionStatus.BLOCKED,error=result.error or result.operation_status.value)
        return result
    def close(self, session, checkpoint_reference):
        if session.status not in (SessionStatus.RESULT_RECEIVED,SessionStatus.CHECKPOINTED):
            raise ValueError("session cannot close before result and checkpoint boundary")
        if session.status is SessionStatus.RESULT_RECEIVED:
            # A no-persist result may close only after explicit blocked/persist policy handling.
            raise ValueError("session must pass persistence and checkpoint transitions before closure")
        result=self.adapters[session.platform].close_session(session)
        if result.operation_status is OperationStatus.SUCCESS:
            transition(session,SessionStatus.CLOSED,continuation=checkpoint_reference)
        return result
