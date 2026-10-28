---
name: resume-state-guard
description: Use before every task in the configured repository. Read state first, resume from the recorded next safe action, preserve checkpoint history, and verify every write by read-back.
---

# ResumeStateGuard

## Purpose and scope
Resume repository work from committed state without restarting from zero. This skill controls only repository state, checkpoint history, evidence logging, and truthful status reporting. Do not broaden scope into business logic or runtime behavior unless explicitly requested. The committed repository state is the source of truth, but every read/write claim must be grounded in the connected repository API.

## Required files — read all six before every task
1. `state/session-state.json`
2. `state/phase-status.json`
3. `state/last-run.json`
4. `state/checkpoints/latest.json`
5. `logs/operation-log.md`
6. `logs/workflow-evidence.md`

Also read the immutable checkpoint named by `latest.json` when it points to one. Read only additional files needed for the active next action. If any required file is missing, inspect both logs first, preserve all existing content, initialize only missing files, create a new immutable checkpoint, and read back each created file. Never infer missing-file status without an actual not-found response.

## Allowed status values
Use exactly one of these status values for every new or normalized status field:
- `Proven`
- `Not proven`
- `Blocked`
- `Inconclusive`

Do not write `success`, `completed`, `failed`, `not_proven`, or lowercase variants into new status fields. When reading legacy state, preserve historical values as observed, map them for reporting, and record any ambiguity rather than silently rewriting history. `Proven` requires specific evidence and successful relevant read-back. Missing required inputs or approvals means `Blocked`. Missing runtime evidence means `Not proven`. Conflicting or ambiguous evidence means `Inconclusive`.

## Core function contracts

### `readCurrentState()`
Read all six required files plus the checkpoint referenced by `latest.json`. Return this shape using only observed values:
```json
{
  "current_phase": null,
  "last_verified_phase": null,
  "status": "Inconclusive",
  "next_action": null,
  "blocker": null,
  "missing_inputs": [],
  "evidence_ref": []
}
```
The nulls/empty arrays above illustrate the return shape; they are not permission to invent repository values. Derive fields from session state, phase status, last run, latest checkpoint, and logs. If state sources conflict, set returned status to `Inconclusive`, preserve conflicting evidence references, and choose a non-destructive next action.

### `getNextAction()`
Call `readCurrentState()` first. Return only the recorded next safe action. Skip phases whose observed status is `Proven` unless newer evidence invalidates that proof. If the active phase is `Blocked`, return the minimum action needed to resolve its actual blocker; do not bypass gates or invent data. If required state is absent or unreadable, return `Blocked` or `Not proven` and name the missing path/read-back issue.

### `saveCheckpoint()`
1. Read current state and inspect checkpoint history before writing.
2. Choose a unique, monotonically increasing checkpoint number/ID; never reuse an existing path.
3. Create a new immutable file under `state/checkpoints/`, with at least `checkpoint_no`, `timestamp`, `phase`, `status`, `summary`, `evidence`, and `next_phase`.
4. Read the new file back from the repository. Confirm it exists, parses as JSON, and required fields match the submitted values.
5. Only after that read-back succeeds, update `state/checkpoints/latest.json` to reference the new immutable checkpoint. Read latest.json back and verify the pointer matches.
6. Never delete or rewrite an older immutable checkpoint. If a write/read-back fails, do not claim the checkpoint was saved; record `Not proven` or `Blocked` after safely capturing the failure.

### `saveEvidence()`
Append to `logs/workflow-evidence.md` or an approved structured evidence file; never replace prior entries. Each entry should include, when applicable and observed: timestamp and task/operation; workflow name or source; run ID only if an actual run ID exists; result/status summary; source URL or commit SHA; relevant file path; evidence URL and read-back result. If no workflow ran, state explicitly that no workflow was dispatched and do not invent a run ID. A workflow definition, page HTML, or generic repository-validation success does not prove domain validation, sync, frontend data rendering, or deployment.

### `markStatus(status, evidence)`
Accept only `Proven`, `Not proven`, `Blocked`, or `Inconclusive`; reject any other value. Never set `Proven` without concrete, relevant evidence and successful read-back. If evidence is absent, choose `Not proven` or `Blocked`; if sources conflict, choose `Inconclusive`. Store evidence references next to the status.

## Required usage order
1. `readCurrentState()`
2. `getNextAction()`
3. Perform only the next safe, in-scope action
4. `saveEvidence()` for observed results, including failures and no-run observations
5. `saveCheckpoint()` to a new immutable file, then update latest pointer
6. Update state files sequentially; never concurrently update the same path
7. Read back each file immediately after writing; verify existence and JSON parsing where applicable
8. Read back all changed files and all six required state/log files before final report
9. Report evidence-backed status, blocker, missing inputs, file paths/SHAs, and one next safe action

## State and write safety
- Read state before every task.
- Never overwrite prior checkpoint content or silently replace state.
- Create/read back a new immutable checkpoint before changing current state.
- Append to logs; preserve prior log lines, failures, and evidence.
- Use current blob SHA for updates and sequential writes.
- After every file write, read it back from the repository. For JSON, parse it and compare required fields; for Markdown, confirm the appended entry is present and prior content remains.
- If read-back fails, mark that write verification `Not proven` or `Blocked`; do not proceed as if it succeeded.
- Never expose secrets, tokens, API keys, or credentials.
- Never claim repository pipeline, sync, frontend, or deployment success based only on plugin creation or static files.

## Final report
Use only the allowed status values. Report what changed; exact paths and verified commit/blob SHAs; current phase and last verified phase; blockers/missing inputs; read-back verification results; whether prior checkpoints remain intact; and the next safe action. Keep plugin/state-layer status separate from business-pipeline status.
