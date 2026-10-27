# Shared Core Decision Log

Record durable decisions affecting repository architecture.

## Entry template
- Date (UTC):
- Decision:
- Context:
- Alternatives:
- Consequences:
- Source/PR/commit:

## Current decisions
- GitHub Pages is a read-only static interface.
- GitHub Actions is the controlled write-back mechanism.
- Approved shared memory lives under `shared/`.
- Promotion from `pending/` requires explicit human approval.
- Existing approved files are not overwritten by the sync workflow.