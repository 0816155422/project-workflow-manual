# Operating Structure + Work Lifecycle Reconstruction State

- Record ID: `operating-work-lifecycle-reconstruction-state`
- Status: `USER-CONFIRMED`
- Knowledge Stage: `RECONSTRUCTION / DISCOVERY`
- Canonical Status: `NOT CANONICAL`
- Verification Status: `NOT REQUIRED FOR CURRENT RECONSTRUCTION STAGE`
- Runtime Evidence Status: `NOT REQUIRED FOR CURRENT RECONSTRUCTION STAGE`
- Provenance: `USER-CONFIRMED Reconstruction Session`
- Recorded: `2026-11-08`
- Parent Repository: `0816155422/project-workflow-manual`
- Parent Branch: `main`
- Parent Commit: `48e9f64bebd7fb3821d6d03377d3713c46e51193`
- Parent State References:
  - `state/session-state.json` blob `564a9311a537ff11e05f4fb72ad3e1dbfc2cdefa`
  - `state/phase-status.json` blob `824d14e5f5e25f08dbacb016d6f2437572d96952`
  - `state/last-run.json` blob `b4737c986caf09c7c756cf94829a52f6ac8900eb`
  - `state/checkpoints/latest.json` blob `25192b62da3de684858c2f2585bb2164ea264bd0`
  - Previous immutable checkpoint `state/checkpoints/CKPT-20261028-005.json` blob `c35c1a8bc0f8a1bea6c3f50c689b0ef4df156b28`

## 1. Current Reconstruction Objective

The current objective is reconstruction of:

`Operating Structure + Work Lifecycle`

The current objective is not reconstruction of Code Structure or Data Structure. Code, Database, API, UI, Adapter, and other elements are not to be used to force or prescribe the lifecycle at this stage.

## 2. Fundamental Working Relation

The user-confirmed fundamental working relation is:

`State → Action → State`

This is the fundamental relationship for the current reconstruction. This statement does not require creating a new State Machine implementation.

## 3. State Semantics

State does not have a fixed meaning as a beginning point or an ending point. State means the current position or condition of work within a cycle. A State can relate to Actions and other States according to the work context.

Do not force a linear `Start → Process → End` structure unless actual information defines it.

## 4. IRIS Controller Role

IRIS Controller controls the work lifecycle. In this context its important role is:

`Call the relevant State → allow work to proceed from that State → change through Action → obtain a State related to the work result`

This reconstruction statement does not define IRIS Controller as a data creator, universal analyzer, Database, Worker AI, or an entity that determines reasons on behalf of the user.

## 5. Reconstruction Evidence Rule

During reconstruction, use information to discover and assemble:

- Operating Structure
- Work Lifecycle
- State
- Action
- Relationship
- Reference

Runtime Evidence is not required at every reconstruction step.

Do not add functions for AI to invent reasons to fill gaps, force evidence for every Node, enforce PASS/FAIL for every Node, or verify its own work to keep reconstruction moving.

If information is unknown or cannot yet be assembled, retain it as unknown/not yet assembled. Do not invent additional information.

## 6. Runtime Evidence Boundary

Evidence of actual runtime use is a separate concern from the current reconstruction.

Runtime Evidence becomes relevant when the reconstructed structure or lifecycle is returned to actual use and actual operation results need to be checked.

Reconstruction must not be blocked solely because Runtime Evidence is absent at every step.

This rule does not cancel Independent Verification that may apply in another Lifecycle.

## 7. Operating Structure + Work Lifecycle

Operating Structure and Work Lifecycle must be considered together. The current reconstruction must discover their relationships from actual information.

Do not design future components in advance.

The current working principle is:

`Assemble the current parts correctly → allow subsequent relationships to emerge from the operation of the structure itself`

Do not create a new Module or Function merely because it is expected that it may be needed later.

## 8. Network Behaviour

The structure is not restricted to a linear path. Network relationships may branch, cross Nodes, return backward, reconnect to an origin, and connect State to State through Action according to context.

Do not force every path to share one Start/End pattern.

## 9. Retrieval Foundation

An important capability for the main AI of each provider is the ability to retrieve related information.

The minimum conceptual form is:

`ID → Reference → Relationship → Source Location`

The goal is for AI to follow References and Relationships back to source information. AI does not need to keep all Payload in Conversational Context at all times.

## 10. Raw Database

Raw Database stores raw information in the condition in which it is received during Intake.

Do not Atomize all information immediately at Intake merely because the system supports Atom.

Mapping, Roadmap, and Atomization occur later, after information has been collected and reviewed for the relevant work.

## 11. Internal Gate Boundary

The Internal Gate within the `IRIS ↔ Raw Database` cycle has the specific boundary of checking defined conditions.

Internal Gate must not create Payload, modify Payload, analyze Payload to create new content, create new Requirements, or arbitrarily change Relationships.

Gate checks the Boundary/Condition of the cycle as defined.

## 12. Main AI and IRIS Boundary

Main AI maintains the Conversational Context necessary for the conversation.

IRIS uses External Memory / Raw Database and related reference mechanisms.

From the Main AI perspective, IRIS can be invoked as an Extension/Tool to access State and external information required by the cycle.

Do not interpret this to mean all information must be loaded into Main AI Context.

## 13. Cross-AI Tool Principle

Tools built from this structure must not be designed around the shortcomings or provider-specific behaviours of any one AI unless necessary.

The goal is for fundamental rules and structures to be usable by multiple AI providers.

AI acts as an operator or tool user according to relevant State/Action. AI is not the owner of the Operating Structure.

## 14. Uncertainty and Conflict Handling

Unknown information remains unknown/not yet assembled. Do not resolve conflicts by choosing one statement and overwriting another.

If a conflict is discovered, create a separate Conflict/Revision Record containing at least:
- Existing Statement Reference
- New USER-CONFIRMED Statement
- Conflict Description
- Existing State Reference
- New Reconstruction State Reference
- Status: `UNRESOLVED`

No conflict is declared resolved by this record.

## 15. Resume Instructions

Current Reconstruction Focus: `Operating Structure + Work Lifecycle`

Current Fundamental Relation: `State → Action → State`

Current Rule: `Do not design the next structure in advance. Continue reconstruction from the current State and observed relationships.`

Current Knowledge Status: `USER-CONFIRMED / RECONSTRUCTION / NOT CANONICAL`

Resume from this record and its linked Parent State. Do not promote this record to Canonical, infer a next State, or treat this record as runtime/evidence verification.

## 16. State Linkage

- Parent State: `state/session-state.json` at Parent Commit above.
- Previous Checkpoint: `state/checkpoints/CKPT-20261028-005.json`.
- Current Reconstruction Record: `04_Discovery/operating-work-lifecycle-reconstruction-state.md`.
- New Checkpoint: to be linked by the immutable checkpoint and current pointer created after this record is persisted.
