# IRIS Working-Branch Runtime

SQLite-backed five-step lifecycle with checkpoint resume, handoff packets, and MCP stdio entry point.

- Entry: create_work(work_id,title) or existing work ID.
- Step: CHECKING -> WORKING -> VERIFYING -> PASSED|FAILED.
- Failure: error + checkpoint + audit retained; resume points to same step.
- Pass: checkpoint retained; resume points to next step.
- Final: all five latest steps PASSED; VERIFIED -> DELIVERED.
- Mismatch: verification/error/checkpoint/audit retained; not delivered.
- Handoff: PENDING -> ACCEPTED by matching designated recipient; returns current resume position.
- Persistence: IRIS_DB_PATH; default iris_runtime/data/iris.db.
- MCP entry: python -m iris_runtime; actual host binding requires separate proof.

Recipient equality is not external identity authentication. SQLite durability is not proof of shared central storage. Raw Collection -> Atomization semantics are not inferred.
