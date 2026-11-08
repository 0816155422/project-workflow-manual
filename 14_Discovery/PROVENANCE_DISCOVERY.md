# PROVENANCE_DISCOVERY

- Discovery Timestamp: 2026-11-08
- Repository Reference: 0816155422/project-workflow-manual
- Repository ID: 1432201372
- Reference Branch: reconstruction/operating-work-lifecycle-state
- Current Branch HEAD observed during this task: bb608e9cac1e33d7959e1c813b0f9c21c8871587
- Evidence Sources: Direct GitHub read-back of source register, raw source index, manifests, state/checkpoint files, logs, and reporting/approval rules.

## Provenance Discovery Summary

- Existing source register: FOUND.
- Source register records: 40.
- Source classes recorded: USER_CONFIRMED_PRIOR_CONVERSATION=2; USER_CONFIRMED_CURRENT_AND_PRIOR_TASK=1; REPOSITORY_OBSERVED=29; SOURCE_CODE_OBSERVED=8.
- Raw research source records: 3.
- User conversation sources with exact repository transcript locators: NOT FOUND in the source register.
- Repository file provenance references: FOUND.
- External source-code provenance: FOUND.
- Workflow/action provenance: FOUND in logs and state records.
- Human approval evidence in approval log: NOT FOUND; the approval log states no approval entries are recorded.

## Existing Source Register

Path: `04_Discovery/system-translation-source-register.json`
Record ID: `SYS-SRC-001`
Classification: `DISCOVERY_NOT_CANONICAL`
Recorded branch: `reconstruction/operating-work-lifecycle-state`
Recorded observed branch HEAD: `502d8c78411b179f2e39195b5231d8921c249aba`
Current branch HEAD observed during this task: `bb608e9cac1e33d7959e1c813b0f9c21c8871587`
Register blob SHA: `42a63ff58a9e3e811bd333b7c56db5a4913fd956`

The source register's observed branch HEAD is different from the branch HEAD observed during this task. The source register is therefore a historical provenance snapshot and is not silently treated as current branch state.

### All recorded source entries

| Source ID | Provenance Type | Repository | Branch | Repository Path | Recorded Blob SHA | Recorded Commit | Locator Status |
|---|---|---|---|---|---|---|---|
| SRC-USER-001 | USER_CONFIRMED_PRIOR_CONVERSATION | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | No repository file locator | Not recorded | Not recorded | conversation source not available as repository file; exact transcript locator UNKNOWN |
| SRC-USER-002 | USER_CONFIRMED_PRIOR_CONVERSATION | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | No repository file locator | Not recorded | Not recorded | conversation source not available as repository file; exact transcript locator UNKNOWN |
| SRC-USER-003 | USER_CONFIRMED_CURRENT_AND_PRIOR_TASK | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | No repository file locator | Not recorded | Not recorded | user-supplied in conversation; exact transcript not committed |
| SRC-REPO-001 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/session-state.json | b4cde3496a464f40f8fa6a81a1b11fc5ec7ff276 | Not recorded | Not stated |
| SRC-REPO-002 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/phase-status.json | 3eb6f5493707206ec80e97a129edc220d754693c | Not recorded | Not stated |
| SRC-REPO-003 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/last-run.json | 7e2f12e027d5b564cb40de00c7666e45fab63ae7 | Not recorded | Not stated |
| SRC-REPO-004 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/checkpoints/latest.json | 036eb0d50a42b7fb83629c5428b55792088a8a05 | Not recorded | Not stated |
| SRC-REPO-005 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/checkpoints/CKPT-20261108-006.json | 1c5bdc0ef38c3b4caf5e94dfd8a25fcb0700b04e | Not recorded | Not stated |
| SRC-REPO-006 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/checkpoints/CKPT-20261108-007.json | abaea404fa2a5b4fcf6b4c8afe1e1f152faf8cf2 | Not recorded | Not stated |
| SRC-REPO-007 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | state/checkpoints/CKPT-20261108-008.json | 717d4858250c6f40771f95104de7a92772c576f2 | Not recorded | Not stated |
| SRC-REPO-008 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | 04_Discovery/operating-work-lifecycle-reconstruction-state.md | bed59033e9af8ed74e17b142abab09fc9ccfc842 | Not recorded | Not stated |
| SRC-REPO-009 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | 04_Discovery/iris-controller-operating-work-lifecycle-reconstruction.md | 784ee8f9c707f1be16297f6b9e3130dccc58b7f5 | Not recorded | Not stated |
| SRC-REPO-010 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | MEMORY_MANIFEST.md | acfca3be866ccd55211ef929c57c70db665e34fc | Not recorded | Not stated |
| SRC-REPO-011 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | docs/project-manifest.md | 425c417910eee4fb4c56780cea7d0987483046eb | Not recorded | Not stated |
| SRC-REPO-012 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | docs/workflow.md | 6e41c4c131746130b0ffe731bb32864af01a69a6 | Not recorded | Not stated |
| SRC-REPO-013 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | docs/ai-collaboration-guide.md | 9484aa6d8e76d236bf21a1e1d2419288696821cb | Not recorded | Not stated |
| SRC-REPO-014 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | shared/core/principles.md | 179d93fde41e496b48d3cbde5d1d0362d39078e7 | Not recorded | Not stated |
| SRC-REPO-015 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | shared/core/constraints.md | d73d7b8f5928389c517a867a2b0d6cb3c43956af | Not recorded | Not stated |
| SRC-REPO-016 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | hap-aicc/data/manifest.json | e8c81d9fda6c1ed895f3675d7aa3da4243b09b3f | Not recorded | Not stated |
| SRC-REPO-017 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | hap-aicc/data/usage-log.json | 0cb1ef2a110b2b24272054ecce61af0a434f757a | Not recorded | Not stated |
| SRC-REPO-018 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | hap-aicc/app.js | 04266b0d545b8ae290d61e0359079d772eb12720 | Not recorded | Not stated |
| SRC-REPO-019 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | api/mcp.js | 223db517d88dc8baba9302779e570ac68a6d9e57 | Not recorded | Not stated |
| SRC-REPO-020 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | MCP_API.md | 5bf9718558c60444b94f3c8ff5af0a8a8c51f8ff | Not recorded | Not stated |
| SRC-REPO-021 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | config/workflow-rules.json | be88744d793deca69ba50458ede371e7870c67a8 | Not recorded | Not stated |
| SRC-REPO-022 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | config/repo-policy.json | 0c85eafabbc485896f6966841ee172c23cc61b8d | Not recorded | Not stated |
| SRC-REPO-023 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | data/schema/memory-schema.json | c979adc1126a4bb9617e3eef8ae2f2c45280da25 | Not recorded | Not stated |
| SRC-REPO-024 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | data/schema/queue-schema.json | e9ca01c57ee1c1c15b44106690189d49d6998978 | Not recorded | Not stated |
| SRC-REPO-025 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | data/schema/approval-schema.json | fa461664844d028eac884a92b00bdfb63781b145 | Not recorded | Not stated |
| SRC-REPO-026 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | logs/audit/event-log.jsonl | b9c1d68da28a9210a6899cf936439fe3d9c16f98 | Not recorded | Not stated |
| SRC-REPO-027 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | logs/mcp-audit.jsonl | 4c186fdd730407f53694c77219aa929910261736 | Not recorded | Not stated |
| SRC-REPO-028 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | logs/task-tracking.md | a2e9b69b75ae81b54873d1790151e04a5654eebf | Not recorded | Not stated |
| SRC-REPO-029 | REPOSITORY_OBSERVED | 0816155422/project-workflow-manual | reconstruction/operating-work-lifecycle-state | 05_Operational/Handoffs/.gitkeep | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | Not recorded | Not stated |
| SRC-IRIS-001 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/runtime/controller.py | 194c81e48dadf5f89a6c5e14731b5288b86164f8 | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-002 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/runtime/database.py | c3937168f3904b804948c7a090ffd8f7f43cd11c | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-003 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/runtime/mcp_server.py | e8851bb16101245f05eace2ead1e82868ef0c919 | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-004 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/runtime/main.py | 7a883223a0f5dcccf3c9fa45800ae628e6e032dc | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-005 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/runtime/model.py | 92beff61b7f113a6395ae38712c529bad252da13 | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-006 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/docs/IRIS_PLUGIN_STRUCTURE.md | ef61207e04049b0c7eaabe950718af5121668dc7 | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-007 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md | d5322ead6eecddac1a5ebecc57553195bbced48e | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |
| SRC-IRIS-008 | SOURCE_CODE_OBSERVED | Prasong1993/Prasong | main | IRIS/iris-controller-v0.6.5/README.md | 1aef014fbeda4e1c98241d0c5da4f43d34a6532e | ebf66dc13e9366fc9e47b6af2206d457cfbd32be | Not stated |

## User Conversation Provenance

The source register contains three conversation-origin entries:
- `SRC-USER-001`: prior conversation dated 2026-11-07; exact transcript locator UNKNOWN.
- `SRC-USER-002`: prior conversation dated 2026-11-01; exact transcript locator UNKNOWN.
- `SRC-USER-003`: current/prior task input dated 2026-11-08; user-supplied in conversation, exact transcript not committed.

These entries are labeled as user-confirmed in the existing register. The corresponding source conversations are not available as repository files in the recorded source register. No transcript location was invented.

## External Source-Code Provenance

The source register records eight source-code observations from:
- Repository: `Prasong1993/Prasong`
- Branch: `main`
- Commit: `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`
- Paths include the IRIS Controller v0.6.5 runtime files, plugin structure documentation, five-step execution contract, and README.
- Each source record includes a repository path and blob SHA in the source register.

These are provenance references recorded by the source register. This task did not independently re-fetch all eight external files.

## Raw Research Source Provenance

Path: `raw_data/openai_research/sources.jsonl`
Blob SHA: `7a49f33f626dce9f5089dc08594af54bae5ddff8`
Record count: 3

| Source ID | Title | Publish Date | Recorded Verification Status | Ingested At | Canonical Source URL |
|---|---|---|---|---|---|
| openai-deep-research-system-card | Deep research System Card | 2025-02-25 | Verified | 2026-10-28T10:13:00+07:00 | https://openai.com/index/deep-research-system-card/ |
| openai-trustworthy-third-party-evaluations | A shared playbook for trustworthy third party evaluations | 2026-05-29 | Verified | 2026-10-28T10:13:00+07:00 | https://openai.com/index/trustworthy-third-party-evaluations-foundations/ |
| openai-safety-overview-gpt-6-astra | Safety overview: GPT-6 Astra | 2026-09-03 | Verified | 2026-10-28T10:13:00+07:00 | https://openai.com/index/safety-overview-gpt-6-astra/ |

Related manifest:
- Path: `raw_data/openai_research/manifest.json`
- Blob SHA: `4dcb87527571d6527a7944696bf7a7bc7962b328`
- Records total_sources=3, total_verified=3, total_unverified=0.
- last_updated: 2026-10-28T10:13:00+07:00.
- The manifest says verification consisted of matching URL, title, publication date, and short excerpt against the official OpenAI page at ingestion time. It explicitly does not claim independent replication of source claims.

## Repository State / Checkpoint Provenance

| Artifact | Recorded Identity / Evidence | Current Blob SHA |
|---|---|---|
| `state/session-state.json` | Includes updatedAt, prior run references, evidence_ref paths, commit SHAs, checkpoint references, and explicit unresolved source locators | `97ce775fcbbac4a63f18fb16968a1626246319ab` |
| `state/last-run.json` | Records workflow run IDs, workflow names, commit SHAs, and notes limiting what each run proves | `6ce48035e082968f0752b0a85c95a8eb7b8ade6f` |
| `state/checkpoints/latest.json` | CKPT-20261108-011; includes timestamp, branch, evidence references, previous checkpoint, workflow run ID, commit, and read-back status fields | `104e0121f73e3568acd883e573490e6534edcdd5` |
| `logs/operation-log.md` | Append-only operational entries with dates, actor/system identity, evidence commits, and source-of-evidence statements | `27ff2ef9805ba3f2e054ad8551efd3c6aef78847` |
| `logs/workflow-evidence.md` | Append-only run evidence with timestamp, actor, workflow, run ID, commit SHA, URL, observed result, and evidence source | `83f00489995ced230d58e9b0c7f0eaf5d524063e` |
| `logs/task-tracking.md` | Task records with status, updated_at, actor/system identity, evidence, source of evidence, next step, and blocker | `a2e9b69b75ae81b54873d1790151e04a5654eebf` |

### Existing workflow provenance example

The latest checkpoint record `CKPT-20261108-011` records:
- GitHub Actions run ID: `42414689846`
- Workflow conclusion: `success`
- Tested commit SHA: `cce74615a7454618f861c0358f81578c33c0d278`
- 13 tests passed, 0 failed, as stated by the checkpoint evidence.
- The same checkpoint states that live platform integration and durable Raw Database integration remain blocked.
- It also records no merge to main and no canonical promotion.

This is a historical checkpoint assertion with linked evidence references; it is not a claim that this task independently reran those tests.

## Approval / Evidence Rules

- `docs/reporting-rules.md` states reports must be append-only and require evidence sources, repository/branch, and timestamps.
- `docs/checklists/reporting-rules.md` requires direct evidence links, run IDs and commit SHAs, and separate statuses for repository, workflow, deployment, sync, approval, and security.
- `templates/approval-gate.md` requires source provenance and evidence, validation run URL, content review, approving identity, approval decision, timestamp, and next step.
- `logs/approval-log.md` contains only an entry template and explicitly states: "No approval entries are recorded by this template itself."

## Provenance Gaps Preserved

1. Exact transcript locators for the three user conversation source entries are UNKNOWN.
2. The source register's recorded branch HEAD `502d8c78411b179f2e39195b5231d8921c249aba` is not the current branch HEAD `bb608e9cac1e33d7959e1c813b0f9c21c8871587` observed in this task.
3. The source register contains repository file blob references from its own recorded snapshot; this task did not independently re-verify every referenced blob.
4. The eight external IRIS source-code records are referenced to a specific source repository branch and commit, but were not all re-fetched during this task.
5. The approval log has no approval entries.
6. The raw research manifest's "Verified" status is scoped to source metadata matching at ingestion, not independent validation of every underlying claim.
7. Some state/log records refer to historical run IDs and commit SHAs; they are retained as historical provenance, not interpreted as current runtime status.

## Scope Boundary
This task discovered existing provenance records, source locators, recorded hashes, commit/run references, timestamps, actors, and explicit provenance gaps. No source was rewritten, approved, promoted, or independently re-verified beyond the direct read-backs stated above. No missing locator or provenance link was invented.

## Task Closure
- TASK-011: COMPLETE
- Snapshot: PERSISTED
- Read-back: PENDING
- TASK-012: NOT STARTED
- WORKSPACE: EMPTY
