# Repository Reporting Rules

Every report is append-only. Never delete, reorder, or overwrite an existing report or historical log entry. When a fact changes, append a new entry with a timestamp and links to the evidence; do not silently rewrite the previous state.

## Required report fields
Report ID; Date/Time; Reporter; Repository; Branch; Scope; Objective; Source of truth; Evidence sources; Repository status; Workflow status; Deployment status; Write-back/sync status; Security and approval review; Proven facts; Not proven facts; Open questions; Conclusion; Next safe action.

## Allowed status values
- **Proven** — directly supported by repository content, a GitHub Actions run, a commit, or other linked primary evidence.
- **Not proven** — no sufficient evidence was observed.
- **Blocked** — a guardrail or missing prerequisite prevents safe progress.
- **Inconclusive** — evidence is incomplete or contradictory.

## Evidence discipline
- Link workflow run ID, workflow name, head commit SHA and run URL.
- A workflow definition does not prove execution.
- A successful validation run does not prove sync, write-back, UI rendering, or deployment.
- Deployment is proven for a revision only when a real deploy run's head SHA is captured and matches the revision claimed as deployed.
- Do not hide failed, cancelled, skipped, or inconclusive runs.
- Record environment failures as environment limitations, not repository failures, unless repository evidence supports that conclusion.
- Secret scans are heuristic; never log secret values.
- Pending data remains pending until the manual approval workflow creates the final dataset.
