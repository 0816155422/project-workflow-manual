# IRIS Controller Operating Structure + Work Lifecycle Reconstruction

- Record ID: `iris-controller-operating-work-lifecycle-reconstruction`
- Revision: `R1`
- Status: `Proven` for source-backed reconstruction and repository read-back only
- Knowledge classification: `USER-CONFIRMED / RECONSTRUCTION / NOT CANONICAL`
- Runtime verification: `NOT REQUIRED FOR CURRENT RECONSTRUCTION STAGE`
- Created: `2026-11-08`
- Working repository: `0816155422/project-workflow-manual`
- Working branch: `reconstruction/operating-work-lifecycle-state`
- Parent checkpoint: `CKPT-20261108-006`
- Parent working-branch commit: `a533dbd1dc510ba312f920a6ac53c1f89a81983e`

## 1. Scope and reconstruction method

This record reconstructs only the Operating Structure + Work Lifecycle relationships exposed by the inspected IRIS Controller v0.6.5 source and the repository's existing IRIS research records. It does not redesign the controller, infer an implementation beyond inspected source, or treat code/data structures as the operating lifecycle.

Fundamental relation:

`State/Condition → Action → State/Condition`

The BEFORE and AFTER descriptions below are descriptive candidate conditions derived from source behavior. They are not newly implemented or formally named State Machine states.

## 2. Source inventory and provenance

### 2.1 Target repository evidence

Inspected the target repository's working branch tree and the other currently listed branches. The current working branch contains the previously persisted user-confirmed Discovery record and state files, but no IRIS Controller source package.

The branch `feature/init-gh-native-structure` contains these IRIS research records:
- `03_Research/IRIS/IRIS_DATA_FRESHNESS_AND_MERGE_REVIEW.md` — blob `58f161ec7320ee3ab3556db610b7f672c1bdef65`
- `03_Research/IRIS/IRIS_V065_SOURCE_CODE_AUDIT.md` — blob `e7495f7dbebed34a71b1c2853558bc95b16ad0f9`

The current target-repository branch list observed:
- `main` — `48e9f64bebd7fb3821d6d03377d3713c46e51193`
- `reconstruction/operating-work-lifecycle-state` — `a533dbd1dc510ba312f920a6ac53c1f89a81983e`
- `feature/init-gh-native-structure` — `f4e14597f4e6c908af165a6244472344210727c0`
- `adapter/iris-evidence-template` — `b3d4a04db0b37be4520812877f1777f6b8d9b02c`
- `feat/github-actions-api-runner` — `c85259b5fc86de18308ae697e613ba2eb9ad3f34`
- `0816155422-patch-1` — `1821fb148d2d676bc7d2351ab6b96cedf4ae7df9`

No IRIS Controller implementation files were found in the current working branch tree. The target branch's IRIS materials are review/audit documents, not the controller runtime source.

### 2.2 Source repository evidence

Source repository: `Prasong1993/Prasong`, branch `main`, observed HEAD `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`.

The current source tree exposes:
- `IRIS/iris-controller-v0.6.2/`
- `IRIS/iris-controller-v0.6.5/`

No separate `iris-step1` or `IRIS Project Controller` package was present in the inspected current source tree. This is a bounded search observation, not a claim that such material does not exist elsewhere.

v0.6.5 source files inspected by blob:
- `runtime/controller.py` — `194c81e48dadf5f89a6c5e14731b5288b86164f8`
- `runtime/model.py` — `92beff61b7f113a6395ae38712c529bad252da13`
- `runtime/database.py` — `c3937168f3904b804948c7a090ffd8f7f43cd11c`
- `runtime/mcp_server.py` — `e8851bb16101245f05eace2ead1e82868ef0c919`
- `runtime/main.py` — `7a883223a0f5dcccf3c9fa45800ae628e6e032dc`
- `runtime/verify.py` — `6865448f4091bdeec9f4aab62f3b4ff12f2464c6`
- `skills/iris/SKILL.md` — `58828bc0cd8c565a08aa4320534362685f068790`
- `docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md` — `d5322ead6eecddac1a5ebecc57553195bbced48e`
- `README.md` — `1aef014fbeda4e1c98241d0c5da4f43d34a6532e`
- `IRIS_VALIDATION_v0.6.5.md` — `8ab1d9fa2583d20a7dff68878f3f40454a6577e6`

The source audit and freshness review are repository records. The runtime source itself was inspected through GitHub blob reads. No runtime execution was performed in this reconstruction.

## 3. Operating Structure

### 3.1 Observed operating responsibilities

The v0.6.5 source shows these operational responsibilities:

1. A caller supplies a work identifier and title to create a work unit.
2. A caller requests a particular numbered work step with expected and actual values.
3. The controller checks that the work exists and, for steps after the first, that the immediately previous step's latest recorded run is `PASSED`.
4. The controller records progress conditions, compares expected and actual values, and records a pass or failure result.
5. On a failed attempt, the controller retains an error and checkpoint, then retries the same requested step within the bounded attempt loop.
6. A later step is permitted only after the preceding step's latest run is `PASSED`.
7. Final verification is permitted only when the latest recorded run for all five required steps is `PASSED`.
8. Final `VERIFIED` changes the work unit status to `DELIVERED`. A mismatch is retained as a mismatch and does not deliver the work.
9. Read operations return the work unit and its recorded step runs, errors, checkpoints, audit records, and verification records.

These are responsibilities visible in the inspected implementation. They do not establish who the human or AI operator is, how a Main AI chooses the task, or any authority beyond the explicit API/tool inputs.

### 3.2 Supporting interfaces and tools, not the operating structure itself

- `controller.py`: implements work creation, step gating, attempt/retry handling, comparison, status updates, error retention, and checkpoint writes.
- MCP stdio server: exposes `health`, `create_work`, `run_step`, `final_verify`, `get_work_status`, `add_evidence`, and `list_evidence`.
- FastAPI REST interface: exposes health, structure, evidence, work creation, work inspection, step execution, and final verification endpoints.
- `database.py` / SQLite: persists work, step runs, errors, checkpoints, verifications, evidence, and audit rows.
- `model.py`: defines the five step names and status vocabulary.
- `verify.py`: contains an expected/actual equality helper; the inspected controller defines and uses its own `verify_pair` helper.
- Agent Skill: instructs an agent to use MCP tools and not simulate execution.
- `IRIS_DB_PATH`: selects the SQLite database location.
- Checkpoint rows: persist snapshots for failed and passed step attempts; no checkpoint-restore/resume operation was found in the inspected controller/API/MCP source.
- `get_work_status`: retrieval interface for recorded work state and history.

These are supporting implementation and access mechanisms. They are not treated as independent operating actors or lifecycle states.

## 4. Work Lifecycle and Event Register

### EVENT IRIS-WORK-001 — Create work

- BEFORE CONDITION: A create request with `work_id` and `title` is supplied. A named pre-existing work State is not required by the source; prior existence is UNKNOWN.
- ACTION: `create_work(work_id, title)`.
- AFTER CONDITION: Work row exists with default status `CREATED`, `current_step=0`; audit action `WORK_CREATED` is inserted.
- CONTINUATION: `run_step` can be requested for an existing work unit.
- BRANCH: Duplicate identifier is returned as a structured conflict at the MCP/REST boundary.
- BYPASS: No preceding numbered work step is required for creation.
- LOOP-BACK: None observed.
- SOURCE: `runtime/controller.py` blob `194c81e...`; `runtime/database.py` blob `c393716...`; `runtime/mcp_server.py` blob `e8851bb...`; `runtime/main.py` blob `7a88322...`.
- UNKNOWN: How the caller obtains/chooses the identifier; whether an external task lifecycle precedes creation.

### EVENT IRIS-WORK-002 — Start/check a requested step

- BEFORE CONDITION: Work unit exists. For step 1, no previous step is required. For step N greater than 1, latest run of step N-1 must be `PASSED`.
- ACTION: `run_step(work_id, step, expected, actual, ...)`; controller writes a `CHECKING` step-run record.
- AFTER CONDITION: Latest recorded run for the requested step is `CHECKING`; work unit current_step/status are updated to that step and condition.
- CONTINUATION: On the normal attempt path, `WORKING` follows.
- BRANCH: Missing work, invalid step, or unmet previous-step gate returns an error and does not proceed through the step attempt.
- BYPASS: Step 1 bypasses the previous-step check by explicit condition `step > 1`.
- LOOP-BACK: A later failure path can return to a new attempt of the same requested step.
- SOURCE: `runtime/controller.py`; `runtime/model.py`; REST and MCP entry points.
- UNKNOWN: The external action that causes the caller to request a step.

### EVENT IRIS-WORK-003 — Execute and verify an attempt

- BEFORE CONDITION: Current attempt is recorded as `CHECKING`.
- ACTION: Controller records `WORKING`, then `VERIFYING`, then compares stripped string forms of expected and actual values.
- AFTER CONDITION: Either `PASSED` when values match, or `FAILED` when values do not match.
- CONTINUATION: `PASSED` allows the next permitted step; `FAILED` enters retained-failure handling.
- BRANCH: Match → `PASSED`; mismatch → `FAILED`.
- BYPASS: No source-observed path skips comparison on the normal attempt path.
- LOOP-BACK: A failed attempt continues the bounded loop for the same requested step.
- SOURCE: `runtime/controller.py` blob `194c81e...`; `runtime/model.py` blob `92beff6...`.
- UNKNOWN: Whether the actual work producing `actual` is performed by the same caller, another agent, or an external system.

### EVENT IRIS-WORK-004 — Retain failed attempt and retry

- BEFORE CONDITION: An attempt is either forced into the configured `fail_attempts` path, or the expected/actual comparison mismatches.
- ACTION: Controller records `FAILED`; writes an error row and audit event; writes a checkpoint snapshot; then continues the same step's bounded attempt loop.
- AFTER CONDITION: Failure remains in `step_runs`, `errors`, `checkpoints`, and `audit_log`; the same requested step is attempted again if attempts remain.
- CONTINUATION: Retry same step; if the attempt limit is exhausted, a runtime error / structured `ATTEMPTS_EXHAUSTED` is returned.
- BRANCH: Condition-not-met failure and expected/actual mismatch have distinct error types/messages.
- BYPASS: The failure-retention branch does not advance to the next step.
- LOOP-BACK: Explicit loop-back to the same step's next attempt.
- SOURCE: `runtime/controller.py` blob `194c81e...`; `runtime/mcp_server.py` blob `e8851bb...`.
- UNKNOWN: Any external correction process between attempts; source only records a note and retries with the supplied expected/actual arguments.

### EVENT IRIS-WORK-005 — Permit next step

- BEFORE CONDITION: Latest run of the preceding step is `PASSED`.
- ACTION: Caller requests the next numbered step; controller checks the previous step's latest status.
- AFTER CONDITION: Next step can enter `CHECKING`.
- CONTINUATION: Repeats the check/execute/verify/failure-retention cycle for the requested step.
- BRANCH: Previous latest run not `PASSED` → gate violation; previous latest run `PASSED` → permitted.
- BYPASS: No bypass of the immediately previous step gate is exposed in inspected `run_step`.
- LOOP-BACK: A failed new step retries itself, not the previous passed step.
- SOURCE: `runtime/controller.py` blob `194c81e...`.
- UNKNOWN: Any parallel or out-of-order work behavior outside this controller call.

### EVENT IRIS-WORK-006 — Final verification

- BEFORE CONDITION: Work exists and the latest run of each of the five defined steps is `PASSED`.
- ACTION: Caller invokes `final_verify` with expected and actual values; the final verifier compares stripped values and writes a verification row plus audit event.
- AFTER CONDITION: Match → verification status `VERIFIED`, work status updated to `DELIVERED`. Mismatch → verification status `MISMATCH`, work is not marked `DELIVERED`.
- CONTINUATION: `VERIFIED / DELIVERED` is the terminal result explicitly shown for this package. Post-delivery use is UNKNOWN.
- BRANCH: Missing/failed step gate rejects final verification; comparison match and mismatch diverge.
- BYPASS: Final verification cannot bypass the five-step latest-`PASSED` requirement.
- LOOP-BACK: No automatic final-verification retry loop is implemented in the inspected function; an external subsequent invocation/correction path is UNKNOWN.
- SOURCE: `runtime/mcp_server.py` blob `e8851bb...`; `runtime/main.py` blob `7a88322...`; contract blob `d5322ea...`.
- UNKNOWN: What consumes a delivered result next; whether there is another lifecycle outside this package.

### EVENT IRIS-WORK-007 — Retrieve work state/history

- BEFORE CONDITION: A work identifier is supplied; work must exist for the full work record to be returned.
- ACTION: `get_work` / MCP `get_work_status` / REST `GET /work/{work_id}`.
- AFTER CONDITION: Caller receives work metadata and ordered step runs, errors, checkpoints, audit rows, and verification rows.
- CONTINUATION: Caller may use the returned information in its own context; any next action is external to this retrieval function.
- BRANCH: Unknown work identifier returns not-found.
- BYPASS: Retrieval does not execute a step or change work status in the inspected implementation.
- LOOP-BACK: Repeated reads are possible; no read-triggered lifecycle transition observed.
- SOURCE: `runtime/controller.py`, `runtime/mcp_server.py`, `runtime/main.py`.
- UNKNOWN: Whether retrieval automatically resumes work; no automatic resume behavior was found.

### EVENT IRIS-WORK-008 — Add/list evidence

- BEFORE CONDITION: Evidence fields are supplied for `add_evidence`; no work_id relation is required by the inspected evidence table/API.
- ACTION: Insert evidence row, or list evidence rows.
- AFTER CONDITION: Evidence item exists in the separate evidence table, or a list is returned.
- CONTINUATION: No explicit link from evidence rows to a work unit or numbered step was found in the inspected schema/functions.
- BRANCH: Duplicate evidence ID returns conflict; invalid required fields return validation error.
- BYPASS: This evidence path can operate without creating a work unit.
- LOOP-BACK: None observed.
- SOURCE: `runtime/database.py`, `runtime/mcp_server.py`, `runtime/main.py`.
- UNKNOWN: How evidence is reviewed, understood, mapped, roadmapped, or atomized; whether an external process links it to work.

## 5. Connected Segments: One Expandable Network

The following connections are directly supported by the inspected implementation:

1. `Create request → CREATED work unit → request step 1`.
2. `Existing work + permitted step request → CHECKING → WORKING → VERIFYING`.
3. `VERIFYING + matching expected/actual → PASSED → request next permitted numbered step`.
4. `VERIFYING + mismatch → FAILED → error + checkpoint + audit retained → retry same step`.
5. `Configured fail_attempts condition → FAILED → error + checkpoint + audit retained → retry same step`.
6. `Previous step latest PASSED → next step request permitted`.
7. `All five latest step runs PASSED → final_verify`.
8. `final_verify VERIFIED → work status DELIVERED`.
9. `get_work_status / GET work → recorded work + step/error/checkpoint/audit/verification history returned`.

These segments are one connected work network through the shared work identifier and controller functions. The numbered steps are the order enforced by this v0.6.5 implementation, not a claim that all IRIS lifecycles in other versions or systems must be linear.

## 6. Unconnected Segments

- `add_evidence / list_evidence` is a separate evidence path. No explicit work_id/step relationship was found in the inspected schema; retain as an unconnected segment.
- Raw Collection → Review → Understanding → Mapping → Roadmap → Atomization: no such sequence or connection was found in the inspected v0.6.5 controller source. Relationship to the separate evidence table is UNKNOWN.
- Main AI conversation lifecycle and external task selection: UNCONNECTED; the skill documents tool use, but no source event binds conversational state to a work unit.
- Continuous execution outside the bounded retry loop in `run_step`: UNKNOWN / not present in inspected implementation.
- Separate IRIS Step 1 package: UNKNOWN / not found in inspected target repository branch set or current source repository tree.
- Handoff, Room/Workspace packet, cross-room transfer, and persistent Resume operation: UNKNOWN / no matching implementation event found in inspected package.
- Project-level controller distinct from `runtime/controller.py`: UNKNOWN.
- Post-`DELIVERED` continuation: UNKNOWN.

## 7. Branches, Bypasses, and Loop-backs

### Branches
- Duplicate work ID → conflict response.
- Invalid/missing work or invalid step → error response.
- Previous step not latest-`PASSED` → gate violation.
- Expected/actual match → `PASSED`.
- Expected/actual mismatch → `FAILED`.
- Retry attempts exhausted → attempts-exhausted result.
- Final verification gate incomplete → final verification rejected.
- Final comparison match → `VERIFIED / DELIVERED`.
- Final comparison mismatch → `MISMATCH`, not delivered.
- Duplicate evidence ID / invalid evidence fields → conflict / validation response.

### Bypasses
- Step 1 has no previous-step prerequisite.
- No bypass around the previous-step `PASSED` check for steps 2–5 was found.
- Evidence insertion/listing is independent of a work unit in the inspected schema.
- No bypass from `FAILED` to next step was found.

### Loop-backs
- `FAILED` step attempt → retained error/checkpoint/audit → next attempt of the same step.
- The retry loop is bounded by `max_attempts` (default 10 in controller; MCP input schema limits maximum to 10).
- No loop-back from final mismatch is implemented inside `final_verify`; any subsequent correction/re-invocation is external/UNKNOWN.

## 8. Supporting Tools Register

| Supporting tool/interface | Observed role | Boundary |
|---|---|---|
| Controller | Orchestrates requested work/step operations, gates, retries, records results | Not the source of user intent or external actual work |
| MCP server | Makes controller functions callable as tools | Host binding/actual target-host connection not proven here |
| REST API | Exposes corresponding HTTP operations | Does not establish a Main AI interaction |
| SQLite database | Persists work and event history | Storage layer, not Operating Structure |
| Checkpoint rows | Preserve per-attempt snapshots | Restore/resume function not found |
| Audit log | Records work-created, step-status, error, checkpoint, final-verification events | Does not itself choose next action |
| Error records | Retain failure detail and correction/verification fields | Root cause may remain UNKNOWN/UNPROVEN |
| Agent Skill | Instructs an agent to use MCP tools and avoid simulated execution | Instruction document, not proof of host invocation |
| Work/evidence IDs | Identify work and evidence records | ID generation/assignment authority is not specified |

## 9. Main AI ↔ IRIS Interaction

Documented intention:
- The v0.6.5 Agent Skill says to use MCP tools and not simulate execution.
- The MCP server exposes tools for work creation, step execution, final verification, retrieval, and evidence access.
- `get_work_status` returns stored work state/history to the calling client.

Not established:
- No actual Main AI invocation trace was found in the inspected repository/source records.
- No explicit context serialization or context-return contract was found.
- No automatic transfer of conversational context into IRIS was found.
- Target-host binding of `.mcp.json` remains unproven in the source audit/validation records.

Therefore: Main AI ↔ IRIS operational interaction is `PARTIALLY DOCUMENTED / ACTUAL INVOCATION UNKNOWN`. No contract is inferred.

## 10. Data-Lifecycle Relationship

| Data activity | Observed relation to IRIS v0.6.5 |
|---|---|
| Raw Collection | UNKNOWN |
| Review | UNKNOWN |
| Understanding | UNKNOWN |
| Mapping | UNKNOWN |
| Roadmap | UNKNOWN |
| Atomization | UNKNOWN |
| Evidence add/list | Implemented separate evidence table/interface; no explicit work/step link found |

Classification: `UNCONNECTED SEGMENT` for the broader data-lifecycle chain. The evidence table is a supporting facility, not proof that the broader data lifecycle is part of the work lifecycle.

## 11. Unknown Register

- UNKNOWN STATE: Caller state before work creation; external condition after delivery.
- UNKNOWN ACTION: External work that produces actual values; correction action between retry attempts; any action after delivery.
- UNKNOWN TRANSITION: Work handoff to another agent/room; restart/resume from a stored checkpoint; Main AI context ↔ IRIS state transition.
- UNKNOWN SOURCE: Separate IRIS Step 1 package; IRIS Project Controller distinct from v0.6.5 Controller; Continuous Execution system outside the retry loop.
- UNKNOWN DESTINATION: Consumer of `DELIVERED`; downstream data lifecycle destination.
- UNCONNECTED SEGMENT: Evidence add/list path relative to work units; Raw Collection through Atomization; Main AI conversation; handoff/room/resume.
- MISSING INTERMEDIATE RELATIONSHIP: Any mapping from evidence records to work units/steps; any relationship between external correction and retry.
- UNKNOWN: Whether parallel work units or concurrent actors coordinate through a higher-level controller.

These unknowns do not block the source-backed segments above.

## 12. Source discrepancy register

1. The target repository's `IRIS_DATA_FRESHNESS_AND_MERGE_REVIEW.md` and v0.6.5 five-step contract describe REST and MCP final-mismatch persistence as equivalent.
2. Direct inspection of `runtime/main.py` shows REST final mismatch inserts `verifications` and `audit_log`, then returns HTTP 409; it does not call `record_error` or `checkpoint`.
3. Direct inspection of `runtime/mcp_server.py` shows MCP final mismatch additionally calls `record_error` and `checkpoint`.
4. The source audit `IRIS_V065_SOURCE_CODE_AUDIT.md` also records this REST/MCP difference.

Classification: `SOURCE DOCUMENT / CONTRACT DISCREPANCY`. The differing source statements are preserved here; this reconstruction does not modify code or resolve the discrepancy.

## 13. Current Reconstruction Position

- Operating Structure: `PARTIALLY RECONSTRUCTED FROM SOURCE`.
- Work Lifecycle: `PARTIALLY RECONSTRUCTED FROM SOURCE`.
- Connected network: the v0.6.5 work-unit/step/retry/final-verification/retrieval path listed in Section 5.
- Unconnected segments and unknowns: retained in Sections 6, 9, 10, and 11.
- Knowledge classification: `USER-CONFIRMED / RECONSTRUCTION / NOT CANONICAL`.
- Runtime verification: `NOT REQUIRED FOR CURRENT RECONSTRUCTION STAGE`.
- Current position: the source-backed v0.6.5 work lifecycle has been assembled to the limit of the inspected material. No next system or future component is designed here.

## 14. Source References

Target repository:
- `0816155422/project-workflow-manual`, branch `feature/init-gh-native-structure`, commit observed from branch list `f4e14597f4e6c908af165a6244472344210727c0`.
- `03_Research/IRIS/IRIS_DATA_FRESHNESS_AND_MERGE_REVIEW.md`, blob `58f161ec7320ee3ab3556db610b7f672c1bdef65`.
- `03_Research/IRIS/IRIS_V065_SOURCE_CODE_AUDIT.md`, blob `e7495f7dbebed34a71b1c2853558bc95b16ad0f9`.

Source repository:
- `Prasong1993/Prasong`, branch `main`, HEAD `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`.
- `IRIS/iris-controller-v0.6.5/runtime/controller.py`, blob `194c81e48dadf5f89a6c5e14731b5288b86164f8`.
- `IRIS/iris-controller-v0.6.5/runtime/model.py`, blob `92beff61b7f113a6395ae38712c529bad252da13`.
- `IRIS/iris-controller-v0.6.5/runtime/database.py`, blob `c3937168f3904b804948c7a090ffd8f7f43cd11c`.
- `IRIS/iris-controller-v0.6.5/runtime/mcp_server.py`, blob `e8851bb16101245f05eace2ead1e82868ef0c919`.
- `IRIS/iris-controller-v0.6.5/runtime/main.py`, blob `7a883223a0f5dcccf3c9fa45800ae628e6e032dc`.
- `IRIS/iris-controller-v0.6.5/runtime/verify.py`, blob `6865448f4091bdeec9f4aab62f3b4ff12f2464c6`.
- `IRIS/iris-controller-v0.6.5/skills/iris/SKILL.md`, blob `58828bc0cd8c565a08aa4320534362685f068790`.
- `IRIS/iris-controller-v0.6.5/docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md`, blob `d5322ead6eecddac1a5ebecc57553195bbced48e`.
- `IRIS/iris-controller-v0.6.5/README.md`, blob `1aef014fbeda4e1c98241d0c5da4f43d34a6532e`.
- `IRIS/iris-controller-v0.6.5/IRIS_VALIDATION_v0.6.5.md`, blob `8ab1d9fa2583d20a7dff68878f3f40454a6577e6`.

No source code was modified, no runtime was executed, no canonical promotion was performed, and no merge to `main` was performed.
