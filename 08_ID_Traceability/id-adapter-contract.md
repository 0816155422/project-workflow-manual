# ID Adapter Contract

## Purpose

The ID Adapter connects the ID Contract and Registry to the target work domain. It adapts the same identity rules to different target contexts without changing an issued identity.

## Required behavior

The Adapter performs:

1. Scan the supplied source/work material.
2. Identify Project, Workflow Cycle, Work Item, Artifact, and Atom/Data Unit entities where present.
3. Decompose source material into Atom/Data Units.
4. Classify the resulting Atoms.
5. Group Atoms according to the target work context.
6. Map existing IDs to the resulting entities and preserve valid identities.
7. Refer to the Registry when an ID must be issued.
8. Maintain explicit links between projects, cycles, work items, artifacts, Atoms, Categories, and Groups.

The target context may vary by work domain, such as Network, Database, or Developer work. Target-specific configuration may change scan/decomposition/classification/grouping behavior, but must not mutate an issued ID.

## Adapter definition fields

Every Adapter configuration must state all four fields:

- `Design`: the structure or target-specific configuration.
- `Command`: the operation the Adapter is asked to perform.
- `Purpose`: why the operation is being performed.
- `Method`: how the operation is carried out.

## Boundaries

- The Adapter does not invent a new ID format or silently replace IDs.
- The Adapter does not make mutable Group identity a substitute for Atom identity.
- The Adapter does not close work merely because it has produced files.
- An ID mapping conflict remains unresolved until the existing identity can be mapped to its source entity.
