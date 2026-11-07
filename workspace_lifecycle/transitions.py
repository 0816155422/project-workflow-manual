"""Single controlled transition function; callers cannot assign status through this API."""
from .models import SessionStatus, utcnow

ALLOWED = {
 SessionStatus.CREATED: {SessionStatus.REFERENCES_RESOLVED, SessionStatus.BLOCKED, SessionStatus.FAILED, SessionStatus.UNKNOWN},
 SessionStatus.REFERENCES_RESOLVED: {SessionStatus.DISPATCHED, SessionStatus.BLOCKED, SessionStatus.FAILED},
 SessionStatus.DISPATCHED: {SessionStatus.ACTIVE, SessionStatus.BLOCKED, SessionStatus.FAILED, SessionStatus.UNKNOWN},
 SessionStatus.ACTIVE: {SessionStatus.RESULT_RECEIVED, SessionStatus.BLOCKED, SessionStatus.FAILED, SessionStatus.UNKNOWN},
 SessionStatus.RESULT_RECEIVED: {SessionStatus.PERSIST_PENDING, SessionStatus.BLOCKED, SessionStatus.FAILED, SessionStatus.CLOSED},
 SessionStatus.PERSIST_PENDING: {SessionStatus.PERSISTED, SessionStatus.BLOCKED, SessionStatus.FAILED},
 SessionStatus.PERSISTED: {SessionStatus.CHECKPOINTED, SessionStatus.BLOCKED, SessionStatus.FAILED},
 SessionStatus.CHECKPOINTED: {SessionStatus.CLOSED, SessionStatus.BLOCKED, SessionStatus.FAILED},
 SessionStatus.CLOSED: set(), SessionStatus.BLOCKED: set(), SessionStatus.FAILED: set(), SessionStatus.UNKNOWN: set(),
}
def transition(session, target, *, error=None, continuation=None):
    target=SessionStatus(target)
    if target not in ALLOWED[session.status]:
        raise ValueError(f"illegal workspace session transition: {session.status.value} -> {target.value}")
    session.status=target
    session.updated_at=utcnow()
    if error: session.errors.append(str(error))
    if continuation is not None: session.continuation=continuation
    if target is SessionStatus.CLOSED:
        session.active_references=[]
        session.closed_at=session.updated_at
    return session
