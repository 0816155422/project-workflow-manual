# System Translation: Unknown and Conflict Register

- Record ID: SYS-UNK-001
- Classification: DISCOVERY / NOT CANONICAL
- Parent: SYS-TR-INDEX-001
- Rule: preserve unknowns and conflicts; do not fill gaps to make a complete diagram.

## Unknown / unconnected register

| ID | Item | Current finding | Status |
|---|---|---|---|
| UNK-001 | Main AI → actual IRIS host invocation | Skill and MCP configuration exist; no actual host invocation trace read | UNKNOWN |
| UNK-002 | Raw Database physical target | User confirms durable Raw Database; repository and v0.6.5 SQLite are not proven to be that same store | UNKNOWN |
| UNK-003 | Temporary Workspace implementation | User confirms per-cycle workspace; no concrete runtime location/cleanup trace found | UNKNOWN |
| UNK-004 | Handoff packet schema | Handoffs folder contains only .gitkeep; no actual packet payload read | UNCONNECTED |
| UNK-005 | Room/workspace transfer authority | Modular work-set separation is user-confirmed; recipient identity, transport, and authority contract not found | UNKNOWN |
| UNK-006 | Resume from original v0.6.5 checkpoint | Checkpoint storage exists; restore/resume API was not found in inspected v0.6.5 source | MISSING TRANSITION |
| UNK-007 | IRIS Storage Lifecycle ↔ v0.6.5 five-step controller | Both are evidenced at different scopes; exact mapping not established | UNCONNECTED |
| UNK-008 | IRIS Workflow Lifecycle complete transition inventory | User confirms component; only bounded controller sub-lifecycle is source-observed | INCOMPLETE |
| UNK-009 | IRIS First Adapter ↔ package MCP/REST adapter | Same/similar terms do not establish identity | UNRESOLVED |
| UNK-010 | SMPE Schema/Gate ↔ controller calls | SMPE responsibility is user-confirmed; concrete schema-to-call mapping absent | UNCONNECTED |
| UNK-011 | AICC evidence ↔ work_id/step | AICC evidence responsibility is user-confirmed; v0.6.5 evidence table has no demonstrated work/step linkage | UNCONNECTED |
| UNK-012 | Raw Collection → Review → Understanding → Mapping → Roadmap → Atomization | Sequence is user-supplied; stage contracts, artifact schemas, and transition conditions are not present in inspected controller source | MISSING TRANSITION |
| UNK-013 | Post-delivery continuation | No continuation after DELIVERED found in inspected v0.6.5 controller | UNKNOWN |
| UNK-014 | Parallel work / concurrent actors | No higher-level coordination contract found | UNKNOWN |
| UNK-015 | Separate Step 1 package / project-level controller | Not found in inspected target branch trees and inspected source tree; bounded search only | UNKNOWN |
| UNK-016 | Output consumer and destination | Verified output is user-confirmed; consumer/location not mapped | UNKNOWN |
| UNK-017 | External approval/independent verification identity registry | Human approval and independent verification rules are user-confirmed; concrete identity/authority store not found | UNKNOWN |
| UNK-018 | HAP policy enforcement location | Policy labels are user-confirmed and repository policy docs exist; runtime enforcement point per action is not fully mapped | PARTIALLY MAPPED |

## Conflict register

### CONFLICT-001 — IRIS system scope vs controller package scope

- Existing statement A: User-confirmed IRIS consists of Storage Lifecycle, Workflow Lifecycle, and First Adapter; these are inseparable.
- Existing statement B: IRIS Controller v0.6.5 documents a five-step work-unit execution controller and a package-level Skill → Execution Boundary → Runtime → State → Verification → Delivery chain.
- Conflict description: The two descriptions have different scopes. No mapping proves that the five-step package is the full user-confirmed IRIS system or that the package's five steps equal the three IRIS components.
- Resolution: UNRESOLVED. Preserve both scopes.

### CONFLICT-002 — REST/MCP final mismatch behavior

- Existing contract/README statements claim equivalent mismatch persistence in REST and MCP.
- Direct source inspection shows REST final mismatch writes verification and audit, then returns HTTP 409; MCP additionally writes error and checkpoint.
- Resolution: UNRESOLVED source-document/source-code discrepancy. Do not rewrite source history.

### CONFLICT-003 — Checkpoint 007 unconnected segment count

- CKPT-20261108-007 records unconnectedSegments = 7.
- Its linked reconstruction record lists 8 unconnected bullet entries.
- Resolution: Historical discrepancy retained. Do not edit CKPT-007.

### CONFLICT-004 — Current state run reference

- session-state.json.lastRun references run 40625614203.
- last-run.json and CKPT-008 implementation evidence reference IRIS test run 42410383181.
- Resolution: session-state lastRun field is stale or represents a different workflow; exact intended meaning is not resolved. Preserve both references and do not silently replace the historical value.

### CONFLICT-005 — Current knowledge classification

- state/session-state.json identifies currentKnowledgeStatus as IMPLEMENTATION / WORKING BRANCH / NOT CANONICAL.
- state/checkpoints/latest.json identifies currentKnowledgeStatus as USER-CONFIRMED / RECONSTRUCTION / NOT CANONICAL.
- Resolution: current classification is ambiguous across state files. This translation record is explicitly DISCOVERY / NOT CANONICAL and does not normalize the existing files without a separate state reconciliation decision.

### CONFLICT-006 — Repository-side iris_runtime vs reality-first instruction

- The working branch contains iris_runtime code, tests, MCP configuration, and an implementation report created during the preceding implementation-completion task.
- The current user instruction states that the system already exists and the task is representation, not new system design or module creation.
- Resolution: classify iris_runtime as a repository-side implementation artifact only. Do not use it as proof of the human operating system, do not expand it in this translation task, and do not delete or rewrite it here.

### CONFLICT-007 — Checkpoint 008 parent commit vs current branch head

- CKPT-008 parentCommitSha is 6fd54ee02a6439edd2006accb05a7e9864764180.
- Current working branch HEAD observed during this extraction is 502d8c78411b179f2e39195b5231d8921c249aba.
- Resolution: branch has advanced since the checkpoint baseline; this is retained as an observed sequence, not treated as proof that CKPT-008 was rewritten.

## Source coverage limitations

- No actual room packet or handoff record was found in the target repository.
- No dedicated SMPE artifact was found in the inspected target repository branch trees or inspected source repository tree.
- HAP/AICC repository artifacts are present, but the user-confirmed HAP/AICC operating roles are sourced from prior user statements and are not all expressed in repository files.
- Prior conversation records are not available as full exportable repository source files in this task. Their user-confirmed content is marked as such, and exact source locations remain unavailable.
