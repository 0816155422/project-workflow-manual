"""Checkpoint creation with immutable records and pointer-after-readback ordering."""
from copy import deepcopy
class CheckpointBoundary:
    def __init__(self, store): self.store=store
    def create(self, *, checkpoint_id, parent_checkpoint_id, session, work_packet, result_packet,
               state_before, state_after, continuation):
        record={"checkpoint_id":checkpoint_id,"parent_checkpoint_id":parent_checkpoint_id,
          "workspace_session":session.workspace_session_id,"work_packet_id":work_packet.packet_id,
          "result_packet_id":result_packet.result_packet_id,"state_before":state_before,
          "state_after":state_after,"continuation":continuation,"immutable":True}
        if self.store.exists(checkpoint_id): raise FileExistsError("checkpoint IDs are immutable and unique")
        self.store.write_checkpoint(checkpoint_id,record)
        readback=self.store.read_checkpoint(checkpoint_id)
        if readback!=record: raise IOError("checkpoint read-back mismatch")
        self.store.update_current_pointer(checkpoint_id)
        if self.store.get_current_pointer()!=checkpoint_id: raise IOError("current pointer read-back mismatch")
        return record

class MemoryCheckpointStore:
    """Test-only checkpoint store; not a project Raw Database."""
    def __init__(self): self.records={}; self.pointer=None
    def exists(self,key): return key in self.records
    def write_checkpoint(self,key,value):
        if key in self.records: raise FileExistsError(key)
        self.records[key]=deepcopy(value)
    def read_checkpoint(self,key): return deepcopy(self.records[key])
    def update_current_pointer(self,key):
        if key not in self.records: raise KeyError(key)
        self.pointer=key
    def get_current_pointer(self): return self.pointer
