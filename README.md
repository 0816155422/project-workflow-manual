# Project Workflow Manual

Repository for the HAP project workflow, governance, evidence tracking, review, and release standards.

This repository stores the standard operating documentation used for project memory, AI workflow, and GitHub repository operations.

## Current standard
- `00_CONTROL/project-workflow-manual-v1.1.html`

## Notes
- The repository follows the workflow rules and status model defined in the project manual.
- Versioned documents are preserved and not overwritten without approval.
- Root-level legacy files are retained for historical reference.

## GitHub Actions repository API

The `.github/workflows/api-runner.yml` workflow supports both reading and writing repository files without adding an external hosting platform.

Supported operations:
- `repository_status` — repository metadata.
- `list_files` — list a directory's contents.
- `read_file` — read a file.
- `write_file` — create or update a file with a commit message.

To run it, open **Actions → GitHub Actions API Runner → Run workflow** and choose the operation. For `write_file`, provide the repository-relative path, complete file content, commit message, and optionally the target branch. Writes use the workflow's `GITHUB_TOKEN`, require `contents: write`, and append metadata-only audit records to `logs/mcp-audit.jsonl`. File contents are not copied into the audit log.

For safety, writes reject absolute paths, traversal, `.env` files, `.github/workflows/`, and the audit log itself. Review the target branch and diff before merging any changes.

## HAP/AICC MCP HTTP API

An authenticated MCP Streamable HTTP API implementation is in `api/mcp.js`. It exposes repository status, file listing, file reading, file writing, and audit-log inspection.

- API details: [MCP_API.md](MCP_API.md)
- Dashboard HTML: [hap-aicc/index.html](hap-aicc/index.html)
- Archived original dashboard source: [source/hap-aicc-original.html](source/hap-aicc-original.html)
- MCP audit log: [logs/mcp-audit.jsonl](logs/mcp-audit.jsonl)

The HTTP MCP endpoint is a separate service and is not currently hosted. The GitHub Actions workflow above is the available GitHub-native read/write interface; it does not pretend to be a persistent HTTP MCP endpoint. No secrets belong in this repository.
