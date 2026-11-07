# System Translation Index

- Record ID: SYS-TR-INDEX-001
- Classification: USER-CONFIRMED + SOURCE-OBSERVED / DISCOVERY / NOT CANONICAL
- Repository: 0816155422/project-workflow-manual
- Working branch: reconstruction/operating-work-lifecycle-state
- Baseline checkpoint: CKPT-20261108-008
- Baseline branch HEAD observed: 502d8c78411b179f2e39195b5231d8921c249aba
- Main HEAD observed: 48e9f64bebd7fb3821d6d03377d3713c46e51193
- Purpose: represent already-existing human operating knowledge and source-observed operations in repository-readable records. This is not a new architecture, workflow, lifecycle, state machine, or canonical knowledge base.

## Governing rule

Reality is the source. This repository contains a partial representation of it. Names of modules, folders, APIs, or code are not sufficient evidence of an operating relationship. Every relationship in these records is classified by provenance. Missing links remain UNKNOWN, UNCONNECTED, UNRESOLVED, or MISSING TRANSITION.

## Record set

- SYS-OPS-001: system-translation-operating-structure.md
- SYS-LIFE-001: system-translation-work-lifecycle.md
- SYS-NET-001: system-translation-state-network.md
- SYS-TOOLS-001: system-translation-tool-classification.md
- SYS-REL-001: system-translation-system-relationships.md
- SYS-UNK-001: system-translation-unknown-conflict-register.md
- SYS-SRC-001: system-translation-source-register.json
- SYS-TRACE-001: ../08_ID_Traceability/system-translation-traceability.json

## Provenance classes

- USER_CONFIRMED: explicitly stated by the user in prior/current working context.
- REPOSITORY_OBSERVED: read directly from a repository file, commit, branch, checkpoint, or log.
- SOURCE_CODE_OBSERVED: read directly from the IRIS v0.6.5 source repository.
- INFERRED: not used to establish a relationship in this record set.
- UNKNOWN: not available from inspected sources.
- CONFLICT: two existing records or sources differ; both are retained.

## Coverage boundary

The target repository currently contains HAP/AICC files, generic repository/process documentation, IRIS reconstruction and implementation artifacts, checkpoint/log/state records, and placeholder folders for handoffs and other work areas. The inspected target-repository branch set and inspected Prasong1993/Prasong source tree did not expose dedicated SMPE artifacts or actual room/handoff packets. User-confirmed SMPE and cross-system details are therefore represented with explicit conversation provenance, not falsely attributed to repository files.

## Authority boundary

All records in this set are Discovery representations. They do not modify Canonical Knowledge, change runtime behavior, authorize database writes, authorize remote mutation, or establish that a host is connected. Existing generated iris_runtime files remain implementation artifacts on the working branch and are not treated as proof of the complete human operating system.
