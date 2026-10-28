# Task Registry

This registry separates work items from status, blockers, evidence, and ownership. It is intentionally scoped to the resume-state layer and course-data blocker only. No workflow, sync, or data write is dispatched from this registry alone.

## Task registry

### T01 — Data source acquisition
- Phase: phase_1_data_preparation
- Status: Blocked
- Priority: Critical
- Owner: project owner / data steward
- Source: manual intake / external source request
- Origin: repository review / issue request / project workflow
- Trigger: pending/course/course-source.json is empty
- Summary: Gather real course data before any validation or sync.
- Blocker: `pending/course/course-source.json` contains `records: []`
- Evidence: `pending/course/course-source.json` read-back shows empty records array.
- Next safe action: Collect real course records from a verified source and keep provenance metadata.
- Updated: 2026-10-28

### T02 — Provenance capture
- Phase: phase_1_data_preparation
- Status: Blocked
- Priority: Critical
- Owner: project owner / data steward
- Source: source document / official course catalog / manual intake
- Origin: requirement for evidence-backed source record
- Trigger: real course data exists but source metadata is missing
- Summary: Record source URL, source name, provider, retrieval time, and provenance trail.
- Blocker: no source_url/provenance metadata recorded
- Evidence: `approvedBy: null`, `approvedAt: null`, and no source provenance object observed in the current pending file.
- Next safe action: Add source_url, source_name, source_type, retrieved_at, and provenance metadata for each actual record.
- Updated: 2026-10-28

### T03 — Approval gate
- Phase: phase_5_approval_gated_sync
- Status: Blocked
- Priority: Critical
- Owner: authorized approver / repository maintainer
- Source: policy / approval workflow
- Origin: required approval before sync
- Trigger: sync is blocked until approval is explicit and traceable
- Summary: Require clear approval metadata before course data can be synced.
- Blocker: `approvedBy: null`, `approvedAt: null`
- Evidence: `pending/course/course-source.json` shows approval metadata is missing.
- Next safe action: Obtain explicit approver identity and timestamp from the authorized person before any sync is triggered.
- Updated: 2026-10-28

### T04 — Schema validation
- Phase: phase_4_validation
- Status: Blocked
- Priority: High
- Owner: workflow maintainer / validation owner
- Source: workflow validation
- Origin: repository validation rules
- Trigger: real data must pass schema validation before sync
- Summary: Validate required fields, data types, and required metadata.
- Blocker: no real course records or non-empty dataset exists
- Evidence: validation infrastructure exists, but source file still contains empty records and no approval metadata.
- Next safe action: Validate an actual dataset with required metadata before sync.
- Updated: 2026-10-28

### T05 — Data sync
- Phase: phase_5_approval_gated_sync
- Status: Blocked
- Priority: Critical
- Owner: repository maintainer / data sync owner
- Source: approved dataset only
- Origin: approval-gated sync workflow
- Trigger: only after validation and approval pass
- Summary: Sync only approved real data.
- Blocker: no approved real dataset exists
- Evidence: no sync was dispatched; pending source is empty and unapproved.
- Next safe action: Do not dispatch sync until validation and approval are both complete.
- Updated: 2026-10-28

### T06 — Usage logging
- Phase: phase_6_usage_logging
- Status: Not proven
- Priority: Medium
- Owner: workflow owner / observability owner
- Source: GitHub Actions runtime logs
- Origin: usage logging workflow requirement
- Trigger: sync should create usage or workflow evidence entries
- Summary: Confirm logger output once sync succeeds.
- Blocker: no successful sync has been proven
- Evidence: no new usage logger run was verified in the current state audit.
- Next safe action: Verify logger output only after a successful sync and a valid dataset.
- Updated: 2026-10-28

### T07 — Frontend rendering
- Phase: phase_7_frontend
- Status: Not proven
- Priority: Medium
- Owner: frontend owner / UI owner
- Source: approved dataset / UI read-back
- Origin: rendering of actual course data in HAP/AICC frontend
- Trigger: frontend should only render approved data
- Summary: Confirm the front-end renders the approved course dataset.
- Blocker: no approved dataset and no proven real source records
- Evidence: no UI read-back for approved course data exists.
- Next safe action: render only after approved dataset is available and read-back verified.
- Updated: 2026-10-28

### T08 — Deployment verification
- Phase: phase_8_deployment
- Status: Not proven
- Priority: Medium
- Owner: deployment owner / repo maintainer
- Source: deploy workflow results
- Origin: deployment of the approved version of the project
- Trigger: deployment should follow successful sync and frontend verification
- Summary: Confirm actual deployment matches the approved data version.
- Blocker: no successful sync or approved dataset exists yet
- Evidence: no deployment proof for the current main HEAD or approved data exists.
- Next safe action: Verify deployment only after sync and frontend proof exist.
- Updated: 2026-10-28

### T09 — ResumeStateGuard
- Phase: system_control
- Status: Proven
- Priority: High
- Owner: repo automation maintainer
- Source: private plugin + repository skill
- Origin: need for state-aware resume protocol without inventing data
- Trigger: require explicit state read before work and append-only checkpointing
- Summary: The plugin and repo skill are installed and read back.
- Blocker: none for the state layer itself
- Evidence: ResumeStateGuard plugin and `skills/resume-state-guard/SKILL.md` were created and read back. Checkpoint files and logs were also read back.
- Next safe action: keep using resume gate before each task; do not broaden scope beyond the state layer.
- Updated: 2026-10-28

### T10 — State read-back verification
- Phase: system_control
- Status: Proven
- Priority: High
- Owner: repo automation maintainer
- Source: repository state verification
- Origin: need to validate every write by read-back
- Trigger: ensure state and log files are persisted and readable
- Summary: Confirm state files, logs, and checkpoint history are readable after each write.
- Blocker: none in the state layer itself
- Evidence: state files and logs were read back successfully from GitHub after update.
- Next safe action: continue read-back verification for each subsequent state update.
- Updated: 2026-10-28

## Status summary
- Proven: T09, T10
- Blocked: T01, T02, T03, T04, T05
- Not proven: T06, T07, T08

## Important rule
This registry does not authorize any workflow dispatch, data sync, or approval override without real records, explicit approval metadata, and validation evidence. The course-data pipeline remains blocked until those conditions are met.

## Source evidence used for this registry
- `pending/course/course-source.json` reads back with `records: []`, `approvedBy: null`, and `approvedAt: null`.
- `state/session-state.json` confirms current phase `phase_5_approval_gated_sync` and overall status `Blocked`.
- `state/phase-status.json` confirms `phase_5_approval_gated_sync` is `Blocked` and related downstream phases are `Not proven`.
- `logs/workflow-evidence.md` confirms actual validation failures on empty pending data and no dispatch of sync.

## Next safe action
Collect real course records with provenance and explicit approved metadata, then validate before any sync. Do not fabricate data or bypass the approval gate.
