# Notion Read-only Account Snapshot — 2026-11-08

## Scope and handling
- Mode: read-only inspection of Notion through the currently available connector links.
- No Notion page, database, workspace, permission, setting, or account was changed.
- No credentials or secrets were requested or collected.
- This record covers only resources surfaced by the currently linked Notion profile and the connector's listing/search capabilities. It does not claim global coverage of every Notion account or every workspace.

## Account / connection observations

Two connector links were individually tested with `notion_get_self`:

| Connector link | Returned user | Returned email | Returned workspace |
|---|---|---|---|
| `link_6ad3dedc8fd881919fd02970cc385d76` | prasong seelaprasong | `prasong5843@gmail.com` | prasong seelaprasong’s Space |
| `link_6ae2441ceaf88191aaa05e3963fef93c` | prasong seelaprasong | `prasong5843@gmail.com` | prasong seelaprasong’s Space |

Both returned the same user ID `3f0d872b-594c-811f-8d5e-000267b384d9` and workspace ID `320089a7-5dad-81c4-b5e0-00039875cd52`. These are two connector links to the same observed Notion identity, not evidence of two distinct accounts.

The four user-supplied Notion access emails remain separate user-provided references:
- `Prasong5841@gmail.com`
- `Prasong.me@proton.me`
- `LEK0805974491@gmail.com`
- `mt9w2tzs2w@privaterelay.appleid.com`

None of those four identities was returned by the currently linked connector profile. This does not prove that those accounts do not exist or that they have no workspaces. They are not currently represented by the two available connector links.

## Workspace-area listing observations

The following listing operations were run separately for both connector links:
- Private sidebar pages/databases
- Shared sidebar pages/databases
- Recently viewed pages/databases
- Teamspaces

Both links returned the same lists. Results are therefore deduplicated as one observed profile.

### Private sidebar — 7 entries
1. Welcome to Notion!
2. To Do List
3. IRIS Project Controller — Continuous Execution Workflow
4. IRIS — Sugra Project Foundation
5. IRIS — WireGuard Project Foundation
6. Loop Control — Master Checkpoint & Registers — LC-CAPMAP-20261012-003
7. Analyst

### Shared sidebar — 4 entries
1. About prasong
2. Memories (database)
3. About prasong (second page record)
4. Memories (second database record)

### Teamspaces
The connector returned `joinedTeams: []`, `otherTeams: []`, and `hasMore: false` for the connected workspace. This is an observation from this connector endpoint, not proof that no other workspace exists under the account.

### Recently viewed
The connector returned several dozen recent pages and databases. The surfaced entries included:
- IRIS Project Controller — Continuous Execution Workflow
- IRIS Workstream Status Register
- WS00–WS12 workstream pages and their database-row counterparts
- IRIS Documentation Portal — Master Build Brief
- IRIS Website — 12 Sections Execution Commands (Separate Working Spec)
- IRIS — Core Operating Structure, Work Patterns & Lifecycle
- IRIS Workstream Atomic Breakdown
- IRIS — Sugra Project Foundation
- IRIS — WireGuard Project Foundation
- Loop Control — Master Checkpoint & Registers
- To Do List / To Do List DB
- Analyst
- Welcome to Notion!
- About prasong
- Memories

Recent-page listing is a navigation surface, not a complete inventory of all pages ever created.

## Content and database reads completed

The discovered private/shared/recent page and database records were fetched read-only. Database schemas were fetched for the following data sources, and row contents were queried:

| Database / data source | Read result |
|---|---|
| IRIS Workstream Status Register — `collection://bb2a636a-227b-4643-9a5f-35a11e7363be` | 13 rows returned; all 13 have Status = In progress; no further page in pagination |
| To Do List DB — `collection://3f1089a7-5dad-805c-a8d7-000bb96e5da8` | 6 rows returned; 1 Done, 5 not Done; no further page in pagination |
| Memories — `collection://407089a7-5dad-814e-8cbb-000bc8282c71` | 0 rows |
| Memories — `collection://407089a7-5dad-819f-b370-000bb4c2b7dc` | 0 rows |

The special connected Notion Memory fetch returned: “No memories have been saved yet.” It also stated that the About page and Memories database are created with the first page saved with parent: “memory”.

### IRIS workstream register
The 13 rows are WS00 through WS12. The fetched register includes each row's Name, Workstream ID, Status, Acceptance Criteria, Dependencies, Evidence, Blockers, Checkpoint, Next Action, and Workstream Page URL. Every row currently reports `In progress`.

Examples of blockers present in the register include canonical IRIS/Portal source selection, Original CDR and 8-module source, sanitized DB/schema/sample, approved ID/contract semantics, named Approver/IdP, independent Auditor/Acceptance Authority, and test authorization. These are recorded as source content, not independently validated by this inventory task.

### To Do List DB
The six rows returned:
- Check the box to mark items as done — Done
- Click the due date below to change it — Not Done
- Click this text to see more details — Not Done
- Click the blue + button to add a task — Not Done
- See finished items in the “Done” view — Not Done
- Click me to learn to hide checked items — Not Done

## Important limitations / unresolved coverage

1. The connector currently exposes only two links, and both resolve to the same user and workspace identity.
2. The connector tools available in this session do not expose an account-level endpoint to enumerate every workspace owned by or accessible to a Notion account, nor a direct workspace-switch/list-all-workspaces action.
3. Private and Shared sidebar listing endpoints enumerate their returned sidebar entries; recent pages enumerate recently viewed items. These are not equivalent to a global export of every page, nested block, archived item, or every workspace.
4. The four user-supplied access emails are not independently connected through the current connector links. Their contents remain uninspected.
5. The user-supplied workspace ID `foil-bite-584` is deliberately not used as a search query, per the user's instruction. Its existence, display name, and account association remain USER-PROVIDED / not independently verified here.
6. Search results that return no match are not evidence that an account, workspace, or page does not exist.

## Current status

- Current connected Notion identity: OBSERVED.
- Duplicate connector links identified: OBSERVED.
- Private/Shared/Recent listing surfaces inspected: OBSERVED.
- Surfaced pages and database records fetched: OBSERVED, subject to connector visibility and fetch completeness.
- Discovered database schemas and rows queried: OBSERVED.
- All four user-supplied Notion accounts inspected: NOT COMPLETED.
- All workspaces under every account enumerated: NOT COMPLETED.
- Global completeness of all Notion content: UNKNOWN.
- External Notion mutations: NONE.

## Next action
Continue only when additional authorized Notion account connections or a supported account/workspace selection route becomes available. For each newly available account, repeat identity discovery, workspace-area listing, and read-only content/database inventory. Keep all account identities and workspace records separate until direct evidence links them.
