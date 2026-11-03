# ID Traceability and Work Closure

This area implements the existing ID and closure model for the Project Workflow Manual. It does not add a new workflow stage or an Audit stage.

## Components

- `id-contract.md`: immutable identity rules for Atom/Data Units.
- `id-adapter-contract.md`: target-aware scan, decomposition, classification, and grouping behavior.
- `closure-contract.md`: rules for closing a work item or returning it to its point of failure.
- `id-registry.json`: authoritative registry for issued IDs.
- `closure-ledger.json`: work closure records linked to issued IDs.

## Operating model

1. Decompose source material into Atom/Data Units.
2. Assign each Atom/Data Unit an ID through the Registry. An ID is never silently replaced or recycled.
3. Record the content hash and version, then perform read-back against the registered identity.
4. Organize Atoms into Categories and Groups. Group membership may change; Atom identity does not.
5. Link work, outputs, and closure records to their IDs.
6. Close only the relevant work item when its defined completion conditions are met. A failed item returns to its originating work form; a failure at origin returns to the first part of that work cycle.

## Important boundaries

- This is the ID and closure implementation area, not a new storage system.
- The Registry is the authority for issued IDs; examples are not issued IDs.
- No real project/work IDs are pre-populated here. Existing IDs must be preserved and mapped, not recreated.
- A Group is a mutable arrangement of Atoms, not a replacement identity for its Atoms.
- Closing one work item or cycle does not automatically close its parent project.
- No additional Audit stage is introduced.
