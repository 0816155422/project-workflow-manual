---
name: iris-step1
version: 0.1.0
status: draft
description: Controlled execution, validation, and evidence auditing for IRIS Step 1 tasks.
---

# IRIS Step 1 — Workflow Skill

> **Status: DRAFT — NOT WIRED TO RUNTIME**

## Purpose

Define a controlled workflow for carrying out IRIS Step 1 tasks, validating results, and recording evidence. This file is a version-controlled workflow definition only; it does not itself deploy, execute, or connect the IRIS runtime.

## Operating rules

1. Inspect the relevant source files, runtime contracts, dependencies, and existing tests before making changes.
2. Establish the requested outcome, scope, constraints, and acceptance criteria before acting.
3. Prefer the smallest bounded change that satisfies the task. Do not expand scope without a clear requirement.
4. Validate inputs and dependencies, and check applicable policy and permission boundaries before execution.
5. Keep evidence traceable to the exact source, command, test, or observation that supports each conclusion.
6. Distinguish verified facts from assumptions, inference, missing evidence, and unverified claims.
7. Do not report a task as passed, persisted, deployed, or integrated unless the corresponding result has been directly verified.
8. If an operation fails or access is unavailable, record the error and stop rather than implying success.

## Work-unit lifecycle

1. **Inspect** — identify the relevant files, interfaces, dependencies, state, and current behavior.
2. **Plan** — define the intended change, affected components, risks, and verification criteria.
3. **Validate** — check source inputs, dependencies, policy constraints, and permissions.
4. **Execute** — make only the bounded, authorized change.
5. **Verify** — run applicable syntax, unit, integration, persistence, policy, and runtime checks. Report only checks actually performed.
6. **Audit** — record evidence, versions, errors, limitations, and unresolved uncertainty.
7. **Report** — summarize the change, verification outcomes, and any remaining work.

## Required work record

For each work unit, record where applicable:

- Work-unit identifier and objective
- Source paths and version or commit reference
- Planned change and affected components
- Commands or tests actually executed
- Results and evidence references
- Errors, skipped checks, assumptions, and unresolved risks
- Final status: `verified`, `failed`, or `blocked`

Use stable, unique identifiers for work units and evidence records when the host system provides an identifier scheme. Do not invent identifiers that appear to be issued by an external system.

## Verification policy

- **Syntax:** validate changed files with the appropriate parser or compiler.
- **Persistence:** read back persisted data and compare it with the intended result.
- **Policy:** confirm that the change respects applicable policy and permission boundaries.
- **Runtime:** execute relevant tests or checks in the actual target environment where available.
- **Evidence:** retain the exact outputs or references needed to support the reported status.

If a verification category cannot be run, mark it as not verified and state why.

## Expected output

Provide a concise report containing:

- Objective and scope
- Files or components changed
- Checks performed and their actual outcomes
- Evidence and version references
- Errors, limitations, and unresolved questions
- Final status and recommended next step

## Integration gate

Do not import this draft into Configuration Core, Target Registry, adapters, serializer registries, or exporter bridges until a separately reviewed integration contract defines:

- Plugin host and manifest schema
- Tool/API interfaces and permission model
- Input, output, and error schemas
- Identity and evidence identifier rules
- Persistence and audit requirements
- Test harness, compatibility expectations, and release versioning

The existence of this file alone does not establish runtime integration or operational readiness.
