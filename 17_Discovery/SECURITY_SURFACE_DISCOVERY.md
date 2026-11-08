# SECURITY_SURFACE_DISCOVERY

- Task ID: TASK-SEC-001
- Discovery date: 2026-11-08
- Repository: 0816155422/project-workflow-manual
- Repository ID: 1432201372
- Visibility: public
- Default branch: main
- Working discovery branch: reconstruction/operating-work-lifecycle-state
- Working branch HEAD: f15604217ccc9f8ff57d94368eb052b81be90388
- Main HEAD observed during this discovery: 2e9eac7cb54823c9ede9efb630798bd6eb06497b
- Working branch tree: 407 entries, 11 workflow files, recursive response not truncated.
- Overall security posture: INCONCLUSIVE
- Discovery scope: repository configuration, branches, workflows, source/API, audit records, deployment declarations, and accessible security-control metadata.
- Execution boundary: read-only discovery. No workflow dispatched, no application code changed, no security setting changed, no deployment initiated.

## 1. Repository and Branch Controls

Repository metadata read-back confirms:
- Repository is public.
- Default branch is main.
- Repository ID is 1432201372.
- Working discovery branch is reconstruction/operating-work-lifecycle-state.

The GitHub branches response returned seven branches. Every returned branch had protected=false:
- 0816155422-patch-1 — 1821fb148d2d676bc7d2351ab6b96cedf4ae7df9
- adapter/iris-evidence-template — b3d4a04db0b37be4520812877f1777f6b8d9b02c
- dependabot/npm_and_yarn/npm_and_yarn-11c2e24550 — 5d4694067376b05845b81a3003e2f14a12b5464d
- feat/github-actions-api-runner — c85259b5fc86de18308ae697e613ba2eb9ad3f34
- feature/init-gh-native-structure — f4e14597f4e6c908af165a6244472344210727c0
- main — 2e9eac7cb54823c9ede9efb630798bd6eb06497b
- reconstruction/operating-work-lifecycle-state — f15604217ccc9f8ff57d94368eb052b81be90388

Repository rulesets endpoint returned an empty array. This is evidence of the returned ruleset inventory, not proof that every possible organization-level control is absent.

Observation:
- Branch protection is not configured on any of the seven branches in the returned branch inventory.
- No repository ruleset was returned.
- The connected integration permission snapshot is not a complete human collaborator inventory.

## 2. Workflow Surface

The working branch contains 11 workflow files:
- api-runner.yml
- codeql.yml
- deploy-pages.yml
- generate-usage-log.yml
- ingest-course-data.yml
- ingest-openai-research.yml
- iris-runtime-tests.yml
- sync-approved-memory.yml
- validate-approved-memory.yml
- validate-course-data.yml
- validate.yml

Observed permission declarations:
- generate-usage-log.yml: contents: write.
- sync-approved-memory.yml: contents: write.
- deploy-pages.yml: contents: read, pages: write, id-token: write.
- codeql.yml: security-events: write, packages: read, actions: read, contents: read.
- validate.yml, api-runner.yml, ingest-course-data.yml, ingest-openai-research.yml, validate-approved-memory.yml, and validate-course-data.yml declare contents: read.
- iris-runtime-tests.yml has no explicit permissions block in the inspected workflow source. Effective token permissions were not established from this file alone.

Workflow supply-chain observations:
- Actions are referenced by version tags such as actions/checkout@v4, actions/setup-python@v5, github/codeql-action/*@v4, actions/configure-pages@v5, and actions/deploy-pages@v4.
- The inspected workflow files do not pin those action references to immutable commit SHAs.
- CodeQL's language matrix includes javascript-typescript only.
- CodeQL push and pull-request triggers target main; its scheduled trigger is configured separately.
- The working branch contains Python runtime code, but the inspected CodeQL matrix does not include Python.
- Workflow definitions are not execution evidence. No CodeQL run was dispatched or independently verified during this discovery.

## 3. Secret and Sensitive-Data Controls

Observed controls:
- config/privacy-policy.json prohibits secrets, tokens, API keys, passwords, credentials, sensitive personal data, and private memory commits.
- .gitignore excludes .env, .env.* except .env.example, private/** except private/README.md, and common local artifacts.
- .env.example contains placeholder values and instructions not to commit real secrets.
- docs/security-checklist.md explicitly says secret detection is heuristic and manual review remains mandatory.
- validate.yml runs a pattern-based credential scan over selected text files in shared, pending, config, platforms, public, and static-site.

Limitations:
- The scanner is explicitly heuristic, not comprehensive.
- The inspected scan path list does not include the entire repository, including all workflow, API, script, log, and history surfaces.
- No complete history-wide secret scan was performed.
- No live secret-scanning or push-protection setting was verified.
- No credential value is reproduced in this report.

## 4. MCP API Surface

Source inspected:
- api/mcp.js — blob SHA 223db517d88dc8baba9302779e570ac68a6d9e57
- MCP_API.md — blob SHA 5bf9718558c60444b94f3c8ff5af0a8a8c51f8ff
- vercel.json — blob SHA b2baadd70f6e865b2d87bfde883576b9f41f7621

Observed controls:
- Non-health MCP requests require Authorization: Bearer using MCP_API_KEY.
- Write operations require GITHUB_TOKEN.
- The write path guard blocks absolute paths, traversal, backslashes, .github/workflows/, environment-file paths, and logs/mcp-audit.jsonl.
- The API uses GitHub Contents API operations against the configured repository and branch.
- The health endpoint does not require bearer authentication and returns repository identity plus boolean readiness indicators for auth and GitHub write configuration.
- The audit log design omits file contents and credentials.
- The audit append routine retries selected GitHub content conflicts.

Source-level gaps:
- write_file is not restricted to a narrow allowlist of data paths. Outside its explicit deny rules, it can create or replace repository files, including state files and non-audit log files.
- The source has no visible per-user role or per-path authorization model beyond possession of the shared bearer key and GITHUB_TOKEN.
- The audited() wrapper catches durable audit append failure, writes a platform console error, and does not make the successful tool result fail solely because the durable audit append failed.
- No rate-limit or request-size control is visible in this source file.
- These are source observations only; deployed runtime behavior and external platform controls remain unverified.

## 5. Audit and Approval Records

- logs/mcp-audit.jsonl contains one bootstrap record stating that no API requests had been processed when the log was initialized. This is the contents of the inspected branch file, not proof about every deployed environment or later runtime.
- logs/approval-log.md contains only its entry template and states that no approval entries are recorded by the template itself.
- The workflow source can append approval and workflow evidence during an actual manual sync run, but no such run was initiated by this discovery.
- No durable audit-persistence test was performed.

## 6. Deployment and External Connection Surface

- vercel.json declares an API function at api/mcp.js and rewrites /mcp and /mcp/health to that function.
- .mcp.json declares a local iris-controller command using python -m iris_runtime and IRIS_DB_PATH=${PLUGIN_DATA}/iris.db.
- .env.example documents MCP_API_KEY and GITHUB_TOKEN as deployment environment variables; no actual secret values are stored in that example file.
- No live Vercel deployment, deployed environment-variable configuration, production/preview separation, or runtime request was verified.
- The existence of deployment configuration does not prove that the service is deployed or connected.
- A Dependabot-named branch exists. No .github/dependabot.yml was present in the inspected working-branch tree. This does not establish whether Dependabot alerts or updates are enabled.
- GitHub Dependabot/code-scanning alert endpoints were not accessible through the available repository connection in this discovery. Alert inventory is therefore Not proven.

## 7. Findings and Evidence Status

### Proven observations
1. Repository visibility is public.
2. All seven branches returned by GitHub have protected=false.
3. The repository rulesets endpoint returned an empty array.
4. Two workflows declare contents: write.
5. CodeQL is configured for JavaScript/TypeScript only and targets main for push/pull-request events.
6. Secret scanning in validate.yml is heuristic and limited to selected directories and extensions.
7. MCP non-health requests require bearer authentication in source.
8. MCP write_file has deny rules but no narrow allowlist for writable repository paths.
9. Durable audit append failure is caught and logged to platform console without necessarily failing the MCP operation response.
10. The audit log inspected on this branch contains only its bootstrap record.
11. Deployment configuration exists, but no deployed runtime was verified.

### Not proven / inaccessible
- Dependabot alert inventory.
- Code-scanning alert inventory and actual CodeQL run coverage.
- Secret-scanning and push-protection settings.
- Complete human collaborator and outside-collaborator inventory.
- Organization-level policy and enforcement settings.
- Vercel project access, production/preview environment variables, and deployed runtime.
- Runtime authentication, rate limiting, request-size behavior, and durable audit persistence.
- Complete history-wide secret exposure status.

### Overall classification
- Repository/source observations: Proven within the inspected paths and returned API responses.
- Overall security posture: Inconclusive.
- Security group closure: Not authorized by this discovery and not supported by the available evidence.
- No statement that the repository is vulnerability-free is made.

## 8. Scope Boundary and Next Safe Action

This task records existing security surfaces, source controls, permission declarations, and inaccessible evidence areas. It does not remediate findings, change permissions, edit workflows, rotate credentials, change deployment settings, or close security groups.

Next safe action:
Obtain independent evidence for GitHub security-alert/settings inventory and the deployed Vercel runtime, then reconcile those results against this source-level discovery before any security group is considered for closure.

## Task Closure
- TASK-SEC-001: DISCOVERY SNAPSHOT COMPLETE
- Snapshot: PERSISTED
- Read-back: PENDING
- Overall security posture: INCONCLUSIVE
- WORKSPACE: EMPTY
