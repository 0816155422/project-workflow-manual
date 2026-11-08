# REVISION_DISCOVERY

- Discovery Timestamp: 2026-11-08
- Repository Reference: 0816155422/project-workflow-manual
- Repository ID: 1432201372
- Reference Branch: reconstruction/operating-work-lifecycle-state
- Reference Commit: fcec1b2548070df38a77c7329a8f026e71046e07
- Evidence Sources: Git tree path inventory, direct file read-back, GitHub commit history by file path, commit metadata, and releases endpoint.

## Discovery Result

- Explicit versioned manual files: FOUND (2).
- Unversioned manual file: FOUND (1).
- Package version metadata: FOUND (1).
- Explicit embedded manual revision history: FOUND (v1.0 and v1.1).
- Commit history for each inspected manual file: FOUND (one creation commit per path).
- GitHub Releases: NOT FOUND (API returned an empty list).
- Tag inventory: UNKNOWN (tag-list endpoint could not be verified through the available GitHub fetch interface).
- Dedicated revision/archive folders: FOUND, but no revision records were present in those folders beyond .gitkeep placeholders.

## Revision Records

### REV-001 — Unversioned Manual
- Path: `project-workflow-manual.html`
- Path version label: NONE
- Blob SHA: `<not separately recorded in this discovery>`
- Creation commit: `d28ccecb5114ec8fb26fde0f87e6fce6a64397e2`
- Commit date: `2026-10-25T07:06:13Z`
- Commit message: Create project-workflow-manual.html
- Parent commit: `62308f045d0efca684b4a6cb528491cfe1185581`
- Status: FOUND; embedded version status UNKNOWN.

### REV-002 — File Named v1.0.0
- Path: `project-workflow-manual-v1.0.0.html`
- Filename version: v1.0.0
- Embedded title/header version: v1.1
- Embedded document date: 2026-10-25
- Embedded version-history entries:
  - v1.0 — 2026-10-25; initial standard edition.
  - v1.1 — 2026-10-25; adds glossary, RACI matrix, naming convention, status decision tree, self-check prompt, escalation path, backup policy, schema version field, and conflict resolution; adjusts Schema 2; states that v1.0 content was retained.
- Blob SHA: `fc8fd6340d9417e8b84846ac5caaccbc2f223679`
- Creation commit: `8d245effe4956031ec2b1ce41c1fd66e88fb12b6`
- Commit date: `2026-10-25T07:08:14Z`
- Commit message: Create project-workflow-manual-v1.0.0.html
- Parent commit: `d28ccecb5114ec8fb26fde0f87e6fce6a64397e2`
- Status: FOUND.
- Revision discrepancy: filename says v1.0.0 while embedded title/header and history identify v1.1. Preserve both observations; do not normalize.

### REV-003 — Control Directory Manual v1.1
- Path: `00_CONTROL/project-workflow-manual-v1.1.html`
- Filename version: v1.1
- Embedded document version: v1.1
- Embedded document date: 2026-10-25
- Embedded content says it is an update from v1.0 without deleting prior content.
- Blob SHA: `7ff4ec8ff8cd724cf279f1ff3c59342a7adc4add`
- Creation commit: `de0a038b7b23bc0e4b8bcdcceb8a80e3e909b456`
- Commit date: `2026-10-25T07:22:54Z`
- Commit message: Create the v1.1 workflow manual in the required control directory and align repo structure with the documented standards
- Parent commit: `53def0f98ef45cfc19d650cb28c2f119fdd92b1e`
- Status: FOUND.
- Revision boundary: This file has a different blob SHA from the root file named v1.0.0, despite both embedding v1.1. The commit parent is not the recorded creation commit of REV-002. No direct file ancestry is asserted.

### REV-004 — Package Version
- Path: `package.json`
- Version value: `1.0.0`
- Blob SHA: `4d3067dfe4eff47dd977291b4de8ecf7cca1af55`
- Status: FOUND.
- Boundary: This is package metadata and is not assumed to be the version of either HTML manual.

## Revision History Evidence

GitHub file-path commit history returned one creation commit for each of:
- `project-workflow-manual.html`
- `project-workflow-manual-v1.0.0.html`
- `00_CONTROL/project-workflow-manual-v1.1.html`

This establishes the observed creation commits for those paths. It does not establish that no revisions existed outside the inspected branch history or before repository import.

## Revision / Archive Locations

- `13_Change_Version/`: directory exists; tree contains only `.gitkeep`.
- `14_Archive_Superseded/`: directory exists; tree contains only `.gitkeep`.
- `archives/`: contains README guidance and subdirectory README files; no archived manual version was present in the inspected tree.
- `archives/README.md` says historical context and superseded documents should be retained for traceability and not treated as current approved guidance without review.
- `source/README.md` identifies `source/hap-aicc-original.html` as an archived copy of dashboard source, not as a manual revision.
- `logs/approval-log.md` contains an entry template and states that no approval entries are recorded.

## Other Revision Signals

- The `00_CONTROL/project-workflow-manual-v1.1.html` document describes a rule to add new versions, preserve prior originals, and move superseded versions to archive rather than overwrite them.
- The current repository tree does not contain `00_CONTROL/project-workflow-manual-v1.0.html` or a manual file under `99_ARCHIVE/`.
- GitHub Releases API returned an empty list.
- Tag inventory remains UNKNOWN because the available fetch interface did not provide a verifiable tag listing.

## Conflicts / Unknowns Preserved

1. Filename `project-workflow-manual-v1.0.0.html` conflicts with its embedded v1.1 title/header and internal version history.
2. Two distinct files claim v1.1 but have different blob SHAs and different paths.
3. The recorded v1.1 creation commit has a parent different from the recorded v1.0.0-file creation commit; no direct revision ancestry is asserted.
4. The expected v1.0 manual path under `00_CONTROL/` is not present in the inspected tree.
5. No approved revision/release register was found in `13_Change_Version/` or `14_Archive_Superseded/`.
6. The meaning of package version 1.0.0 relative to manual version 1.1 is UNKNOWN.

## Scope Boundary
This task only discovered existing version labels, file-path history, creation commits, revision-history statements, and archive/release indicators. No files were renamed, overwritten, moved, approved, or reconciled. No revision chain was inferred beyond directly observed Git commit parent references.

## Task Closure
- TASK-010: COMPLETE
- Snapshot: PERSISTED
- Read-back: PENDING
- TASK-011: NOT STARTED
- WORKSPACE: EMPTY
