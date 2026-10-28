# Approval Policy: Course and Activity Data

## Non-negotiable gate
No write-back, sync, promotion, or creation of final approved dataset files may occur without an explicit human approval action through the manual `.github/workflows/sync-approved-memory.yml` workflow. A push, validation success, workflow file, approval-note text in an ordinary commit, or pending fixture is not itself approval.

## Approval action
The authorized operator must manually dispatch the workflow and provide:
- `source_path`: existing regular file below `pending/`
- `target_path`: new destination below `shared/` or `data/`; course sync currently supports the canonical course targets only
- `approval_note`: one line, 1–300 characters, no newline

The workflow actor is recorded as the approver. Repository environment protections and required reviewers should be configured in GitHub Settings if a second-person review is required; a workflow dispatch alone does not prove branch protection or external review settings.

## Required safety checks
- reject traversal, absolute paths, backslashes, symlinks, unsupported extensions, missing/non-regular source, existing target, and multi-line/overlong notes
- reject likely credentials and validate JSON/schema at approval time
- use create-only writes for final data mirrors
- append an approval audit entry and retain GitHub run/commit evidence
- never mark the pending source as approved in place

## Current implementation status
The policy and workflow definitions are documentation/configuration, not evidence of an executed approval. The sample course record remains pending. Do not invoke the sync workflow until the human explicitly intends to approve the exact source and destination.
