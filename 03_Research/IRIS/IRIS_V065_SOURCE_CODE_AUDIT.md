# IRIS v0.6.5 Source Code Audit

- Review date: 2026-11-04
- Source repository: `Prasong1993/Prasong`
- Source branch: `main`
- Source HEAD observed: `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`
- Package: `IRIS/iris-controller-v0.6.5`
- Review status: **SOURCE INSPECTED / RUNTIME NOT EXECUTED**
- This is a source-code inspection, not a fresh test run.

## 1. Components inspected

| Component | Blob SHA |
|---|---|
| `.mcp.json` | `f4292ce99d12a9169c2921bba505123cc024bfa0` |
| `.codex-plugin/plugin.json` | `b68db556440fd59bc43f14b9ad4818eef49ab501` |
| `runtime/controller.py` | `194c81e48dadf5f89a6c5e14731b5288b86164f8` |
| `runtime/database.py` | `c3937168f3904b804948c7a090ffd8f7f43cd11c` |
| `runtime/main.py` | `7a883223a0f5dcccf3c9fa45800ae628e6e032dc` |
| `runtime/mcp_server.py` | `e8851bb16101245f05eace2ead1e82868ef0c919` |
| `runtime/model.py` | `92beff61b7f113a6395ae38712c529bad252da13` |
| `runtime/verify.py` | `6865448f4091bdeec9f4aab62f3b4ff12f2464c6` |
| `tests/test_api.py` | `7d060a16e5cf1f1ce36b0b3b423c49feaf4c2085` |
| `tests/test_controller.py` | `c7fcbfe2d9267b98d21a684c6e7a894da82e3d4e` |
| `tests/test_e2e_api.py` | `297c71677f554b59ac86a3a588edac1398e6be27` |
| `tests/test_mcp.py` | `855a963176e40ff6f4e1845f2bdeed777fecc959` |
| `tests/test_mcp_e2e.py` | `b3bf742a74610b6cc4fdef52862aab52ef3d8122` |

## 2. Confirmed implementation structure

- `controller.py` owns work creation, gated step execution, retry handling, error recording, checkpoint recording, and work status aggregation.
- `database.py` uses SQLite and creates seven tables: `evidence`, `work_units`, `step_runs`, `errors`, `checkpoints`, `verifications`, and `audit_log`.
- `main.py` exposes the REST API and applies the five-step gate before final verification.
- `mcp_server.py` exposes MCP tools and returns structured success/error payloads.
- `model.py` defines five ordered steps and a 22-section working-structure list.
- `verify.py` exposes a string-normalized equality helper. The controller currently implements its own `verify_pair` equality helper rather than importing this module.
- `.mcp.json` launches `python runtime/mcp_server.py` and sets `IRIS_DB_PATH` to `${PLUGIN_DATA}/iris.db`.

## 3. Confirmed five-step model

1. แนวคิด: input `evidence/source`; output `goal_and_conditions`.
2. ออกแบบ: input `verified_step_1`; output `actionable_design`.
3. ทำงานจริง: input `verified_step_2`; output `actual_result`.
4. ส่งผล: input `verified_step_3`; output `verified_delivery`.
5. ตรวจสอบบนพื้นที่ ChatGPT: input `delivered_step_4`; output `chatgpt_workspace_verified`.

The controller checks that the previous step's latest run is PASSED before allowing the next step. Step execution records checking/working/verifying/pass or failure states. A mismatch is not promoted to PASSED; attempts are bounded by `max_attempts`.

## 4. Persistence and verification behavior

- Work creation writes a work row and audit event.
- Each step run writes a step-run record and audit event.
- Failed attempts write an error record and checkpoint.
- Successful attempts write a PASSED step-run record and checkpoint.
- Final verification requires the latest record for each of the five steps to be PASSED.
- MCP final mismatch writes a verification row and audit event, then records an error and checkpoint, and returns `FINAL_MISMATCH`; it does not mark the work DELIVERED.
- REST final mismatch writes a verification row and audit event and does not mark the work DELIVERED. The inspected REST implementation does not call the error/checkpoint recording functions for this final mismatch. This differs from the MCP implementation's richer mismatch retention.

## 5. Discrepancies requiring owner review

### 5.1 Codex manifest metadata mismatch

The inspected `.codex-plugin/plugin.json` declares version `0.6.5`, but its `homepage` still points to the v0.6.2 directory. Its visible manifest content also does not include an `mcpServers` field, while the root `plugin.json` does include `mcpServers: "./.mcp.json"`. The package includes a separate `.mcp.json`, but whether the target host discovers and launches it must be proven on that host.

Status: **SOURCE VERIFIED DISCREPANCY / HOST EFFECT NOT VERIFIED**.

### 5.2 REST and MCP final mismatch parity

The README and validation record emphasize that MCP final mismatch persistence was fixed. Source inspection confirms MCP stores mismatch in verification, audit, errors, and checkpoints. The REST path stores verification and audit records but does not add a corresponding error/checkpoint record for the final mismatch.

Status: **SOURCE VERIFIED BEHAVIOR DIFFERENCE**. Do not describe the two paths as identical for final-mismatch retention without a code change and fresh tests.

### 5.3 Verification helper duplication

`runtime/verify.py` defines `matches()`, while `controller.py` defines and uses `verify_pair()`. Both perform stripped string equality. The helper module appears unused in the inspected runtime imports.

Status: **OBSERVED / CLEANUP DECISION NOT MADE**.

### 5.4 Architecture document version label

`docs/IRIS_PLUGIN_STRUCTURE.md` is labelled v0.6.3 while it resides inside the v0.6.5 package. Its older orchestration vocabulary should remain a legacy reference until the owner decides whether to update it.

Status: **SOURCE VERIFIED VERSION-LABEL CONFLICT**.

## 6. Test evidence boundaries

The repository contains REST, controller, MCP tool, and E2E test files. The validation record reports historical execution results. The GitHub Actions run observed in the source repository succeeded on commit `fee44e82a0926ca85833beff8a9462156117a2d9` on 2026-10-07.

The current source HEAD observed during this review is `ebf66dc13e9366fc9e47b6af2206d457cfbd32be`. No test run against that current HEAD was executed in this review. Therefore:
- Source files present: **VERIFIED**.
- Historical test report present: **VERIFIED AS A DOCUMENT**.
- Current HEAD test pass: **NOT VERIFIED**.
- Target-host MCP binding: **NOT VERIFIED**.
- Multi-user/concurrency behavior: **NOT VERIFIED**.

## 7. Integration decision

This audit can be used as supplemental evidence alongside `IRIS_DATA_FRESHNESS_AND_MERGE_REVIEW.md`. It must not be mistaken for output from `IRIS_PROJECT_DATA_COLLECTION.py`. The exact user-provided collector was not available in the active execution context, so it was not run and no generated collector output is claimed.

No source code was changed. No target-host installation or runtime execution was performed. No merge into `main` was performed.
