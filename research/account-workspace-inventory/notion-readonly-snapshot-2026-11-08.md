# Notion Read-only Verified Snapshot — 2026-11-08

## Scope
This snapshot retains only facts directly observed through the currently connected Notion integration. Unverified account references and workspace mappings have been excluded from this active snapshot.

All Notion operations described here were read-only. No external Notion data or settings were changed.

## Connected identity and workspace

Two connector links were checked independently. Both returned the same identity and workspace:

| Field | Observed value |
|---|---|
| User display name | prasong seelaprasong |
| Connected email | `prasong5843@gmail.com` |
| User ID | `3f0d872b-594c-811f-8d5e-000267b384d9` |
| Workspace name | prasong seelaprasong’s Space |
| Workspace ID | `320089a7-5dad-81c4-b5e0-00039875cd52` |

The two connector links are duplicate access paths to the same observed identity and workspace.

## Listing results

| Listing surface | Results |
|---|---:|
| Private sidebar | 7 entries |
| Shared sidebar | 4 entries |
| Teamspaces | 0 returned |
| Recently viewed | Several dozen entries |

The private/shared entries and the surfaced recent-page records were used to discover pages and databases. Recent-page results are not a complete export of all content.

## Database content read

| Database | Rows returned | Findings |
|---|---:|---|
| IRIS Workstream Status Register | 13 | WS00–WS12; all 13 show `In progress` |
| To Do List DB | 6 | 1 Done; 5 not Done |
| Memories database (first surfaced record) | 0 | Empty result |
| Memories database (second surfaced record) | 0 | Empty result |

The connected Notion Memory endpoint returned: no memories have been saved yet.

The IRIS workstream register includes fields for workstream name/ID, status, acceptance criteria, dependencies, evidence, blockers, checkpoint, next action, and workstream page URL. This snapshot records the returned database status only; it does not independently validate the workstream claims.

## Coverage and limitations

- Only one distinct Notion identity and one workspace were returned by the two available connector links.
- The available connector tools do not expose a complete account-level workspace enumeration operation.
- Private/shared sidebar and recently viewed listings do not prove global completeness across all pages, nested blocks, archived content, or other workspaces.
- No conclusions are made about unconnected accounts or workspaces.
- Details without independent confirmation were excluded from this active verified snapshot.

## Final status
`VERIFIED_PARTIAL_INVENTORY`

Verified observations are recorded. Full account-wide and all-workspace coverage is not claimed.

External Notion mutations: NONE.
