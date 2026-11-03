# IRIS Data Freshness and Merge Review

- Review date: 2026-11-04
- Review type: repository evidence review and cross-source consolidation
- Status: **PARTIALLY VERIFIED / CURRENT RUNTIME STATUS NOT VERIFIED**
- Target repository: `0816155422/project-workflow-manual`
- Target branch: `feature/init-gh-native-structure`
- Target branch HEAD observed: `f15cbc2e780f16475b0fcd02c071848e09f03ee3`
- Source repository: `Prasong1993/Prasong`
- Source branch: `main`
- Source HEAD observed: `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`
- Source HEAD commit date: `2026-10-27T13:57:55Z`

## 1. Scope and method

This review compares the current IRIS source tree and its v0.6.5 documentation with the existing target repository structure and workflow evidence. It preserves provenance and distinguishes source-code presence, historical test evidence, and target-host runtime evidence.

**Important:** The Python collector `IRIS_PROJECT_DATA_COLLECTION.py` was not present in the target branch tree and was not executed in this review. This document is an evidence-based review artifact, not a claimed output of that script. No missing collector output has been fabricated.

## 2. Current source inventory

The current source repository tree contains:
- `IRIS/iris-controller-v0.6.2/`
- `IRIS/iris-controller-v0.6.5/`

The current tree does not show an IRIS v0.7.4 directory. A v0.7.4 version reference from earlier user-provided collection notes is therefore **NOT VERIFIED against the current source tree**.

### v0.6.5 source files read

| File | Observed blob SHA | Review |
|---|---|---|
| `README.md` | `1aef014fbeda4e1c98241d0c5da4f43d34a6532e` | Current package description and changelog |
| `IRIS_VALIDATION_v0.6.5.md` | `8ab1d9fa2583d20a7dff68878f3f40454a6577e6` | Historical VM test record |
| `docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md` | `d5322ead6eecddac1a5ebecc57553195bbced48e` | Five-step gated contract |
| `docs/IRIS_PLUGIN_STRUCTURE.md` | `ef61207e04049b0c7eaabe950718af5121668dc7` | Older v0.6.3-labelled architecture note |
| `plugin.json` | `2f2e854017ab17e0548aa3ac333a84f087dcde6c` | Manifest version 0.6.5 |
| `skills/iris/SKILL.md` | `58828bc0cd8c565a08aa4320534362685f068790` | Runtime-required skill instructions |
| `runtime/requirements.txt` | `903eaab7371a4bd3719c9cb917f301b879725a9b` | Python dependencies |
| `.github/workflows/iris-v065-test.yml` | `a20eef08b961c606da87cef85004951ef72f8c75` | CI test workflow definition |

## 3. Consolidated architecture

The current v0.6.5 README and execution contract describe this flow:

`Agent Skill → MCP / REST execution boundary → Controller → SQLite state → Verification → Delivery`

Runtime components:
- Python runtime.
- FastAPI REST API in `runtime/main.py`.
- MCP stdio server in `runtime/mcp_server.py`.
- Shared workflow logic in `runtime/controller.py`.
- SQLite persistence in `runtime/database.py`.
- Step and status definitions in `runtime/model.py`.
- Expected-versus-actual verification helper in `runtime/verify.py`.
- Database location can be overridden with `IRIS_DB_PATH`; fallback documented as `runtime/data/iris.db`.

The seven MCP tools documented by the source README are:
`health`, `create_work`, `run_step`, `final_verify`, `get_work_status`, `add_evidence`, and `list_evidence`.

## 4. Merged five-step execution contract

The v0.6.5 README, skill, and five-step contract agree on the following ordered stages:

1. แนวคิด
2. ออกแบบ
3. ทำงานจริง
4. ส่งผล
5. ตรวจสอบบนพื้นที่ ChatGPT

Each step must follow `CHECK → DO → VERIFY`. The workflow must not advance unless the current step passes. Failures, errors, checkpoints, and audit records must be retained. Final delivery requires all five steps to pass and final expected-versus-actual verification to return `VERIFIED`, after which the work status may become `DELIVERED`.

## 5. Freshness and evidence assessment

| Item | Latest observed evidence | Freshness / status |
|---|---|---|
| Source repository HEAD | `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`, 2026-10-27 | Current source snapshot observed on 2026-11-04 |
| v0.6.5 package files | Read from source `main` | Present in current source tree |
| v0.6.5 historical validation | VM validation record dated 2026-10-08 | Historical evidence, not a fresh run |
| GitHub Actions test run | Run [37678194022](https://github.com/Prasong1993/Prasong/actions/runs/37678194022), success on SHA `fee44e82a0926ca85833beff8a9462156117a2d9`, 2026-10-07 | Successful historical run, but it does not test the current source HEAD |
| Earlier test attempts | Runs 37677886877 and 37677468237 failed | Retain as historical failures |
| Target-host MCP binding | Source validation document explicitly marks this unproven | NOT VERIFIED |
| Target-host Python dependency availability | Source validation document explicitly marks this unproven | NOT VERIFIED |
| Multi-user / concurrency isolation | Source validation document explicitly marks this unproven | NOT VERIFIED |
| v0.7.4 | Not present in current source tree inventory | NOT VERIFIED |
| Target repository collector script | Not found in target branch tree | BLOCKED for exact collector execution |
| Collector-generated Markdown | Not found in target branch tree | NOT VERIFIED; not created as a substitute |

## 6. Version and document conflicts

1. `IRIS_PLUGIN_STRUCTURE.md` is labelled v0.6.3 and describes an older `INSPECT → PLAN → EXECUTE → VERIFY → DELIVER` orchestration vocabulary.
2. The v0.6.5 README, skill, and five-step contract use the five named stages listed in Section 4.
3. These descriptions are not silently treated as identical. For this consolidation, the v0.6.5 README + v0.6.5 skill + v0.6.5 five-step contract are the aligned version-specific execution contract. The v0.6.3-labelled architecture note is retained as a legacy architecture reference pending owner review.
4. The validation record reports 23/23 tests and 19/19 MCP stdio E2E checks on 2026-10-08, but the most recent observed successful CI run is on 2026-10-07 and an older source SHA. Neither proves the current source HEAD or target-host binding.
5. A source commit after the recorded successful test run means the test evidence must not be presented as validation of the current source HEAD.

## 7. Target repository baseline and integration boundary

The target branch currently contains the GitHub-native workspace structure, project records, state files, and workflow logs. Its observed branch HEAD is `f15cbc2e780f16475b0fcd02c071848e09f03ee3`.

The target repository's existing project overview describes the repository as a document and coordination workspace, not a real-time database, and states that allowlist entries do not prove platform connection or automatic synchronization.

The existing state/checkpoint files still contain historical references to branch `main` and dates around 2026-10-28. Those historical records have not been rewritten by this review. The latest target-branch Actions runs observed were repository validation and CodeQL checks for commit `26e7de48575ee16a85dc2d3385cc66ade928e09e`, both successful on 2026-11-02; these are generic repository checks, not IRIS runtime tests.

## 8. Safe integration result

- Consolidated source architecture and five-step contract: **PARTIALLY VERIFIED** from current source files.
- v0.6.5 package version: **SOURCE VERIFIED** from manifest and source files.
- Current runtime test status on source HEAD: **NOT VERIFIED**.
- Actual target-host MCP connection: **NOT VERIFIED**.
- v0.7.4: **NOT VERIFIED**.
- Exact Python collector execution and its output: **BLOCKED** because the collector file was not found in the target branch and was not available to execute in this repository review.
- Target branch writes, commit, push, and PR: **NOT PERFORMED** as part of this review artifact.

## 9. Sources

- Source repository: https://github.com/Prasong1993/Prasong
- Current IRIS v0.6.5 directory: https://github.com/Prasong1993/Prasong/tree/main/IRIS/iris-controller-v0.6.5
- v0.6.5 README: https://github.com/Prasong1993/Prasong/blob/main/IRIS/iris-controller-v0.6.5/README.md
- v0.6.5 validation record: https://github.com/Prasong1993/Prasong/blob/main/IRIS/iris-controller-v0.6.5/IRIS_VALIDATION_v0.6.5.md
- Five-step contract: https://github.com/Prasong1993/Prasong/blob/main/IRIS/iris-controller-v0.6.5/docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md
- Legacy plugin structure note: https://github.com/Prasong1993/Prasong/blob/main/IRIS/iris-controller-v0.6.5/docs/IRIS_PLUGIN_STRUCTURE.md
- Successful historical CI run: https://github.com/Prasong1993/Prasong/actions/runs/37678194022
- Target repository branch: https://github.com/0816155422/project-workflow-manual/tree/feature/init-gh-native-structure
