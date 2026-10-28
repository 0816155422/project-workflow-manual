---
name: resume-state-guard
description: Use before every task in this repository to resume from committed state, perform only the next safe action, and record append-only evidence.
---

# ResumeStateGuard

This repository's committed state is the source of truth. Before every task, use the GitHub connector to read these exact paths on `main`:
- `state/session-state.json`
- `state/phase-status.json`
- `state/last-run.json`
- `state/checkpoints/latest.json`
- `logs/operation-log.md`
- `logs/workflow-evidence.md`

Then read any source, workflow, script, or output file required by the current phase. Never assume repository HTML or a workflow definition proves runtime behavior.

## Required methods

### `readCurrentState()`
Return `current_phase`, `last_verified_phase`, `status`, `next_action`, `blocker`, `missing_inputs`, and `evidence_ref` from read-back state. Do not invent missing values. If state files are absent, inspect existing logs first, initialize only missing files, and record that fact in a new checkpoint.

### `getNextAction()`
Continue from the recorded phase and next action. Skip phases already proven unless new evidence invalidates them. If required input is missing, stop at the blocker and name the minimum safe next action. Do not restart from zero or bypass validation/approval gates.

### `saveEvidence()`
Append only observed evidence: workflow name, real run ID, conclusion, commit SHA, evidence URL, validation output, source URL/provenance, and read-back result as applicable. A workflow definition is not a run. A generic repository validation success does not prove course validation, sync, frontend rendering, or deployment of current HEAD. If no run exists, say so; never invent a run ID or success.

### `saveCheckpoint()`
Create a new immutable file such as `state/checkpoints/CKPT-YYYYMMDD-NNN.json` first, with checkpoint number/ID, timestamp, phase, status, summary, evidence, and next phase/action. Only after its commit is returned may you update `state/checkpoints/latest.json`. Never delete or replace historical checkpoint files.

### `markStatus()`
Use exactly one of these user-facing statuses: `Proven`, `Not proven`, `Blocked`, `Inconclusive`. `Proven` requires concrete evidence and relevant read-back. Missing real data or approval means `Blocked`; missing runtime evidence means `Not proven`; conflicting evidence means `Inconclusive`.

## Safe sequence

1. Read all six required state/log files before every task.
2. Inspect current phase, proven phases, last run, blockers, and next action.
3. Perform only the next safe action; never fabricate course records, provenance, approval, commits, workflow runs, or results.
4. Append to both logs. Never remove or rewrite historical entries.
5. Create an immutable checkpoint before changing current state; update the latest pointer only after the immutable checkpoint commit is confirmed.
6. Update state files sequentially, using the latest blob SHA for each write. Never race writes to the same path.
7. Read back every changed file and the checkpoint; record commit/blob SHAs. If read-back fails, status is `Not proven`.
8. Never dispatch approval-gated sync unless real provenance-backed records pass validation and explicit authorized approval is verified.
9. Never expose secrets or credentials.

## Current known blocker (revalidate on every invocation)

The latest observed read-back of `pending/course/course-source.json` had `records: []`, `approvedBy: null`, and `approvedAt: null` (blob SHA `90c325b0694e1ecc89b411787a4ae4fdd19b9295`). Therefore do not approve or sync based on this snapshot. Obtain real course records with source URL/provenance and an explicit authorized approval, then validate before sync.

## Final report

Report overall status, current phase, last verified phase, evidence references, blocked/not-proven phases, missing inputs, changed files and verified SHAs, and one clear next safe action. Never claim success without actual workflow logs, validation output, or file read-back verification.
