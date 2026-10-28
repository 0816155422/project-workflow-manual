# Reporting Rules (Append-only)

## 1. Append-only history
1. Do not delete, reorder, or overwrite historical checklist entries or reports.
2. Every new investigation creates a new entry with a unique Report ID and/or Entry ID.
3. If a status changes, add a new entry. Reference the earlier entry and explain what new evidence caused the change.
4. Preserve prior findings even when they are incorrect or superseded; add a correction instead of silently rewriting history.
5. Do not use a mutable “current status” field as a substitute for the historical log.

## 2. Required fields
Every checklist item must include:
- Status
- Evidence
- Notes
- Observation timestamp, including timezone when available

Every report must identify:
- Repository and branch
- Scope and objective
- Commit SHA where relevant
- Evidence sources
- Limitations
- Next action

## 3. Allowed status values
Use these terms consistently:
- **Proven** — direct evidence supports the specific claim.
- **Not proven** — sufficient evidence for the claim has not been found.
- **Blocked** — a specific environmental, permission, or prerequisite constraint prevents the check.
- **Inconclusive** — available evidence is insufficient or ambiguous and does not justify a decision.

Do not treat “Not proven” as proof that something failed. Do not treat a workflow's success as proof of a separate deployment, sync, or write-back operation.

## 4. Evidence requirements
1. Link to direct evidence whenever possible: GitHub API response/page, workflow run, job logs, commit, file path, diff, deployment output, or checked URL.
2. Record Run ID and commit SHA for workflow claims.
3. For deployment claims, match the deployment run to the exact commit being claimed as deployed.
4. For write-back claims, verify the source, destination, resulting commit, changed file content, and audit-log entry.
5. Record when evidence was observed. A past successful run does not establish current live status.
6. Distinguish observed facts from assumptions, recommendations, and unresolved questions.
7. Do not claim success without evidence supporting that exact claim.

## 5. Keep statuses separate
Always distinguish:
- Repository status
- Local environment status
- Workflow execution status
- Deployment status
- Write-back/sync status
- Approval status
- Security review status

Do not treat a local environment limitation as a repository failure. Do not treat repository accessibility as proof that a workflow ran. Do not treat workflow success as proof that the latest commit is deployed.

## 6. Approval and write operations
1. Read-only inspection does not authorize write-back.
2. Before any write-back, confirm the exact source path, destination path, and explicit approval note required by the applicable workflow.
3. Do not infer approval from a pending file, example, template, prior discussion, or absence of objections.
4. Do not run a sync/write workflow when required approval details are missing or marked pending.
5. Record the approving instruction and resulting evidence without exposing secrets.

## 7. Security checks
- Mark credential scanning as heuristic if it is pattern-based; do not call it a complete security audit.
- Verify path traversal, symlink, overwrite, and approval controls against workflow contents and/or test evidence before marking them Proven.
- Separate a control's presence in source code from evidence that it behaved correctly in execution.
- Never place tokens, passwords, private keys, or other secrets in reports.

## 8. Final conclusion
Use one of:
- Safe
- Needs review
- Blocked
- Ready for next step

Explain the evidence behind the conclusion, identify what remains Not proven or Inconclusive, and state the next verification step. “Ready for next step” does not mean an unverified operation has completed.


## 9. Required subsystem statuses
Every end-to-end course data report must separately state one of: Proven, Not proven, Blocked, or Inconclusive for:
- pending source and its blob/commit SHA
- validation and ingest workflow runs
- manual approval/sync run and approval note
- final data target existence and commit
- approval log, usage log, and workflow evidence
- UI rendering against the approved dataset
- Pages deployment run, page URL, and deployed commit SHA

Do not convert an absent workflow run into a success claim. A run must be linked by its actual run ID and URL, and its head SHA must be checked. Preserve failed, cancelled, skipped, and inconclusive outcomes in subsequent append-only entries.
