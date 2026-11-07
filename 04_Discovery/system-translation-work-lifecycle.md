# System Translation: Work Lifecycle

- Record ID: SYS-LIFE-001
- Classification: USER-CONFIRMED + SOURCE-CODE-OBSERVED
- Status: DISCOVERY / NOT CANONICAL
- Fundamental relation: State/Condition → Action → State/Condition
- Parent: SYS-TR-INDEX-001

## 1. User-confirmed overall operating cycle

The following relationship was explicitly stated in the user's prior working context. The conditions below are descriptive translations of that stated sequence, not newly named formal states.

| Order as stated | Before condition | Action | After condition | Provenance |
|---|---|---|---|---|
| 1 | Current cycle requires external information/state | IRIS retrieves required data | Required data is available to the cycle | USER_CONFIRMED |
| 2 | Retrieved data is available | Place/use data in Temporary Workspace | Per-cycle working data is available in workspace | USER_CONFIRMED |
| 3 | Required inputs are available in workspace | Main AI / MCP execution occurs | An execution result exists | USER_CONFIRMED |
| 4 | Execution result exists | Gate / verification is applied | Result has a gate/verification outcome | USER_CONFIRMED |
| 5 | Result has the required authorization | Perform authorized persistence | Authorized result is persisted to the appropriate durable location | USER_CONFIRMED |
| 6 | Persisted result exists | Update checkpoint / resume position | A resumable position is recorded/updated | USER_CONFIRMED |
| 7 | Per-cycle work has reached its cleanup point | Clean Temporary Workspace | Temporary working data is cleaned up | USER_CONFIRMED |
| 8 | Required persistence and verification are complete | Produce verified output | Verified output is available | USER_CONFIRMED |

The table preserves the sequence as stated. It does not assert that every task follows one unbranched path, that each action has one universal payload, or that all implementation endpoints are known.

## 2. Source-observed IRIS Controller v0.6.5 work-unit sub-lifecycle

This is a bounded sub-lifecycle observed in the separate IRIS Controller v0.6.5 source package. It must not be substituted for the whole user-confirmed IRIS lifecycle.

### Event IRIS-SRC-WORK-001 — Create work

- BEFORE CONDITION: A request supplies work_id and title; no prior numbered step is required by the inspected source.
- ACTION: create_work.
- AFTER CONDITION: A work unit exists with status CREATED and current_step 0; WORK_CREATED audit entry is stored.
- NEXT RELATION: A caller may request a step for the existing work unit.
- BRANCH/BYPASS: Creation does not require a preceding step.
- SOURCE: Prasong1993/Prasong, IRIS/iris-controller-v0.6.5/runtime/controller.py and runtime/database.py.

### Event IRIS-SRC-WORK-002 — Gate a requested step

- BEFORE CONDITION: Work unit exists. Step 1 has no preceding-step requirement. For step N greater than 1, the latest run of step N-1 must be PASSED.
- ACTION: Caller invokes run_step; controller checks the gate and records CHECKING.
- AFTER CONDITION: The requested step enters its attempt path, or the request is rejected by the gate.
- SOURCE: runtime/controller.py, runtime/model.py, runtime/mcp_server.py, runtime/main.py.

### Event IRIS-SRC-WORK-003 — Execute and compare

- BEFORE CONDITION: Attempt is recorded as CHECKING.
- ACTION: Controller records WORKING, then VERIFYING, and compares expected and actual values.
- AFTER CONDITION: Match produces PASSED; mismatch produces FAILED.
- BRANCH: PASSED / FAILED.
- SOURCE: runtime/controller.py and runtime/model.py.

### Event IRIS-SRC-WORK-004 — Retain failure and retry

- BEFORE CONDITION: Attempt has FAILED.
- ACTION: Error, checkpoint, and audit records are retained; the controller retries the same requested step within its bounded attempt loop.
- AFTER CONDITION: Another attempt begins, or attempts are exhausted and an error result is returned.
- LOOP-BACK: FAILED → retained error/checkpoint/audit → retry same step.
- SOURCE: runtime/controller.py and runtime/mcp_server.py.

### Event IRIS-SRC-WORK-005 — Permit next step

- BEFORE CONDITION: Latest run of the immediately preceding step is PASSED.
- ACTION: Caller requests the next numbered step; controller checks the prior-step result.
- AFTER CONDITION: The next step may enter CHECKING.
- BRANCH: Gate met / gate violation.
- SOURCE: runtime/controller.py.

### Event IRIS-SRC-WORK-006 — Final verification and delivery

- BEFORE CONDITION: Latest run of all five defined steps is PASSED.
- ACTION: Caller invokes final_verify with expected and actual values.
- AFTER CONDITION: Match produces VERIFIED and work status DELIVERED. Mismatch remains MISMATCH and is not delivered.
- SOURCE: runtime/controller.py, runtime/main.py, runtime/mcp_server.py.

### Event IRIS-SRC-WORK-007 — Retrieve work state

- BEFORE CONDITION: A work identifier is supplied.
- ACTION: get_work_status / get_work reads the work unit and associated history.
- AFTER CONDITION: Caller receives available work metadata, step runs, errors, checkpoints, audit, and verifications.
- SOURCE: runtime/controller.py, runtime/database.py, runtime/main.py, runtime/mcp_server.py.

## 3. Lifecycle boundary and differences

- The user-confirmed overall cycle includes retrieval, temporary workspace, AI/MCP execution, gate/verification, authorized persistence, checkpoint/resume update, workspace cleanup, and verified output.
- The inspected v0.6.5 controller package directly demonstrates a work-unit five-step controller, SQLite records, retry, final verification, and retrieval.
- The v0.6.5 source does not demonstrate the full user-confirmed Storage Lifecycle, Temporary Workspace cleanup, Main AI context binding, cross-room handoff, or the Raw Collection-to-Atomization process.
- The existence of a checkpoint table does not establish checkpoint restoration. The inspected v0.6.5 API has no checkpoint-resume operation.
- The working-branch iris_runtime package contains a later repository-side resume/handoff implementation. It is recorded as a separate implementation artifact, not as evidence that those transitions existed in the original human operating system.

## 4. Unresolved lifecycle relationships

- Exact entry condition for a new human work cycle: UNKNOWN.
- Exact relation between IRIS Storage Lifecycle and IRIS Workflow Lifecycle: USER_CONFIRMED as inseparable components; detailed transition map: UNKNOWN.
- Exact conditions/authority for gate approval and independent verification: partially USER_CONFIRMED; per-event schema and actor binding: UNKNOWN.
- Exact external persistence target for each data class: UNKNOWN.
- Exact workspace cleanup condition and proof: UNKNOWN.
- Resume from the existing Storage Lifecycle and from room handoff: USER-CONFIRMED as concepts where stated; concrete repository transition and payload: UNCONNECTED.
- Post-delivery continuation: UNKNOWN.
