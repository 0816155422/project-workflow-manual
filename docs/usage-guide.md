# Usage Guide

## How to use this repository

This repository is divided into separate layers to keep AI automation, human operations, and data approval distinct.

## Layer 1: Machine control layer
Use this layer for AI and automation.

Files:
- state/session-state.json
- state/phase-status.json
- state/last-run.json
- state/checkpoints/latest.json
- logs/operation-log.md
- logs/workflow-evidence.md

Rules:
- read state before every task
- keep checkpoints append-only
- do not overwrite prior state silently
- do not claim success without evidence
- do not fabricate approval or records

## Layer 2: Human coordination layer
Use this layer for people.

Files:
- README.md
- docs/task-registry.md
- docs/project-status.md
- docs/usage-guide.md

Human tasks:
- assign owner
- review status
- approve official records
- coordinate blockers
- review execution evidence

## Layer 3: Data and approval layer
Use this layer for actual data and approval.

Files:
- pending/course/course-source.json
- approvals/
- data/raw/
- data/approved/

Rules:
- real data only
- required provenance
- explicit approval
- no fake records
- no sync without approval and validation

## Layer 4: Frontend layer
Use this layer only for presentation.

Files:
- hap-aicc/index.html
- hap-aicc/app.js
- hap-aicc/styles.css

This layer must not be used as the source of truth for state or data.

## Operational behavior

The safe order is:
1. read state
2. read task registry
3. identify blocker
4. gather real source data
5. validate
6. record approval
7. run sync
8. verify outputs

## Important

This project is intentionally strict:
- data must be real
- approval must be explicit
- AI must use evidence
- humans must review before promotion
