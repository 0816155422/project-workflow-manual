# System Translation: Tool Classification

- Record ID: SYS-TOOLS-001
- Classification: DISCOVERY / NOT CANONICAL
- Parent: SYS-TR-INDEX-001

## Classification rule

An object is classified as an Operating Structure element, Lifecycle activity, or Supporting Tool only where its role is evidenced. A tool does not become a lifecycle state or operating actor merely because it has a folder, API, or database table.

## 1. Operating Structure elements

| Element | Observed / user-confirmed role | Classification | Boundary |
|---|---|---|---|
| IRIS | User-facing control/coordination; Storage Lifecycle, Workflow Lifecycle, First Adapter | OPERATING STRUCTURE | Three components are inseparable; preserve Storage Lifecycle |
| HAP | Environment and policy constraints | OPERATING STRUCTURE / GOVERNANCE CONTEXT | Offline-first, approval/write boundaries |
| AICC | Data, evidence, and records responsibility | OPERATING STRUCTURE / RECORDS CONTEXT | Exact mapping of every record class remains incomplete |
| SMPE | Schema/process/validation/gates and independent verification | OPERATING STRUCTURE / PROCESS CONTROL | Not IRIS; no dedicated repo package found |
| Main AI | Conversation context and operator/tool user | OPERATING ACTOR | Not owner and not permanent storage |
| Raw Database | Durable project state | STORAGE ELEMENT | Physical authoritative location unresolved |
| Temporary Workspace | Per-cycle working data | WORKING AREA | Concrete runtime implementation unresolved |
| Human approver / independent verifier | Human approval and separate verification authority where required | AUTHORITY / CONTROL ROLE | Exact actor identity and authorization registry unresolved |

## 2. Lifecycle activities

These are activities in the user-confirmed cycle, not new modules:
- Retrieve required data.
- Place/use data in Temporary Workspace.
- Main AI / MCP execution.
- Produce a result.
- Apply gate / verification.
- Perform authorized persistence.
- Update checkpoint / resume position.
- Clean Temporary Workspace.
- Produce verified output.

The separate v0.6.5 controller sub-lifecycle includes create work, gate step, execute, compare, retain failure, retry, final verification, delivery, and retrieval. It remains a controller-specific source-observed sub-lifecycle.

## 3. Supporting tools and records

| Object | Classification | Observed role | Not evidence of |
|---|---|---|---|
| IRIS Controller v0.6.5 package | SUPPORTING IMPLEMENTATION | Specific controller runtime for five-step work units | Whole human IRIS system |
| iris_runtime/ in target branch | WORKING-BRANCH IMPLEMENTATION ARTIFACT | Later repository-side code for SQLite lifecycle, resume, handoff, MCP | Existing reality or canonical operating structure |
| MCP server | SUPPORTING INTERFACE | Exposes functions/tools to a host | Actual host connection |
| REST API | SUPPORTING INTERFACE | Exposes HTTP endpoints | Main AI invocation |
| IRIS Adapter | USER-CONFIRMED IRIS COMPONENT | First adapter within IRIS | Same as SMPE Adapter |
| SMPE Adapter | USER-CONFIRMED SMPE TEMPLATE | Fixed/versioned master template in Central Repository | Same as IRIS Adapter |
| SQLite database | SUPPORTING STORAGE IMPLEMENTATION | Persists controller work/run/error/checkpoint/audit data | Raw Database identity |
| Checkpoint record | SUPPORTING STATE RECORD | Captures a position/snapshot | A resume operation by itself |
| Resume operation | LIFECYCLE ACTION / SUPPORTING CAPABILITY | Returns work to a recorded position when actual rules permit | Proven in original v0.6.5 runtime |
| Handoff / Room Packet | SUPPORTING TRANSFER ARTIFACT | Carries only required information between modular work sets, as user described | A concrete packet schema; none found in repo |
| Registry / ID system | SUPPORTING TRACEABILITY MECHANISM | IDs connect objects to references and sources | Proof of a complete registry implementation |
| Database layer | SUPPORTING STORAGE TOOL | Persists data | Operating actor |
| UI / Dashboard | SUPPORTING PRESENTATION | Shows status/data | Source of truth or write authority |
| API / MCP | SUPPORTING ACCESS INTERFACE | Exposes operations | Lifecycle itself |
| GitHub Actions | SUPPORTING AUTOMATION | Executes repository workflows when dispatched | Domain success unless relevant output is verified |
| GitHub repository | REPOSITORY REPRESENTATION / VERSIONED STORAGE | Stores files, commits, logs, and checkpoints | Real-time database or automatic shared memory |

## 4. Similar names kept separate

- IRIS Workflow Lifecycle is not the same as the v0.6.5 five-step package contract unless a source mapping proves equivalence.
- IRIS Adapter is not the SMPE Adapter.
- Raw Database is not assumed to be the SQLite database used by v0.6.5.
- Checkpoint storage is not equivalent to checkpoint restore/resume.
- MCP tool definition is not equivalent to a connected host.
