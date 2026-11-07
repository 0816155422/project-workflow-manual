"""Typed records and enumerations for cross-platform workspace coordination."""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any
import uuid

def utcnow(): return datetime.now(timezone.utc).isoformat()
def new_id(prefix): return f"{prefix}-{uuid.uuid4().hex}"

class SessionStatus(str, Enum):
    CREATED="CREATED"; REFERENCES_RESOLVED="REFERENCES_RESOLVED"; DISPATCHED="DISPATCHED"
    ACTIVE="ACTIVE"; RESULT_RECEIVED="RESULT_RECEIVED"; PERSIST_PENDING="PERSIST_PENDING"
    PERSISTED="PERSISTED"; CHECKPOINTED="CHECKPOINTED"; CLOSED="CLOSED"
    BLOCKED="BLOCKED"; FAILED="FAILED"; UNKNOWN="UNKNOWN"

class OperationStatus(str, Enum):
    SUCCESS="SUCCESS"; BLOCKED="BLOCKED"; NOT_ACCESSIBLE="NOT_ACCESSIBLE"
    NOT_SUPPORTED="NOT_SUPPORTED"; NOT_FOUND="NOT_FOUND"; FAILED="FAILED"; UNKNOWN="UNKNOWN"

class OutputStatus(str, Enum):
    OUTPUT_PRESENT="OUTPUT_PRESENT"; OUTPUT_VALID="OUTPUT_VALID"; OUTPUT_INVALID="OUTPUT_INVALID"
    PERSIST_PENDING="PERSIST_PENDING"; PERSISTED="PERSISTED"; BLOCKED="BLOCKED"
    FAILED="FAILED"; UNKNOWN="UNKNOWN"

class HandoffStatus(str, Enum):
    PENDING="PENDING"; ACCEPTED="ACCEPTED"; REJECTED="REJECTED"
    COMPLETED="COMPLETED"; BLOCKED="BLOCKED"; FAILED="FAILED"

@dataclass
class WorkspaceSession:
    workspace_session_id: str
    work_id: str
    cycle_id: str
    current_state_reference: str
    parent_checkpoint_id: str | None
    platform: str
    workspace_type: str
    workspace_reference: str | None
    actor: str
    allowed_scope: list[str]
    requested_action: str
    requested_references: list[str]
    resolved_references: list[str] = field(default_factory=list)
    status: SessionStatus = SessionStatus.CREATED
    result_reference: str | None = None
    resulting_state_reference: str | None = None
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)
    closed_at: str | None = None
    errors: list[str] = field(default_factory=list)
    active_references: list[str] = field(default_factory=list)
    continuation: str | None = None

@dataclass
class AdapterResult:
    adapter_id: str
    platform: str
    workspace_reference: str | None
    operation: str
    operation_status: OperationStatus
    external_reference: str | None = None
    result_reference: str | None = None
    error: str | None = None
    timestamp: str = field(default_factory=utcnow)

@dataclass
class WorkPacket:
    packet_id: str
    work_id: str
    cycle_id: str
    source_state_reference: str
    parent_checkpoint_id: str | None
    target_platform: str
    target_workspace_reference: str | None
    requested_action: str
    allowed_scope: list[str]
    required_references: list[str]
    expected_result_type: str
    persistence_policy: str
    checkpoint_policy: str
    return_destination: str
    created_by: str
    created_at: str = field(default_factory=utcnow)

@dataclass
class ResultPacket:
    result_packet_id: str
    packet_id: str
    workspace_session_id: str
    work_id: str
    platform: str
    action_performed: str
    result_status: OutputStatus
    result_references: list[str] = field(default_factory=list)
    created_references: list[str] = field(default_factory=list)
    modified_references: list[str] = field(default_factory=list)
    test_results: list[dict[str, Any]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    proposed_resulting_state: str | None = None
    continuation: str | None = None
    created_at: str = field(default_factory=utcnow)

@dataclass
class HandoffPacket:
    handoff_id: str
    from_workspace_session: str
    to_platform: str
    to_workspace_reference: str | None
    work_id: str
    current_state_reference: str
    checkpoint_reference: str | None
    required_references: list[str]
    allowed_scope: list[str]
    pending_action: str
    return_contract: str
    status: HandoffStatus = HandoffStatus.PENDING

def to_dict(value):
    result=asdict(value)
    for k,v in list(result.items()):
        if isinstance(v, Enum): result[k]=v.value
    return result
