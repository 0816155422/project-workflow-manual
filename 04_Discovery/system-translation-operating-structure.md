# System Translation: Operating Structure

- Record ID: SYS-OPS-001
- Classification: USER-CONFIRMED / REPOSITORY-OBSERVED
- Status: DISCOVERY / NOT CANONICAL
- Parent: SYS-TR-INDEX-001
- Source register: SYS-SRC-001

## 1. Operating system already present in reality

The system is treated as an existing human operating system. This record identifies responsibilities and relationships explicitly present in user-confirmed context or repository/source evidence. It does not define a replacement architecture.

### IRIS

USER_CONFIRMED:
- IRIS is the user-facing control and coordination point.
- IRIS has three inseparable components: Storage Lifecycle, IRIS Workflow Lifecycle, and the first Adapter / IRIS Adapter.
- Storage Lifecycle is the existing first three of ten parts and must not be modified, replaced, or dismantled.
- IRIS coordinates work; it is not the project database and is not SMPE.
- The Main AI can invoke IRIS as an extension/tool to retrieve state and external information needed by the current cycle.
- The Main AI retains conversational context; IRIS uses external memory / Raw Database and reference mechanisms.

REPOSITORY_OBSERVED:
- A distinct IRIS Controller v0.6.5 package exists in Prasong1993/Prasong.
- That package exposes a five-step work-unit controller through REST and MCP interfaces.
- The package is a specific controller implementation. It is not, by itself, evidence that it represents all three user-confirmed IRIS components.

### HAP

USER_CONFIRMED:
- HAP provides the operating environment and policy constraints.
- HAP principles include offline-first operation, approval-gated actions, ZERO_DATABASE_WRITE, prohibition of unauthorized remote mutation, and human approval requirements.
- Existing project policy labels include HAP-2026-OFFLINE-FIRST, PHASE_0_BLOCKED, PHASE_1_NOT_AUTHORIZED, DATABASE_WRITE_POLICY: ZERO_DATABASE_WRITE, REMOTE_MUTATION_POLICY: PROHIBITED, HUMAN_APPROVAL_REQUIRED: TRUE, and SPECIFICATION_STATUS: NOT_APPROVED_FOR_FREEZE.

REPOSITORY_OBSERVED:
- HAP/AICC dashboard files exist under hap-aicc/.
- Repository policy and approval documents define manual review, explicit approval, no overwrite, protected secrets, and evidence-based claims.
- api/mcp.js documents repository read/write tools and audit behavior; deployment/host use is not established by file presence alone.

### AICC

USER_CONFIRMED:
- AICC is responsible for data, evidence, and records in the combined operating context.

REPOSITORY_OBSERVED:
- Existing AICC/HAP artifacts include the dashboard, data manifest, usage log, MCP API, MCP audit log, schemas, approval records/templates, workflow logs, and data-validation/sync scripts.
- The dashboard manifest states that the approved course dataset has not been written and that approval is required.
- pending/course/course-source.json has an empty records array and no approval markers in the inspected branch state.

### SMPE

USER_CONFIRMED:
- SMPE is the Schema-Managed Process Engine.
- The Central Repository is a single central read-only source.
- Schema provides multi-layer rules controlling the process.
- Adapter is a fixed, versioned master template stored in the Central Repository.
- Artifact is a flexible schema-built extension.
- Independent Verification must be performed by another person/system; self-verification is prohibited.
- IDs provide traceability across objects.
- SMPE governs schema/process/validation and gates; it is not IRIS.

REPOSITORY_OBSERVED:
- No dedicated SMPE-named file or package was found in the inspected target repository branch trees or the inspected Prasong1993/Prasong main tree. This is a bounded search result, not proof that no SMPE material exists elsewhere.

### Main AI / operator

USER_CONFIRMED:
- Main AI maintains the conversational context necessary for the current conversation.
- AI operates as an operator/tool user according to the applicable state/action; it does not own the Operating Structure.
- Conversational context, chat, and AI memory are not permanent project storage.

REPOSITORY_OBSERVED:
- The IRIS Agent Skill documents intended MCP tool use.
- A live Main AI host invocation trace has not been found in the inspected records.

### Data locations and working areas

USER_CONFIRMED:
- Raw Database is durable project state.
- Temporary Workspace contains per-cycle working data.
- AI context/chat is not permanent storage.
- The user-confirmed cycle includes retrieval into a workspace, execution, gate/verification, authorized persistence, checkpoint/resume update, workspace cleanup, and verified output.

REPOSITORY_OBSERVED:
- The repository is versioned file storage and coordination source for committed artifacts; its policy states that it is not a real-time database.
- The repository contains private/ and operational handoff placeholders, not proof of a secure external Raw Database or a live Temporary Workspace.

## 2. Responsibility separation

| Existing responsibility | Responsible element | Evidence class | Boundary |
|---|---|---|---|
| User-facing coordination and state retrieval | IRIS | USER_CONFIRMED | Not the project database or SMPE |
| Existing storage lifecycle | IRIS Storage Lifecycle | USER_CONFIRMED | First three of ten parts; preserve unchanged |
| Work coordination and execution lifecycle | IRIS Workflow Lifecycle | USER_CONFIRMED | Exact complete transition inventory remains under extraction |
| First adapter | IRIS Adapter | USER_CONFIRMED | Do not conflate with SMPE Adapter |
| Environment and operating policy | HAP | USER_CONFIRMED | Includes offline-first and approval/write constraints |
| Data, evidence, and records | AICC | USER_CONFIRMED | Actual source-of-record locations need exact mapping |
| Schema/process/validation/gates | SMPE | USER_CONFIRMED | No dedicated repository representation found |
| Conversational context and tool operation | Main AI | USER_CONFIRMED | Not durable storage and not owner of the system |
| Durable project state | Raw Database | USER_CONFIRMED | Exact physical implementation/location unresolved |
| Per-cycle working data | Temporary Workspace | USER_CONFIRMED | Exact implementation/location unresolved |

## 3. Explicit non-equivalences

- IRIS as a user-confirmed three-part system is not interchangeable with the IRIS Controller v0.6.5 five-step package.
- IRIS Adapter and SMPE Adapter are separate named concepts; no equivalence is asserted.
- Raw Database, SQLite in a controller package, and GitHub repository storage are not assumed to be the same store.
- A repository MCP endpoint or .mcp.json is not proof of a connected Main AI host.
- A folder placeholder is not proof that a handoff, room packet, register, or external storage service exists.
