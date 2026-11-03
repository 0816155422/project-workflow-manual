# ID Contract

## Purpose

Provide stable identity and traceability across the project and its work.

## ID coverage

The Registry supports distinct IDs for:

1. Project
2. Workflow Cycle
3. Work Item
4. Artifact
5. Atom / Data Unit

Each entity receives its own identity. Relationships between entities are stored as explicit references. Do not reuse a Project ID as a Cycle ID, a Work Item ID, an Artifact ID, or an Atom ID.

## Identity rules

1. Every registered entity has one unique, immutable ID.
2. An issued ID must not be renamed, reassigned, recycled, or silently replaced.
3. Existing IDs are preserved. Map them to their source entities before considering a new ID.
4. Do not invent a prefix, namespace, sequence rule, or ID format. Use the already-defined convention for the relevant entity type.
5. IDs may be associated in pairs or other explicit relationships. Relationships are recorded as links and do not constrain the number of relationships.
6. Atom/Data Unit identity is immutable even when its content version or Group membership changes.
7. Each Atom/Data Unit record includes a content hash, version, and read-back reference.
8. Content changes are represented by a new version under the same Atom identity unless the source represents a genuinely different Atom.
9. Group membership and Category/Group arrangements may change without changing the Atom ID.
10. The Registry is the authority for whether an ID exists and which source entity it identifies.

## Known Atom example

`ATM-img-001` is an example previously supplied for an Atom. It is illustrative and is not issued by this file.

## Registry fields

Every record includes:

- `id`: immutable ID.
- `entity_type`: Project, WorkflowCycle, WorkItem, Artifact, or Atom.
- `source_ref`: source location or source identifier.
- `relationships`: explicit links to related registered IDs.

Atom/Data Unit records additionally require:

- `content_hash`: SHA-256 of the registered content.
- `version`: version of the registered content.
- `readback_ref`: location/reference used to read the registered content back.
- `group_memberships`: current mutable Category/Group references.

For non-content identity records, fields that do not apply must remain null or be omitted; do not fabricate hashes or versions.

Do not issue an ID if the source identity or the applicable naming convention is unavailable. Do not fabricate source references, hashes, timestamps, or version values.
