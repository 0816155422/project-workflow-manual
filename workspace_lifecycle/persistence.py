"""Persistence gate. No adapter or worker receives direct Raw Database access."""
from .models import OutputStatus

class PersistenceBoundary:
    REQUIRED=("work_id","workspace_session_id","current_state_reference",
              "parent_checkpoint_id","allowed_scope","target_location")
    def __init__(self, store, *, authorization_check, readback_check,
                 state_precondition_check, target_location_check, historical_protection_check):
        self.store=store
        self.authorization_check=authorization_check
        self.readback_check=readback_check
        self.state_precondition_check=state_precondition_check
        self.target_location_check=target_location_check
        self.historical_protection_check=historical_protection_check
        self.persisted={}
    def persist(self, *, work_id, workspace_session_id, result_packet, current_state_reference,
                parent_checkpoint_id, allowed_scope, target_location, payload):
        values=locals()
        missing=[k for k in self.REQUIRED if values.get(k) in (None,"",[])]
        if missing: raise ValueError("missing persistence fields: "+", ".join(missing))
        if result_packet.work_id!=work_id or result_packet.workspace_session_id!=workspace_session_id:
            raise PermissionError("work/session identity mismatch")
        if not result_packet.result_packet_id:
            raise PermissionError("Result Packet identity missing")
        if result_packet.result_status not in (OutputStatus.OUTPUT_VALID,OutputStatus.PERSIST_PENDING):
            raise PermissionError("only validated output may be persisted")
        touched=set(result_packet.created_references)|set(result_packet.modified_references)
        if not touched.issubset(set(allowed_scope)):
            raise PermissionError("result exceeds Allowed Scope")
        if not self.state_precondition_check(current_state_reference,parent_checkpoint_id):
            raise PermissionError("current state or parent checkpoint precondition failed")
        if not self.target_location_check(target_location,allowed_scope):
            raise PermissionError("target location is not authorized by scope")
        if not self.historical_protection_check(target_location):
            raise PermissionError("historical record protection check failed")
        if not self.authorization_check(result_packet,target_location,allowed_scope):
            raise PermissionError("persistence authorization denied")
        key=(work_id,result_packet.result_packet_id,target_location)
        if key in self.persisted or self.store.exists(key):
            raise FileExistsError("duplicate persistence blocked")
        record={"work_id":work_id,"workspace_session_id":workspace_session_id,
          "result_packet_id":result_packet.result_packet_id,"current_state_reference":current_state_reference,
          "parent_checkpoint_id":parent_checkpoint_id,"target_location":target_location,
          "payload":payload,"result_references":list(result_packet.result_references)}
        self.store.write(key,record)
        readback=self.store.read(key)
        if readback!=record or not self.readback_check(key,record,readback):
            raise IOError("persistence read-back failed")
        self.persisted[key]=record
        return {"status":"PERSISTED","key":key,"record":record}

class MemoryPersistenceStore:
    """Test-only store. Not a Raw Database implementation."""
    def __init__(self): self.records={}
    def exists(self,key): return key in self.records
    def write(self,key,record):
        if key in self.records: raise FileExistsError(key)
        self.records[key]=dict(record)
    def read(self,key): return dict(self.records[key])
