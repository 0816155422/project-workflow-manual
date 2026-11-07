"""Pure resume-position derivation. This function never executes an action."""
def derive_resume(*, current_state_reference, last_completed_action=None, pending_action=None,
 required_references=None, target_platform=None, target_workspace_reference=None,
 workspace_session_status="UNKNOWN", result_status="UNKNOWN", cleanup_status="UNKNOWN",
 checkpointed=False, persisted=False, result_received=False, result_validated=False,
 references_resolved=False):
    if workspace_session_status in ("BLOCKED","FAILED") or result_status in ("BLOCKED","FAILED","OUTPUT_INVALID"):
        position="BLOCKED"
    elif not references_resolved:
        position="RESOLVE_REFERENCES"
    elif result_received and not result_validated:
        position="VALIDATE_RESULT"
    elif result_validated and not persisted:
        position="PERSIST_RESULT"
    elif persisted and not checkpointed:
        position="CREATE_CHECKPOINT"
    elif checkpointed and cleanup_status!="CLOSED":
        position="CLOSE_SESSION"
    elif not pending_action:
        position="STOP"
    elif workspace_session_status in ("DISPATCHED","ACTIVE"):
        position="WAIT_FOR_RESULT"
    elif target_platform=="chatgpt":
        position="DISPATCH_TO_CHATGPT"
    elif target_platform=="github":
        position="DISPATCH_TO_GITHUB"
    else:
        position="UNKNOWN"
    return {"current_state_reference":current_state_reference,"last_completed_action":last_completed_action,
      "pending_action":pending_action,"required_references":list(required_references or []),
      "target_platform":target_platform,"target_workspace_reference":target_workspace_reference,
      "workspace_session_status":workspace_session_status,"result_status":result_status,
      "cleanup_status":cleanup_status,"resume_position":position}
