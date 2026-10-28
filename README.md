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
