# Project Workflow Manual

This repository is a shared AI memory workspace and approved knowledge archive for multi-platform AI collaboration.

## Principles
- The repository is a source of approved memory, not a live database.
- GitHub Pages serves a public static UI.
- GitHub Actions validates and promotes reviewed content into approved shared memory.
- Never store secrets, tokens, API keys, credentials, or sensitive personal data here.
- AI systems should use explicitly approved files, not implicit chat memory.

## Repository roles
- `shared/`: approved knowledge safe for reuse across platforms
- `pending/`: drafts waiting for review and approval
- `logs/`: approval, validation, sync, and deployment history
- `platforms/`: platform-specific memory snapshots and templates
- `archives/`: historical data retained for traceability
- `private/`: local-only placeholder; sensitive content must not be pushed
- `docs/`: operational and governance documentation
- `hap-aicc/`: current GitHub Pages dashboard source

## Security and write-back
GitHub Pages is static hosting and must not write repository files directly. Write-back must occur through GitHub Actions after explicit human review. Secret scanning is heuristic and does not replace manual review.

## Current site
The current Pages workflows publish `hap-aicc/`. The `public/` and `static-site/` directories in this repository are reference layouts unless deployment configuration is deliberately changed.


## Course/activity data pipeline

The course data path is intentionally approval-gated:

1. `pending/course/course-source.json` is the candidate source. It is marked `pending`.
2. `validate-approved-memory.yml` and `ingest-course-data.yml` validate source syntax, required fields, evidence formats, and heuristic secret patterns. Validation does not approve data.
3. `sync-approved-memory.yml` is manual-only. It requires source path, new target path, and a single-line approval note; it rejects traversal, symlinks, likely secrets, and existing final paths. It was not dispatched by the implementation task.
4. After a future explicitly approved run, the workflow creates the canonical mirrors under `shared/course/`, `data/course/`, and `hap-aicc/data/`, and appends audit records.
5. The HAP/AICC course section reads `hap-aicc/data/course-data.json`. If it is missing or invalid, the UI visibly displays `Awaiting approved dataset` or `Data unavailable or invalid`; it does not substitute hardcoded records.
6. `generate-usage-log.yml` appends actual GitHub Actions run metadata to usage/workflow logs. The Pages workflow emits a run/commit/deployment URL summary and a downloadable deployment-evidence artifact.

### Evidence status

The pending fixture, scripts, and workflow definitions are repository configuration, not proof that the end-to-end pipeline has run. The final approved dataset files are intentionally absent until manual approval. Do not claim sync, write-back, UI data rendering, or latest-commit deployment without a real run ID, full commit SHA, evidence URL, and appropriate post-run verification.

## Approval-gated course data pipeline

The course/activity pipeline is intentionally fail-closed. GitHub repository content and GitHub Actions runs are the source of truth; a file or workflow definition alone is not proof of execution.

### Data lifecycle
1. Candidate input: `pending/course/course-source.json`.
2. Validation: `Validate Shared Memory and Course Data` and `Ingest and Validate Pending Course Data`.
3. Explicit human approval: manually dispatch `Sync Approved Course Data` with source path, supported new target path, and a single-line approval note.
4. Final data mirrors are created only by that approval-gated workflow at `shared/course/course-data.json`, `data/course/course-data.json`, and `hap-aicc/data/course-data.json`.
5. The static UI loads `hap-aicc/data/course-data.json`; missing/invalid data must remain visibly unavailable rather than replaced with fabricated records.
6. Pages deployment evidence is tied to the exact commit SHA and a real Actions run.

### Operational records
- Project scope and criteria: `docs/project-manifest.md`
- Phase ledger: `docs/phase-status.md`
- Operation and task ledgers: `logs/operation-log.md`, `logs/task-tracking.md`
- Workflow evidence: `logs/workflow-evidence.md`
- Usage history: `logs/usage-history.md`
- Approval audit: `logs/approval-log.md`
- Approval checklist: `templates/approval-gate.md`

### Current evidence-based status (2026-10-28)
- **Proven:** repository validation workflow run [40621846957](https://github.com/0816155422/project-workflow-manual/actions/runs/40621846957) succeeded for commit `6c6d5a0885994e9b9c0b56c2fffbd0e40f25d7f5`.
- **Proven:** Pages deployment run [40621846897](https://github.com/0816155422/project-workflow-manual/actions/runs/40621846897) succeeded for that same SHA.
- **Blocked:** no verified real course records are available. The pending source is intentionally empty and strict validation fails with `records must be a non-empty array`; see [validation run 40621846907](https://github.com/0816155422/project-workflow-manual/actions/runs/40621846907) and [ingest run 40621830477](https://github.com/0816155422/project-workflow-manual/actions/runs/40621830477).
- **Not proven:** approved sync, final data creation, approval-log entry from an actual sync, usage logger execution, and deployment of current main HEAD.
- No approval/sync workflow was dispatched during implementation. Do not treat the pending file, passing general repository validation, or an older Pages run as end-to-end completion evidence.

See `docs/reporting-rules.md` and `docs/checklists/reporting-rules.md` for append-only reporting and status semantics.
