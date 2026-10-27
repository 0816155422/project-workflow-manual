# HAP/AICC MCP API

Authenticated Model Context Protocol (MCP) Streamable HTTP endpoint for the HAP/AICC project workflow repository.

## Repository source of truth

- Dashboard source: `hap-aicc/index.html`
- Archived copy of the published dashboard source: `source/hap-aicc-original.html`
- MCP implementation: `api/mcp.js`
- Audit trail: `logs/mcp-audit.jsonl` (JSON Lines; records tool, path, timestamp, result, duration and error metadata; never stores file contents or credentials)
- Runtime/deployment config: `package.json`, `vercel.json`, `.env.example`

## Tools exposed

- `repository_status` — repository identity and branch.
- `list_files(prefix?)` — list tracked files.
- `read_file(path)` — read a repository file.
- `write_file(path, content, message)` — create/update a file; requires a GitHub token and protects workflow, secret and audit paths.
- `audit_log_tail(lines?)` — inspect recent audit records.

Every MCP tool invocation attempts to append a durable audit record to `logs/mcp-audit.jsonl` through the GitHub Contents API. The log intentionally omits file contents, tokens and arbitrary tool arguments. If GitHub audit persistence fails, the runtime emits an error to its platform logs; do not treat that request as durably audited.

## Deploy to Vercel

1. Import `0816155422/project-workflow-manual` as a Vercel project with the repository root as the Root Directory.
2. Set the following environment variables in Vercel Project Settings (Production and any desired Preview environments):
   - `MCP_API_KEY`: a long, random client authentication secret.
   - `GITHUB_TOKEN`: a fine-grained GitHub token scoped to this repository with Contents read/write permission. Keep it in Vercel secrets only; never commit it or send it in chat.
   - `GITHUB_OWNER=0816155422`
   - `GITHUB_REPO=project-workflow-manual`
   - `GITHUB_BRANCH=main`
3. Redeploy after setting the environment variables.

## MCP client configuration

Use the deployed HTTPS origin plus `/mcp` as the MCP server URL and configure the client's HTTP Authorization header as `Bearer <MCP_API_KEY>`.

## Endpoints

- `POST /mcp` — MCP JSON-RPC requests.
- `GET /mcp` and `DELETE /mcp` — Streamable HTTP transport methods.
- `GET /mcp/health` — non-secret readiness status.

## Security / operational notes

- Never expose `GITHUB_TOKEN` or `MCP_API_KEY` in the repository or audit logs.
- MCP access is protected by bearer authentication.
- File writes are restricted from `.github/workflows/`, environment files and the audit log.
- The audit file is stored in a public repository; it must contain metadata only. Concurrent append conflicts are retried.
- This is a repository-file MCP API, not a database; writes create Git commits and are versioned by GitHub.
