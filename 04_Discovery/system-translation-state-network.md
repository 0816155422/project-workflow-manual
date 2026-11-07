# System Translation: State Network

- Record ID: SYS-NET-001
- Classification: USER-CONFIRMED + SOURCE-OBSERVED
- Status: DISCOVERY / NOT CANONICAL
- Parent: SYS-TR-INDEX-001

## 1. Network rule

State means the current position or condition of work. It is not inherently a start or end. A state may connect to other states through actions according to the work context. The network is not forced into one linear Start → Process → End sequence.

This rule is USER_CONFIRMED in the existing reconstruction record and is retained here without defining a new state machine.

## 2. User-confirmed overall cycle network

The known connected relationship is:

IRIS retrieves required data
→ data is available to Temporary Workspace
→ Main AI / MCP execution
→ result exists
→ gate / verification
→ authorized persistence
→ checkpoint / resume update
→ Temporary Workspace cleanup
→ verified output

Classification: USER_CONFIRMED sequence. The exact branch conditions, return edges, parallel paths, restart rules, and bypass conditions of the whole human system remain UNKNOWN unless separately established below.

## 3. Source-observed controller network

The following is a separate network for IRIS Controller v0.6.5:

- Work creation → CREATED.
- Step 1 can enter CHECKING without a previous-step PASS.
- Steps 2–5 require the immediately preceding step's latest run to be PASSED.
- CHECKING → WORKING → VERIFYING → PASSED or FAILED.
- PASSED permits the next numbered step.
- FAILED → error retained + checkpoint retained + audit retained → retry the same step.
- Attempts exhausted → error result; no advancement to the next step.
- All five latest step runs PASSED → final_verify.
- Final match → VERIFIED → DELIVERED.
- Final mismatch → MISMATCH; not delivered.
- get_work_status retrieves the recorded work and related history.

These are source-code observations for the controller package, not a declaration that the entire human operating system has exactly these states.

## 4. Branches / bypasses / loop-backs / returns

| Network behavior | Observed relationship | Provenance |
|---|---|---|
| Branch | Expected/actual match → PASSED; mismatch → FAILED | SOURCE_CODE_OBSERVED |
| Branch | Prior step latest PASSED → next step permitted; otherwise gate violation | SOURCE_CODE_OBSERVED |
| Branch | Final match → DELIVERED; mismatch → not delivered | SOURCE_CODE_OBSERVED |
| Bypass | Step 1 has no previous-step prerequisite | SOURCE_CODE_OBSERVED |
| Loop-back | Failed step → retained records → retry same step | SOURCE_CODE_OBSERVED |
| Restart | Controller checkpoint rows exist, but v0.6.5 checkpoint restore/resume endpoint was not found | UNKNOWN / MISSING TRANSITION |
| Return | Main AI retrieval of external state is USER_CONFIRMED; actual host invocation trace is not present | USER_CONFIRMED / REPOSITORY UNPROVEN |
| Handoff | Modular work sets and use of only necessary handoff information are USER_CONFIRMED; actual room packet file/payload/transport not found | USER_CONFIRMED / REPOSITORY UNCONNECTED |
| Direct jump | No user-system-wide direct-jump rule was established in the inspected evidence | UNKNOWN |
| Parallel path | No higher-level concurrent work coordination contract was established | UNKNOWN |

## 5. Separate discovery/data sequence

The user has supplied the following sequence as a relevant work area:

Raw Collection → Review → Understanding → Mapping → Roadmap → Atomization

The SMPE discovery rule also states: start from real data; record problems, questions, exceptions, gaps, new data, and reasons; do not immediately fix issues, create modules, or change structure.

Representation boundary:
- The sequence itself is USER-SUPPLIED.
- The inspected IRIS v0.6.5 controller does not implement or connect this sequence.
- Stage-specific entry conditions, exit conditions, artifact schemas, responsible actors, and transitions between stages remain UNKNOWN / MISSING TRANSITION.
- No node or edge is invented to make the sequence appear executable.

## 6. Unconnected network segments

- Raw Collection-to-Atomization relative to IRIS Controller v0.6.5.
- Main AI conversation context to a concrete IRIS work_id.
- User-confirmed IRIS Storage Lifecycle to the v0.6.5 work-unit controller.
- Handoff / room / workspace packet to an executable resume point.
- Raw Database to the v0.6.5 SQLite database.
- Temporary Workspace creation and cleanup to repository-visible evidence.
- IRIS Adapter and the package-level MCP/REST adapter/interface.
- SMPE Schema/Gate decisions to actual controller calls.
- AICC evidence records to a specific work unit/step.
- Post-DELIVERED continuation.

Unconnected means the relationship was not established by the inspected source. It does not mean the component does not exist in reality.
