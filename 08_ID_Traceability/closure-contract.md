# Work Item, Workflow Cycle, and Project Closure

## Purpose

Connect registered IDs to completion and closure at the correct level in the existing workflow. This contract does not add a new workflow stage.

## Closure levels

Closure is recorded separately for:

- Work Item
- Workflow Cycle
- Project

A closure at one level does not automatically close another level.

**Cycle Complete does not mean Project Complete.**

## Work Item Closure

A Work Item may be marked CLOSED only when its own defined completion conditions are satisfied and its result is linked to the relevant registered IDs.

The closure record identifies the Work Item, its originating work form, scope, linked inputs/outputs, and the basis on which its own completion conditions were met.

## Workflow Cycle Closure

A Workflow Cycle may be marked CLOSED only against that cycle's defined completion conditions. Its closure is recorded against the Workflow Cycle ID and linked Work Item IDs.

Closing a cycle does not automatically close the Project or any other cycle.

## Project Closure

Project Closure is a separate decision recorded against the Project ID and the Project's own defined completion conditions. A completed cycle alone is not sufficient to mark the Project CLOSED.

## Failure and return behavior

- If a Work Item fails, return it to the work form where the failure occurred.
- If the failure is at the origin of the cycle, return to the first part of that cycle.
- Do not close a failed Work Item, Workflow Cycle, or Project.
- Preserve prior closure records when work is changed or reopened; represent the later state as a new record/version rather than erasing history.

## Closure states

- `OPEN`: the entity is not closed.
- `CLOSED`: its applicable completion conditions have been met and recorded.
- `RETURNED`: the work failed and has been returned to its originating work form or the first part of its cycle.

## Required closure record fields

- `entity_type`: WorkItem, WorkflowCycle, or Project.
- `entity_id`: the registered ID being closed.
- `work_form`
- `origin_ref`
- `scope`
- `input_refs`
- `output_refs`
- `completion_conditions`
- `closure_state`
- `closure_basis`
- `closed_at` (required only when CLOSED)
- `return_to` (required only when RETURNED)
- `related_ids`

The closure record stores the basis for the closure. It does not create a separate Audit activity. No closure record may be fabricated to make the repository appear complete.
