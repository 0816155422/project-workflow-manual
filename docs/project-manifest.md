# Project Manifest — Repository Automation

- Project ID: PWA-2026-10-28
- Repository: `0816155422/project-workflow-manual`
- Repository ID: `1432201372`
- Branch: `main`
- Created at: `2026-10-28T09:32:00+07:00`
- Updated at: `2026-10-28T09:36:00+07:00`
- Actor/system identity: GitHub-connected repository automation agent; GitHub actor observed in Actions: `0816155422`
- Source of truth: GitHub repository content, commits, GitHub Actions run metadata/job steps, and deployment evidence artifacts.

## Objective
Implement a verifiable course/activity data path from pending input through validation and explicit manual approval to approved dataset rendering, append-only usage/workflow evidence, and commit-bound GitHub Pages deployment.

## Non-negotiable controls
1. Pending data is not approved data.
2. Only a manually dispatched approval-gated workflow may create final course dataset paths.
3. No sample or invented course records are accepted as real source data.
4. Workflow definitions are not execution evidence.
5. Deployment is proven only for a real successful deploy run and its exact head SHA.
6. Operational logs are append-only; never delete or rewrite historical entries.
7. Never put credentials or secret values in repository files or logs.
8. Secret scanning is heuristic and does not guarantee absence of secrets.

## Required paths
- Workflows: `.github/workflows/validate-approved-memory.yml`, `.github/workflows/sync-approved-memory.yml`, `.github/workflows/ingest-course-data.yml`, `.github/workflows/generate-usage-log.yml`, `.github/workflows/deploy-pages.yml`
- Validation/sync/logging scripts: `scripts/validate-course-data.mjs`, `scripts/sync-course-data.mjs`, `scripts/generate-usage-log.mjs`
- UI: `hap-aicc/index.html`, `hap-aicc/app.js`, `hap-aicc/styles.css`
- Data: `pending/course/course-source.json`, `shared/course/course-data.json`, `data/course/course-data.json`, `hap-aicc/data/course-data.json`
- Records: `logs/operation-log.md`, `logs/task-tracking.md`, `logs/workflow-evidence.md`, `logs/approval-log.md`, `logs/usage-history.md`
- Policy/docs: `docs/data-contract.md`, `docs/approval-policy.md`, `docs/reporting-rules.md`, `docs/phase-status.md`, `templates/approval-gate.md`

## Current baseline evidence
- Main HEAD observed during audit: `53abab031fac464fc871f94480f2143f2896fe12`.
- Successful Pages deployment run: [40618194726](https://github.com/0816155422/project-workflow-manual/actions/runs/40618194726), head SHA matched the observed main HEAD at audit time.
- Final approved course dataset paths were absent during audit.
- Pending source existed with a sample-looking record; it is not treated as trustworthy real course data and must not be promoted without real source evidence and explicit approval.

## Completion criteria
Validation must produce real run evidence; manual sync must produce a successful run, target data, and approval log; usage/workflow evidence must link real run metadata; Pages deployment must have a successful run whose SHA matches the claimed deployed revision; UI must be read back against the approved dataset or explicitly show the missing/invalid state. Overall completion remains unproven until all conditions are evidenced.

## Implementation status snapshot — 2026-10-28T02:35:00Z
- Operational records and approval checklist were added to the repository.
- The prior sample-looking pending record was removed; `pending/course/course-source.json` now has an empty `records` array and intentionally fails strict validation.
- Actual validation run [40621830468](https://github.com/0816155422/project-workflow-manual/actions/runs/40621830468) failed with `records must be a non-empty array.`; ingest run [40621830477](https://github.com/0816155422/project-workflow-manual/actions/runs/40621830477) failed for the same missing-data reason.
- No sync workflow was dispatched. Final dataset files remain absent by design.
- The previous successful Pages run [40618194726](https://github.com/0816155422/project-workflow-manual/actions/runs/40618194726) proves deployment only for its recorded SHA, not any later commit.
- Current overall status: **Blocked** for approved-data integration; **Not proven** for end-to-end sync; **Inconclusive** for deployment of the current HEAD until a matching run is observed.
