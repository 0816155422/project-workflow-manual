# Workflow Overview

1. Draft content is written into `pending/`.
2. **Validate Shared Memory** checks JSON syntax in configured areas and scans selected files for likely secrets.
3. A human reviews source, accuracy, privacy, and necessity.
4. A maintainer manually runs **Sync Approved Memory** with a source under `pending/`, a new destination under `shared/`, and an approval note.
5. The workflow validates paths and file type, refuses an existing destination, copies the file into `shared/`, appends an entry to `logs/approval-log.md`, and commits to `main`.
6. GitHub Pages serves static UI; it does not write to the repository.
7. Confirm success from the Actions run, commit history, audit log, and published page.

Secret detection is heuristic and must be supplemented by manual review. Platform snapshots require explicit export and are not automatically synchronized.