# System Translation: System Relationships

- Record ID: SYS-REL-001
- Classification: USER-CONFIRMED + REPOSITORY-OBSERVED
- Status: DISCOVERY / NOT CANONICAL
- Parent: SYS-TR-INDEX-001

## Relationship register

| Relationship ID | From | Relation | To | Provenance | Boundary |
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

## Relationship limits

- A relationship can be user-confirmed without a complete repository implementation.
- A repository file can document an intended relationship without proving that it runs.
- A source-code call can prove a package-local relationship without proving that it belongs to the whole human operating system.
- No relation is inferred between Raw Database and SQLite, between the user-confirmed IRIS Adapter and SMPE Adapter, or between the HAP/AICC MCP API and the IRIS MCP host binding.
