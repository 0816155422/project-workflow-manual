# RELATIONSHIP_DISCOVERY

- Discovery Timestamp: 2026-11-08
- Repository Reference: 0816155422/project-workflow-manual
- Repository ID: 1432201372
- Reference Branch: reconstruction/operating-work-lifecycle-state
- Evidence Source: Direct read-back of existing relationship register, state-network record, operating-structure record, lifecycle record, source register, and unknown/conflict register.

## Discovery Result

- Existing explicit relationship records: FOUND (20 records).
- Existing explicit unknown/unconnected records: FOUND (18 records).
- Existing conflict records: FOUND (7 records).
- New relationships inferred in this task: NONE.
- Canonical relationship model: NOT ESTABLISHED. The source relationship records are marked DISCOVERY / NOT CANONICAL.

## Existing Relationship Register

Source: `04_Discovery/system-translation-system-relationships.md`
Source Record ID: SYS-REL-001
Source Classification: USER-CONFIRMED + REPOSITORY-OBSERVED
Source Status: DISCOVERY / NOT CANONICAL
Source Blob SHA: `b4dda7b009f6208111f08a401012781b0158b03e`

| ID | From | Recorded Relation | To | Provenance | Recorded Boundary |
|---|---|---|---|---|---|
| REL-001 | Main AI | invokes as extension/tool to retrieve needed state/data | IRIS | USER_CONFIRMED | Actual host invocation trace not found |
| REL-002 | IRIS | coordinates | Storage Lifecycle | USER_CONFIRMED | Storage Lifecycle must remain intact |
| REL-003 | IRIS | coordinates | Workflow Lifecycle | USER_CONFIRMED | Exact complete event map still being extracted |
| REL-004 | IRIS | includes | First IRIS Adapter | USER_CONFIRMED | Not equivalent to SMPE Adapter |
| REL-005 | HAP | constrains operating environment/actions | IRIS and related work | USER_CONFIRMED | Exact enforcement point for each policy not fully mapped |
| REL-006 | SMPE | governs schema/process/validation/gates | relevant work operations | USER_CONFIRMED | Concrete schema-to-controller call mapping absent |
| REL-007 | AICC | manages | data/evidence/records | USER_CONFIRMED | Exact record-to-work ID links incomplete |
| REL-008 | IRIS | retrieves required data | external state / Raw Database | USER_CONFIRMED | Physical store and API binding unresolved |
| REL-009 | IRIS | makes retrieved data available to | Temporary Workspace | USER_CONFIRMED | Runtime workspace implementation unresolved |
| REL-010 | Main AI / MCP | executes work using required context/data | current cycle | USER_CONFIRMED | Exact host invocation and payload contract unresolved |
| REL-011 | result | is subject to | Gate / Verification | USER_CONFIRMED | Gate schema and actor authority need source mapping |
| REL-012 | authorized result | is persisted to | durable state | USER_CONFIRMED | Exact target mapping unresolved |
| REL-013 | persistence result | updates | Checkpoint / Resume position | USER_CONFIRMED | Existing v0.6.5 source lacks resume endpoint |
| REL-014 | cycle completion | triggers | Temporary Workspace cleanup | USER_CONFIRMED | Cleanup trigger and evidence format unresolved |
| REL-015 | completed cycle | produces | verified output | USER_CONFIRMED | Output location/consumer unresolved |
| REL-016 | IRIS Controller v0.6.5 | persists work/run/error/checkpoint/audit | SQLite database | SOURCE_CODE_OBSERVED | Package-local implementation only |
| REL-017 | MCP/REST interfaces | expose operations | IRIS Controller v0.6.5 | SOURCE_CODE_OBSERVED | Host binding not proven |
| REL-018 | GitHub Actions | validates/records repository artifacts | GitHub repository | REPOSITORY_OBSERVED | Workflow run results must be inspected individually |
| REL-019 | HAP/AICC dashboard | reads approved dataset path | repository data/course-data.json | REPOSITORY_OBSERVED | Manifest says no approved dataset has been written |
| REL-020 | approval-gated sync workflow | copies reviewed pending source to shared destination | shared repository memory | REPOSITORY_OBSERVED | Manual approval required; current course source is empty |

## Existing State-Network Relationships

Source: `04_Discovery/system-translation-state-network.md`
Source Record ID: SYS-NET-001
Source Status: DISCOVERY / NOT CANONICAL
Source Blob SHA: `8dd9e06ca903522296330e55d27a584ece325a20`

### User-confirmed overall cycle sequence

The source records this sequence:
1. IRIS retrieves required data.
2. Data is available to Temporary Workspace.
3. Main AI / MCP execution occurs.
4. Result exists.
5. Gate / verification is applied.
6. Authorized persistence occurs.
7. Checkpoint / resume position is updated.
8. Temporary Workspace cleanup occurs.
9. Verified output is produced.

The source explicitly says exact branch conditions, return edges, parallel paths, restart rules, and bypass conditions of the whole human system remain UNKNOWN unless separately established.

### Source-observed IRIS Controller v0.6.5 sub-lifecycle

The source separately records:
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

These records are explicitly bounded to the controller package and are not asserted to describe the entire human operating system.

### Existing branch / bypass / loop-back / return records

| Behavior | Recorded Relationship | Provenance |
|---|---|---|
| Branch | Expected/actual match → PASSED; mismatch → FAILED | SOURCE_CODE_OBSERVED |
| Branch | Prior step latest PASSED → next step permitted; otherwise gate violation | SOURCE_CODE_OBSERVED |
| Branch | Final match → DELIVERED; mismatch → not delivered | SOURCE_CODE_OBSERVED |
| Bypass | Step 1 has no previous-step prerequisite | SOURCE_CODE_OBSERVED |
| Loop-back | Failed step → retained records → retry same step | SOURCE_CODE_OBSERVED |
| Restart | Checkpoint rows exist, but v0.6.5 checkpoint restore/resume endpoint not found | UNKNOWN / MISSING TRANSITION |
| Return | Main AI retrieval of external state is USER_CONFIRMED; actual host invocation trace absent | USER_CONFIRMED / REPOSITORY UNPROVEN |
| Handoff | Modular work sets and necessary handoff information are USER_CONFIRMED; actual packet/payload/transport not found | USER_CONFIRMED / REPOSITORY UNCONNECTED |
| Direct jump | No user-system-wide direct-jump rule established | UNKNOWN |
| Parallel path | No higher-level concurrent work coordination contract established | UNKNOWN |

### Separate user-supplied discovery/data sequence

The source records:
Raw Collection → Review → Understanding → Mapping → Roadmap → Atomization

It also records that stage-specific entry conditions, exit conditions, artifact schemas, responsible actors, and transitions remain UNKNOWN / MISSING TRANSITION. The inspected IRIS v0.6.5 controller does not implement or connect this sequence.

## Existing Unknown / Unconnected Register

Source: `04_Discovery/system-translation-unknown-conflict-register.md`
Source Record ID: SYS-UNK-001
Source Status: DISCOVERY / NOT CANONICAL
Source Blob SHA: `b76edf132cf7478de69dec37894de01a2f6a15cb`

| ID | Item | Existing Finding | Status |
|---|---|---|---|
| UNK-001 | Main AI → actual IRIS host invocation | Skill and MCP configuration exist; no actual host invocation trace read | UNKNOWN |
| UNK-002 | Raw Database physical target | User confirms durable Raw Database; repository and v0.6.5 SQLite are not proven to be the same store | UNKNOWN |
| UNK-003 | Temporary Workspace implementation | User confirms per-cycle workspace; no concrete runtime location/cleanup trace found | UNKNOWN |
| UNK-004 | Handoff packet schema | Handoffs folder contains only .gitkeep; no actual packet payload read | UNCONNECTED |
| UNK-005 | Room/workspace transfer authority | Modular work-set separation is user-confirmed; recipient identity, transport, and authority contract not found | UNKNOWN |
| UNK-006 | Resume from original v0.6.5 checkpoint | Checkpoint storage exists; restore/resume API not found in inspected v0.6.5 source | MISSING TRANSITION |
| UNK-007 | IRIS Storage Lifecycle ↔ v0.6.5 five-step controller | Both evidenced at different scopes; exact mapping not established | UNCONNECTED |
| UNK-008 | IRIS Workflow Lifecycle complete transition inventory | User confirms component; only bounded controller sub-lifecycle is source-observed | INCOMPLETE |
| UNK-009 | IRIS First Adapter ↔ package MCP/REST adapter | Similar terms do not establish identity | UNRESOLVED |
| UNK-010 | SMPE Schema/Gate ↔ controller calls | SMPE responsibility is user-confirmed; concrete schema-to-call mapping absent | UNCONNECTED |
| UNK-011 | AICC evidence ↔ work_id/step | AICC evidence responsibility is user-confirmed; v0.6.5 evidence table has no demonstrated work/step linkage | UNCONNECTED |
| UNK-012 | Raw Collection → Review → Understanding → Mapping → Roadmap → Atomization | Sequence is user-supplied; stage contracts, artifact schemas, and transition conditions absent in inspected controller source | MISSING TRANSITION |
| UNK-013 | Post-delivery continuation | No continuation after DELIVERED found in inspected v0.6.5 controller | UNKNOWN |
| UNK-014 | Parallel work / concurrent actors | No higher-level coordination contract found | UNKNOWN |
| UNK-015 | Separate Step 1 package / project-level controller | Not found in inspected target branch trees and inspected source tree; bounded search only | UNKNOWN |
| UNK-016 | Output consumer and destination | Verified output is user-confirmed; consumer/location not mapped | UNKNOWN |
| UNK-017 | External approval/independent verification identity registry | Human approval and independent verification rules are user-confirmed; concrete identity/authority store not found | UNKNOWN |
| UNK-018 | HAP policy enforcement location | Policy labels are user-confirmed and repository policy docs exist; runtime enforcement point per action not fully mapped | PARTIALLY MAPPED |

## Existing Conflict Records

The source conflict register contains seven records:
- CONFLICT-001: IRIS system scope vs controller package scope.
- CONFLICT-002: REST/MCP final mismatch behavior.
- CONFLICT-003: Checkpoint 007 unconnected segment count.
- CONFLICT-004: Current state run reference.
- CONFLICT-005: Current knowledge classification.
- CONFLICT-006: Repository-side iris_runtime vs reality-first instruction.
- CONFLICT-007: Checkpoint 008 parent commit vs current branch head.

The source document preserves each conflict as unresolved or historical; no conflict was resolved or normalized in this task.

## Relationship Discovery Boundaries

- User-confirmed relationships remain labeled USER_CONFIRMED; they are not presented as runtime-proven.
- Source-code observations remain bounded to the named IRIS Controller v0.6.5 package.
- Repository-observed relationships remain bounded to repository artifacts.
- "Unconnected" means not established by the inspected source, not that the component does not exist.
- No relationship is inferred between Raw Database and SQLite, between IRIS Adapter and SMPE Adapter, or between the HAP/AICC MCP API and the IRIS MCP host binding.
- No new edge, node, component, state, authority, or transition was created.

## Task Closure
- TASK-009: COMPLETE
- Snapshot: PERSISTED
- Read-back: PENDING
- TASK-010: NOT STARTED
- WORKSPACE: EMPTY
