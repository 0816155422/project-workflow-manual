# Notion — Verified Source Register

## Scope
This register contains only facts directly returned by the currently connected Notion integration and read back from its accessible listing/fetch/query endpoints.

External Notion access was read-only. No Notion pages, databases, workspaces, settings, permissions, or account data were changed.

## Verified connected identity

| Field | Observed value |
|---|---|
| Notion user display name | prasong seelaprasong |
| Connected email | prasong5843@gmail.com |
| User ID | `3f0d872b-594c-811f-8d5e-000267b384d9` |
| Workspace display name | prasong seelaprasong’s Space |
| Workspace ID | `320089a7-5dad-81c4-b5e0-00039875cd52` |

Two available connector links returned the same user ID, email, workspace name, and workspace ID. They are treated as two links to one observed identity, not as two separate accounts.

## Verified accessible listing surfaces

Both connector links returned the same listing results:

| Surface | Returned entries |
|---|---:|
| Private sidebar | 7 |
| Shared sidebar | 4 |
| Teamspaces | 0 |
| Recently viewed | Several dozen; not a complete inventory |

The private and shared sidebar entries were fetched where exposed by the connector. Recently viewed entries were used as additional discovery paths, not as proof of complete account contents.

## Verified database reads

| Database | Rows returned | Observed status |
|---|---:|---|
| IRIS Workstream Status Register | 13 | WS00–WS12; all 13 rows show `In progress` |
| To Do List DB | 6 | 1 Done; 5 not Done |
| Memories database (first surfaced record) | 0 | No rows returned |
| Memories database (second surfaced record) | 0 | No rows returned |

The connected Notion Memory endpoint also returned that no memories had been saved.

## Coverage boundary

This register deliberately excludes account references, workspace mappings, and other details that have not been independently confirmed by the connected Notion source.

The currently available connector links resolve to one observed Notion identity and one observed workspace. The available tools do not provide an account-wide endpoint to enumerate every workspace. Therefore:

- The connected identity and workspace above are verified observations.
- The surfaced pages and database rows are verified only within the connector's returned scope.
- Completeness across all content or all workspaces is not established.
- No statement is made about any unconnected account or workspace.

## Current status
`VERIFIED_PARTIAL_INVENTORY`

Last inspected: 2026-11-08.
