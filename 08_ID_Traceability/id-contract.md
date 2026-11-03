# ID Contract

## Purpose

Provide stable identity and traceability for every Atom/Data Unit used by the project workflow.

## Identity rules

1. Every Atom/Data Unit receives one unique, immutable ID from the ID Registry.
2. An issued Atom ID must not be renamed, reassigned, recycled, or replaced when its content or grouping changes.
3. Each registered Atom/Data Unit records a content hash, version, and a read-back reference.
4. Content changes are represented by a new version under the same Atom identity unless the source represents a genuinely different Atom. The identity itself remains unchanged.
5. Group membership and Category/Group arrangements may change without changing the Atom ID.
6. Existing IDs are preserved. Mapping must happen before any proposed replacement; unmatched IDs remain unresolved rather than being guessed.
7. IDs may be associated in pairs or other explicit relationships. Relationships are recorded as links and do not constrain the number of relationships.
8. The Registry is the authority for whether an ID has been issued.

## Known example

`ATM-img-001` is an example previously supplied for an Atom. It is illustrative and is not an issued record in this Registry.

## Required registry fields

Each issued record must include:

- `id`: immutable ID.
- `entity_type`: Atom or another explicitly defined registry entity type.
- `source_ref`: source location or source identifier.
- `content_hash`: SHA-256 of the registered content.
- `version`: version of the registered content.
- `created_at`: issuance timestamp.
- `readback_ref`: location/reference used to read the registered content back.
- `relationships`: explicit links to related IDs.
- `group_memberships`: current mutable Category/Group references.

Do not issue an ID if the required source identity is unavailable. Do not fabricate source references, hashes, timestamps, or version values.
