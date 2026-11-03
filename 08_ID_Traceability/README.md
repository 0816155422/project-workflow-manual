# ID Traceability and Work Closure

This area implements the existing ID assignment and closure model for the Project Workflow Manual. It does not add a new workflow stage or an Audit stage.

## ID coverage

The Registry tracks distinct identities for:

- Projects
- Workflow Cycles
- Work Items
- Artifacts
- Atoms / Data Units

Each entity has its own stable ID. Relationships between entities are explicit links; one entity's ID is not substituted for another.

## Components

- `id-contract.md`: identity rules and registry requirements.
- `id-adapter-contract.md`: target-aware scan, decomposition, classification, grouping, and ID mapping.
- `closure-contract.md`: work-item, cycle, and project closure rules.
- `id-registry.json`: authoritative registry for existing and newly issued IDs.
- `closure-ledger.json`: closure records linked to registered IDs.

## Operating model

1. Identify the project, workflow cycle, work item, artifact, and Atom/Data Unit entities present in the actual work.
2. Preserve and map existing IDs before considering any new issuance.
3. Assign a new ID only through the Registry and the already-defined ID convention. Do not invent a prefix or naming format.
4. For each Atom/Data Unit, record its content hash and version and retain a read-back reference.
5. Organize Atoms into Categories and Groups. Group membership may change; Atom identity does not.
6. Link work, outputs, and closure records to their registered IDs.
7. Close the relevant work item or cycle only against its own defined completion conditions.

## Closure boundaries

- Work Item Closure, Workflow Cycle Closure, and Project Closure are separate levels.
- Cycle Complete does not mean Project Complete.
- A failure returns to the work form where it occurred. A failure at the origin returns to the first part of that work cycle.
- No additional Audit stage is introduced.

## Registry status

The existing Project ID `PWA-2026-10-28` is preserved from `docs/project-manifest.md`. Other IDs are not pre-populated unless an existing source record can be mapped to them. Empty registry entries are intentional; no IDs are fabricated.
