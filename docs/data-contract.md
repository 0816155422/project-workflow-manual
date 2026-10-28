# Course and Activity Data Contract

## Source of truth
GitHub repository content on `main` is authoritative. Pending input lives at `pending/course/course-source.json`. A record is not approved merely because it passes validation. Approval is recorded only by an explicitly invoked `sync-approved-memory.yml` run that validates the inputs and creates the final files.

## Envelope
- `schemaVersion`: exactly `"1.0"`
- `source`: exactly `"course-ui"`
- `status`: one of `pending`, `approved`, `blocked`, `rejected`
- `approvedBy`: null while pending; non-empty actor identifier when approved
- `approvedAt`: null while pending; ISO 8601 timestamp when approved
- `records`: non-empty array; empty datasets fail validation

## Record
Each record requires non-empty `id`, `title`, `category`, `status`, `updatedAt`, and `owner`.
- Record status: `pending`, `in_progress`, `completed`, `blocked`, or `rejected`
- `updatedAt`: parseable date/time
- `evidence.runId`: numeric GitHub Actions run ID as a string
- `evidence.commitSha`: full 40-character commit SHA
- `evidence.url`: HTTPS GitHub Actions run URL

IDs must be unique within a dataset. The validator performs heuristic secret scanning for GitHub tokens, AWS access-key IDs, API/token/password-like assignments, and private-key headers. A clean heuristic scan is not a guarantee that content contains no secrets.

## Lifecycle
1. Put proposed data in `pending/`; set top-level status to `pending`, with null approval fields.
2. Validation workflow checks syntax, schema, required fields, evidence formats, and likely secrets. Passing validation is not approval.
3. A human explicitly invokes the manual sync workflow with source path, new target path, and a single-line approval note.
4. The sync workflow rejects unsafe paths, symlinks, existing destinations, invalid JSON, and likely secrets; it sets approval metadata and creates the approved data mirrors with create-only semantics.
5. UI reads `hap-aicc/data/course-data.json`. Missing or invalid data must display a visible unavailable/awaiting message.
6. Workflow logs must use actual GitHub run ID, SHA, actor and evidence URL. Do not fabricate entries.

## Canonical final paths
- `shared/course/course-data.json`
- `data/course/course-data.json`
- `hap-aicc/data/course-data.json`

These final paths are deliberately absent until the manual approval workflow runs. Do not create placeholder files at these paths: the sync workflow is create-only and rejects overwrites.
