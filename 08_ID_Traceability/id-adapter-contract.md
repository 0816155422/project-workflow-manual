# ID Adapter Contract

## Purpose

The ID Adapter connects the ID Contract and Registry to the target work domain. It adapts the same identity rules to different target contexts without changing the identity of an Atom.

## Required behavior

The Adapter performs:

1. Scan the supplied source/work material.
2. Decompose it into Atom/Data Units.
3. Classify the resulting Atoms.
4. Group Atoms according to the target work context.
5. Map existing IDs to the resulting Atoms and preserve valid identities.
6. Refer to the Registry when an ID must be issued.
7. Maintain links between Atoms, Categories, Groups, work items, and outputs.

The target context may vary by work domain, such as Network, Database, or Developer work. Target-specific configuration may change the scan/decomposition/classification/grouping behavior, but must not mutate an issued Atom ID.

## Adapter definition fields

Every Adapter configuration must state all four fields:

- `Design`: the structure or target-specific configuration.
- `Command`: the operation the Adapter is asked to perform.
- `Purpose`: why the operation is being performed.
- `Method`: how the operation is carried out.

## Boundaries

- The Adapter does not independently invent or silently replace IDs.
- The Adapter does not make mutable Group identity a substitute for Atom identity.
- The Adapter does not close work merely because it has produced files.
- An ID mapping conflict is retained as unresolved until the existing identity can be mapped correctly.
