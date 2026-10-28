# Report: [Project / Workflow / Deployment / Security Review]

- Report ID:
- Date/Time (include timezone, preferably ISO 8601):
- Reporter:
- Repository:
- Branch:
- Scope:
- Objective:
- Source of truth:
  - [ ] GitHub API
  - [ ] Workflow run logs
  - [ ] Repository file contents
  - [ ] Pages deployment logs
  - [ ] Local environment
  - [ ] Other:

## 1. Objective
- What are we trying to verify?
- Exact question to answer:

## 2. Scope
- In scope:
- Out of scope:
- Environment scope:
  - Local environment:
  - GitHub environment:
  - Repository:
  - Pages:
  - Workflow:
  - External dependencies:
  - Other:

## 3. Evidence Sources
- Repository metadata:
- Workflow definitions:
- Workflow run logs:
- Commit SHA:
- Deployment logs:
- Local environment logs:
- URL checked:
- Limitations or unavailable evidence:
  - DNS blocked:
  - API access limited:
  - Clone unavailable:
  - Live status unavailable:
  - Other:
- Evidence collection time:

## 4. Repository Status
- Repository accessible via GitHub API: Proven / Not proven / Blocked / Inconclusive
- File structure confirmed: Proven / Not proven / Blocked / Inconclusive
- Branch:
- Repository type: static site / workflow repo / memory repo / mixed / other
- Evidence:
- Notes:

## 5. Workflow Status
### Validation workflow
- Status: Proven / Not proven / Blocked / Inconclusive
- Run ID:
- Commit SHA:
- Run URL:
- Proof:
- Notes:

### Read-only API runner
- Status: Proven / Not proven / Blocked / Inconclusive
- Run ID:
- Commit SHA:
- Run URL:
- Proof:
- Notes:

### Sync workflow
- Status: Proven / Not proven / Blocked / Inconclusive
- Run ID:
- Commit SHA:
- Run URL:
- Proof:
- Notes:

### Pages deployment workflow
- Status: Proven / Not proven / Blocked / Inconclusive
- Run ID:
- Commit SHA:
- Run URL:
- Proof:
- Notes:

## 6. Deployment Status
- Pages deployment success: Proven / Not proven / Blocked / Inconclusive
- Latest commit deployed: Proven / Not proven / Blocked / Inconclusive
- URL checked:
- Deployment evidence (job logs / run summary / commit SHA / artifact):
- Evidence collection time:
- Notes:

## 7. Write-back / Sync Status
- Sync approved: Proven / Not proven / Blocked / Inconclusive
- Source file:
- Target file:
- Approval note:
- Audit log created: Proven / Not proven / Blocked / Inconclusive
- Write-back evidence (commit SHA / file diff / approval log entry):
- Notes:

## 8. Security & Approval Review
- API runner read-only: Proven / Not proven / Blocked / Inconclusive
- Path traversal blocked: Proven / Not proven / Blocked / Inconclusive
- Symlink blocked: Proven / Not proven / Blocked / Inconclusive
- Overwrite blocked: Proven / Not proven / Blocked / Inconclusive
- Credential scan: Heuristic only / Manual review required / Passed / Blocked / Inconclusive
- Approval required before write-back: Proven / Not proven / Blocked / Inconclusive
- Risk notes:
- Evidence:

## 9. Proven Facts
- [Fact, evidence reference, and timestamp]
- [Fact, evidence reference, and timestamp]

## 10. Not Proven / Open Questions
- [Question, missing evidence, and next verification step]

## 11. Conclusion
- Status: Safe / Needs review / Blocked / Ready for next step
- Reason:
- Next action:
- Recommended next step:
- Reviewer:
- Review timestamp:

## Evidence Reference Format
For each material claim, include a direct URL or repository path, run ID, commit SHA, and observation timestamp where available. Do not describe a check as successful unless the referenced evidence supports that exact claim.


## Required Status Vocabulary for Each Subsystem

Use exactly one of these labels for each relevant finding:
- Proven
- Not proven
- Blocked
- Inconclusive

Report these separately: repository status; validation workflow status; ingest workflow status; approval/sync status; target-file existence; approval-log status; usage-log status; workflow-evidence status; UI data-render status; deployment status and deployed commit SHA.

Never fill a missing value with a guess. Use “Not observed” or “Not proven” and include the next safe verification action.
