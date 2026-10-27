# Project Workflow Manual

Repository for the HAP project workflow, governance, evidence tracking, review, and release standards.

This repository stores the standard operating documentation used for project memory, AI workflow, and GitHub repository operations.

## Current standard
- `00_CONTROL/project-workflow-manual-v1.1.html`

## Notes
- The repository follows the workflow rules and status model defined in the project manual.
- Versioned documents are preserved and not overwritten without approval.
- Root-level legacy files are retained for historical reference.


## HAP/AICC MCP API

An authenticated MCP Streamable HTTP API implementation is available in `api/mcp.js`.

- API and deployment guide: [MCP_API.md](MCP_API.md)
- Dashboard HTML: [hap-aicc/index.html](hap-aicc/index.html)
- Archived original dashboard source: [source/hap-aicc-original.html](source/hap-aicc-original.html)
- MCP audit log: [logs/mcp-audit.jsonl](logs/mcp-audit.jsonl)

The MCP service exposes repository status, file listing, file reading, file writing, and audit-log inspection. It is designed to append metadata-only JSONL audit records to this repository. File writes and durable audit logging require a repository-scoped GitHub token stored as the Vercel `GITHUB_TOKEN` secret. The MCP endpoint additionally requires a Vercel `MCP_API_KEY` secret. No secrets belong in this repository.

The source and deployment configuration are committed, but the live MCP endpoint is not yet provisioned: Vercel currently cannot link this repository, and the required GitHub token has not been configured. See [MCP_API.md](MCP_API.md) for the remaining deployment steps.
