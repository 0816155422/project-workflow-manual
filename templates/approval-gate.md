# Course Data Approval Gate

Use this checklist before manually dispatching `Sync Approved Course Data`. A completed form is not itself approval and must not be used to imply that a run occurred.

- task_id:
- objective:
- status: Blocked / Inconclusive until reviewed
- created_at:
- updated_at:
- actor or approving identity:
- source_path (must be a real file under `pending/`):
- target_path (new supported path under `shared/` or `data/`):
- approval_note (single line, 1–300 characters):
- source provenance and evidence:
- validation run URL and conclusion:
- content review completed by:
- secret scan reviewed (heuristic only):
- target confirmed absent:
- approval decision: Approve / Reject / Defer
- decision timestamp:
- next_step:
- blocker:
- source of evidence:

## Rules
1. Do not approve example, placeholder, or fabricated records.
2. Do not dispatch sync when source provenance is missing.
3. Validation passing is not approval.
4. Only a real successful manual sync run plus resulting commit, target file read-back, and approval log entry can prove write-back.
5. Keep this checklist and all logs append-only; create a new entry for each decision.
