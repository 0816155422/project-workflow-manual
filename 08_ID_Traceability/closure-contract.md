# Work and Cycle Closure Contract

## Purpose

Connect issued IDs to the completion and closure of work items in the existing workflow. This contract does not add a new workflow stage.

## Closure unit

A closure record applies to a specific identified work item or cycle. It does not implicitly close its parent, sibling items, or the whole project.

## Conditions to close a work item

A work item may be marked CLOSED only when all applicable conditions below are satisfied:

1. The work item has a registered, stable ID.
2. Its originating work form and scope are identified.
3. Its required inputs and outputs are linked by their existing IDs or source references.
4. Its defined completion conditions are satisfied.
5. The resulting content/version and content hash are recorded where applicable.
6. The saved result can be read back and matched to the recorded identity.
7. No required dependency for this work item remains open or blocked.

The closure record stores the basis for closure. It does not create a separate Audit activity.

## Failure and return behavior

- If a work item fails, return it to the work form where the failure occurred.
- If the failure is at the origin of the cycle, return to the first part of that cycle.
- Do not close a failed item.
- Do not mark a parent cycle or project CLOSED solely because one child item is CLOSED.

## Closure states

- `OPEN`: work is not closed.
- `CLOSED`: the applicable completion conditions have been met and recorded.
- `RETURNED`: work failed and has been returned to its originating work form or the first part of its cycle.

A later change to a CLOSED item must be represented as a new version/change record. Do not erase the prior closure event.

## Required closure record fields

- `work_id`
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

No closure record may be fabricated to make the repository appear complete.
