# IRIS/SMPE State/Status — Evidence Confidence (Draft)

> Record type: user-provided candidate inventory; not a canonical registry.  
> Provenance: current conversation context + user-confirmed IRIS rules.  
> Hash status: `[NOT_HASHABLE]` — no single source artifact for this compiled table.  
> Verification requirement: compare against the original Source Registry, source/runtime artifacts, Runtime Evidence, and Hash Catalog before promoting this document to a canonical or high-confidence registry.

## Purpose and interpretation

**Evidence Confidence** is an assessment of how strongly the available evidence supports the record. It is separate from the State/Status value and separate from the evidence-status/provenance label. For example, `USER_CONFIRMED` describes the evidence/provenance class; `สูง` is the supplied confidence assessment. A confidence label does not by itself prove that an item is currently implemented or used at runtime.

The values below reproduce the user's supplied assessment. They have not been independently validated against the original IRIS/SMPE source or runtime artifacts.

## Candidate State/Status inventory

| State / Status | Namespace | หลักฐาน | สถานะหลักฐาน | ความน่าเชื่อถือ |
|---|---|---|---|---|
| TRANSFER | Runtime | มี state diagram v0.3.1 | USER_CONFIRMED / HISTORICAL | สูง |
| WAIT_TARGET | Runtime | มี state diagram v0.3.1 | USER_CONFIRMED / HISTORICAL | สูง |
| SEND | Runtime | มี state diagram v0.3.1 | USER_CONFIRMED / HISTORICAL | สูง |
| WAIT_COPY | Runtime | มี state diagram v0.3.1 | USER_CONFIRMED / HISTORICAL | สูง |
| STOPPED | Runtime | มี guard behavior ระบุไว้ | USER_CONFIRMED / HISTORICAL | สูง |
| PASS | Verification | พบใน Test Oracle | OBSERVED | กลาง |
| PASSED | Verification | พบใน Gate Reports | OBSERVED | กลาง |
| FAIL | Verification | พบใน Test Oracle | OBSERVED | กลาง |
| BLOCKED | Verification | พบใน Runtime Gate Design | OBSERVED | กลาง |
| NOT_CHECKED | Verification | แนวคิดสถาปัตยกรรม | USER_DEFINED | กลาง |
| VERIFIED | Verification | พบในหลาย Contract | USER_DEFINED | กลาง |
| UNKNOWN | Verification | พบหลายบริบท | OBSERVED | กลาง |
| NOT_TESTED | Verification | พบใน Test State | OBSERVED | กลาง |
| NOT_YET_PROVEN | Verification | พบใน Test State | OBSERVED | กลาง |
| PARTIALLY_OBSERVED | Verification | พบใน Test State | OBSERVED | กลาง |
| OBSERVED | Verification | พบใน Test State | OBSERVED | กลาง |
| RUNTIME_UNPROVEN | Verification | ใช้งานจริงหลายครั้งในบริบท IRIS | USER_CONFIRMED | สูง |
| RUNTIME_TEST_PENDING | Verification | ใช้กับ v0.3.1 | USER_CONFIRMED | สูง |
| SOURCE_VERIFIED | Evidence | Discovery Reports | OBSERVED | กลาง |
| TOOL_VERIFIED | Evidence | Discovery Reports | OBSERVED | กลาง |
| USER_SUPPLIED | Evidence | Discovery Reports | OBSERVED | กลาง |
| USER_DECLARED | Evidence | User Rule | USER_DEFINED | สูง |
| USER_CONFIRMED | Evidence | User Rule | USER_DEFINED | สูง |
| AI_STATIC_CHECK | Evidence | User Verification Model | USER_DEFINED | สูง |
| AI_RUNTIME_CHECK | Evidence | User Verification Model | USER_DEFINED | สูง |
| NOT_VERIFIED | Evidence | Discovery Reports | OBSERVED | กลาง |
| HISTORICAL_EVIDENCE | Evidence | Reconstruction Reports | OBSERVED | กลาง |
| QUOTED | Provenance | Recovery Rules | USER_CONFIRMED | สูง |
| DERIVED | Provenance | Recovery Rules | USER_CONFIRMED | สูง |
| HALLUCINATION | Provenance | Recovery Rules | USER_CONFIRMED | สูง |
| ORIGINAL | Recovery | Recovery Model | USER_CONFIRMED | สูง |
| HISTORICAL | Recovery | Recovery Model | USER_CONFIRMED | สูง |
| RECONSTRUCTION | Recovery | Recovery Model | USER_CONFIRMED | สูง |
| RECONSTRUCTION-SPEC | Recovery | Recovery Package | USER_CONFIRMED | สูง |
| PROPOSAL | Governance | Governance Rules | USER_DEFINED | สูง |
| ACCEPTED_DECISION | Governance | Governance Rules | USER_DEFINED | สูง |
| VERIFIED_IMPLEMENTATION | Governance | Governance Rules | USER_DEFINED | สูง |
| HAVE_BODY | Recovery Audit | Artifact Audit | USER_CONFIRMED | สูง |
| NAME_ONLY | Recovery Audit | Artifact Audit | USER_CONFIRMED | สูง |
| NOT_HAVE | Recovery Audit | Artifact Audit | USER_CONFIRMED | สูง |
| NOT_RECOVERED | Recovery Audit | Artifact Audit | USER_CONFIRMED | สูง |
| NOT_FOUND | Recovery Audit | Recovery Rules | USER_DEFINED | กลาง |
| NOT_FOUND_IN_INSPECTED_SCOPE | Recovery Audit | Source Inspection | OBSERVED | กลาง |
| NOT_INITIALIZED | Capability | Failure Pattern Rule | USER_CONFIRMED | สูง |
| NOT_ACCESSIBLE | Capability | Failure Pattern Rule | USER_CONFIRMED | สูง |
| NOT_SUPPORTED | Capability | Failure Pattern Rule | USER_CONFIRMED | สูง |
| FAILED | Work Cycle | Work Cycle Step 10 | USER_CONFIRMED | สูง |
| VERIFIED_OUTPUT | Work Cycle | Work Cycle Step 8 | USER_CONFIRMED | สูง |

## Evidence Confidence criteria

| ระดับ | ความหมาย |
|---|---|
| สูงมาก | มี Source Body จริง + Runtime Evidence + User Confirmation |
| สูง | ผู้ใช้ยืนยันโดยตรง หรือเป็นกฎ/คอนแทรกต์ที่ประกาศใช้อย่างชัดเจน |
| กลาง | พบในรายงาน, การวิเคราะห์, Discovery หรือ Historical Record แต่ยังไม่มี Source Body ต้นทางในมือ |
| ต่ำ | อนุมานจากความสัมพันธ์หรือจากเอกสารรอง |
| ต่ำมาก | Proposal หรือสมมติฐานที่ยังไม่มีหลักฐานรองรับ |

## ข้อสังเกตที่ต้องคงไว้

- Runtime states `TRANSFER`, `WAIT_TARGET`, `SEND`, `WAIT_COPY`, and `STOPPED` are assessed as **สูง**, not **สูงมาก**, because the supplied basis is historical evidence and user confirmation, without current runtime evidence in hand.
- `RUNTIME_UNPROVEN` is assessed as **สูง** for the claim that the term was used in the IRIS context; this does not prove that the runtime itself has been verified.
- No entry in this supplied table reaches **สูงมาก** because a source registry/source body, current runtime evidence, and hash confirmation are not all available together in this context.
- Do not collapse namespaces into one enum or infer a state machine from this inventory.
- Confidence describes support for the recorded claim; it is not an authorization to write to production, change runtime behavior, or treat a draft as canonical.
- When later evidence changes an assessment, add a new dated revision/decision record referencing this inventory. Do not silently overwrite this historical assessment.

## Required verification before promotion

Before any item or the inventory is labeled canonical/high-confidence, record the exact artifact path, repository, branch or version, commit/hash, inspection scope, and test/run evidence. Inspect the artifact body; a filename, report, or user-provided description alone is not source/runtime verification. Keep static inspection separate from runtime testing, and retain the reviewer/approver and explicit decision.

## Record metadata

- Record class: draft candidate inventory
- Supplied by: user
- Supplied in: current conversation context
- Hashability: `[NOT_HASHABLE]`
- Canonical status: not established
- Next step: source/runtime/evidence comparison before promotion
