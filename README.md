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
