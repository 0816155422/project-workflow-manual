import pytest
from workspace_lifecycle.models import SessionStatus, OutputStatus, OperationStatus
from workspace_lifecycle.packets import create_work_packet
from workspace_lifecycle.adapters.chatgpt import ChatGPTWorkspaceAdapter
from workspace_lifecycle.adapters.github import GitHubWorkspaceAdapter
from workspace_lifecycle.session import WorkspaceCoordinator
from workspace_lifecycle.handoff import create_handoff, accept_handoff
from workspace_lifecycle.persistence import PersistenceBoundary, MemoryPersistenceStore
from workspace_lifecycle.checkpoint import CheckpointBoundary, MemoryCheckpointStore
from workspace_lifecycle.resume import derive_resume
from workspace_lifecycle.transitions import transition

def packet(platform="chatgpt", scope=None, refs=None, target=None):
    scope=scope or ["docs/allowed.md","tests/test_workspace_lifecycle.py"]
    refs=refs or ["docs/allowed.md"]
    return create_work_packet(work_id="W-1",cycle_id="C-1",source_state_reference="state://before",
      parent_checkpoint_id="CKPT-20261108-010",target_platform=platform,target_workspace_reference=target,
      requested_action="inspect and return a scoped result",allowed_scope=scope,required_references=refs,
      expected_result_type="ResultPacket",persistence_policy="approval-required",
      checkpoint_policy="after-persist-readback",return_destination="iris://coordinator",created_by="test-actor")

def test_chatgpt_logical_session_and_closure():
    adapter=ChatGPTWorkspaceAdapter(); coordinator=WorkspaceCoordinator({"chatgpt":adapter})
    p=packet(); s=coordinator.open_session(p,"worker")
    assert s.status is SessionStatus.REFERENCES_RESOLVED
    assert coordinator.dispatch(s,p).operation_status is OperationStatus.SUCCESS
    rp=adapter.record_result_candidate(s,p,action_performed="summarize evidence",
      result_references=["docs/allowed.md"],proposed_resulting_state="state://after")
    assert coordinator.receive(s).operation_status is OperationStatus.SUCCESS
    assert rp.result_status is OutputStatus.OUTPUT_VALID
    transition(s,SessionStatus.PERSIST_PENDING); transition(s,SessionStatus.PERSISTED)
    transition(s,SessionStatus.CHECKPOINTED)
    assert coordinator.close(s,"CKPT-NEW").operation_status is OperationStatus.SUCCESS
    assert s.status is SessionStatus.CLOSED and s.active_references==[]
    assert "deletion is not supported" in adapter.close_session(s).error

class FakeGitHub:
    def __init__(self): self.files={}; self.head="abc123"; self.commits=0
    def get_repository(self,repo): return {"name":repo}
    def get_branch(self,repo,branch): return {"name":branch,"sha":self.head}
    def get_development_workspace(self,name): raise LookupError("not found")
    def get_file(self,repo,path,branch): return self.files[path]
    def put_file(self,repo,path,content,branch): self.files[path]=content; return {"path":path}
    def run_tests(self,repo,branch,command,paths): return {"passed":True,"command":command}
    def commit(self,repo,branch,message,paths):
        self.commits+=1; self.head=f"commit-{self.commits}"
        return {"commit_sha":self.head,"paths":paths}

def test_github_branch_scope_test_commit_and_result_packet():
    client=FakeGitHub(); scope=["docs/allowed.md","tests/test_workspace_lifecycle.py"]
    adapter=GitHubWorkspaceAdapter(client,repository="owner/repo",
      branch="reconstruction/operating-work-lifecycle-state",allowed_scope=scope,
      development_workspace="codespace-if-authorized")
    coordinator=WorkspaceCoordinator({"github":adapter}); p=packet("github",scope,["docs/allowed.md"])
    s=coordinator.open_session(p,"worker")
    assert adapter.branch_head=="abc123"
    assert coordinator.dispatch(s,p).operation_status is OperationStatus.SUCCESS
    adapter.write_file("docs/allowed.md","updated")
    assert adapter.read_file("docs/allowed.md")=="updated"
    assert adapter.run_tests("pytest -q",["tests/test_workspace_lifecycle.py"])["passed"]
    commit=adapter.commit("scoped commit",["docs/allowed.md"],request_id="commit-req-1")
    assert commit["commit_sha"]=="commit-1"
    with pytest.raises(FileExistsError):
        adapter.commit("scoped commit",["docs/allowed.md"],request_id="commit-req-1")
    rp=adapter.record_result_candidate(s,p,action_performed="modify, test, commit and read-back",
      result_references=["github://owner/repo/commit/commit-1"],modified_references=["docs/allowed.md"],
      test_results=[{"passed":True}],proposed_resulting_state="git://commit-1")
    assert coordinator.receive(s).operation_status is OperationStatus.SUCCESS
    assert s.result_reference==rp.result_packet_id
    with pytest.raises(FileExistsError):
        adapter.record_result_candidate(s,p,action_performed="duplicate")
    with pytest.raises(PermissionError): adapter.write_file("state/historical.json","bad")
    with pytest.raises(PermissionError): adapter.commit("bad",["state/checkpoints/old.json"],request_id="bad")
    with pytest.raises(ValueError):
        GitHubWorkspaceAdapter(client,repository="owner/repo",branch="main",allowed_scope=scope)

def test_handoff_target_and_scope_authorization():
    adapter=ChatGPTWorkspaceAdapter(); c=WorkspaceCoordinator({"chatgpt":adapter})
    p=packet(); s=c.open_session(p,"worker"); c.dispatch(s,p)
    adapter.record_result_candidate(s,p,action_performed="prepare handoff")
    c.receive(s)
    h=create_handoff(s,to_platform="github",to_workspace_reference="github://owner/repo/tree/work",
      required_references=["docs/allowed.md"],allowed_scope=["docs/allowed.md"],pending_action="edit allowed doc",
      return_contract="ResultPacket",checkpoint_reference="CKPT-010")
    with pytest.raises(PermissionError):
        accept_handoff(h,target_platform="github",target_workspace_reference="wrong",
          allowed_scope=["docs/allowed.md"],authority_check=lambda _:True)
    h.status=type(h.status).PENDING
    accepted=accept_handoff(h,target_platform="github",target_workspace_reference="github://owner/repo/tree/work",
      allowed_scope=["docs/allowed.md"],authority_check=lambda _:True)
    assert accepted.status.value=="ACCEPTED"

def test_checkpoint_readback_and_resume_are_non_executing():
    adapter=ChatGPTWorkspaceAdapter(); c=WorkspaceCoordinator({"chatgpt":adapter})
    p=packet(); s=c.open_session(p,"worker"); c.dispatch(s,p)
    rp=adapter.record_result_candidate(s,p,action_performed="produce output",proposed_resulting_state="state://after")
    c.receive(s); transition(s,SessionStatus.PERSIST_PENDING); transition(s,SessionStatus.PERSISTED)
    store=MemoryCheckpointStore(); boundary=CheckpointBoundary(store)
    record=boundary.create(checkpoint_id="CKPT-011",parent_checkpoint_id="CKPT-010",session=s,
      work_packet=p,result_packet=rp,state_before="state://before",state_after="state://after",continuation="next-work")
    assert store.get_current_pointer()=="CKPT-011" and record["parent_checkpoint_id"]=="CKPT-010"
    state=derive_resume(current_state_reference="state://after",pending_action="next-work",
      required_references=["docs/allowed.md"],target_platform="github",workspace_session_status="CHECKPOINTED",
      result_status="PERSISTED",cleanup_status="OPEN",references_resolved=True,persisted=True,checkpointed=True)
    assert state["resume_position"]=="CLOSE_SESSION"

def test_persistence_boundary_and_duplicate_protection():
    adapter=ChatGPTWorkspaceAdapter(); c=WorkspaceCoordinator({"chatgpt":adapter})
    p=packet(); s=c.open_session(p,"worker"); c.dispatch(s,p)
    rp=adapter.record_result_candidate(s,p,action_performed="valid output",created_references=["docs/allowed.md"])
    c.receive(s); store=MemoryPersistenceStore()
    boundary=PersistenceBoundary(store,authorization_check=lambda *_:True,readback_check=lambda *_:True)
    args=dict(work_id=p.work_id,workspace_session_id=s.workspace_session_id,result_packet=rp,
      current_state_reference=s.current_state_reference,parent_checkpoint_id=p.parent_checkpoint_id,
      allowed_scope=p.allowed_scope,target_location="approved://records",payload={"ref":"docs/allowed.md"})
    assert boundary.persist(**args)["status"]=="PERSISTED"
    with pytest.raises(FileExistsError): boundary.persist(**args)

def test_scope_violation_main_and_inaccessible_host():
    client=FakeGitHub(); adapter=GitHubWorkspaceAdapter(client,repository="owner/repo",
      branch="reconstruction/operating-work-lifecycle-state",allowed_scope=["docs/allowed.md"])
    with pytest.raises(PermissionError): adapter.read_file("docs/private.md")
    with pytest.raises(PermissionError):
        adapter.commit("bad",["state/checkpoints/old.json"],request_id="bad")
    with pytest.raises(ValueError):
        GitHubWorkspaceAdapter(client,repository="owner/repo",branch="main",allowed_scope=["*"])
    offline=GitHubWorkspaceAdapter(None,repository="owner/repo",
      branch="reconstruction/operating-work-lifecycle-state",allowed_scope=["docs/allowed.md"])
    assert offline.resolve_workspace(None).operation_status is OperationStatus.NOT_ACCESSIBLE

def test_duplicate_session_packet_and_invalid_transition():
    adapter=ChatGPTWorkspaceAdapter(); c=WorkspaceCoordinator({"chatgpt":adapter})
    p=packet(); s=c.open_session(p,"worker")
    with pytest.raises(FileExistsError): c.open_session(p,"worker")
    with pytest.raises(ValueError): transition(s,SessionStatus.CLOSED)

def test_cross_platform_handoff_chatgpt_github_chatgpt():
    chat=ChatGPTWorkspaceAdapter(); gh=GitHubWorkspaceAdapter(FakeGitHub(),repository="owner/repo",
      branch="reconstruction/operating-work-lifecycle-state",
      allowed_scope=["docs/allowed.md","tests/test_workspace_lifecycle.py"])
    coordinator=WorkspaceCoordinator({"chatgpt":chat,"github":gh})
    p1=packet("chatgpt",["docs/allowed.md","tests/test_workspace_lifecycle.py"])
    s1=coordinator.open_session(p1,"main-ai"); coordinator.dispatch(s1,p1)
    chat.record_result_candidate(s1,p1,action_performed="prepare scoped repository change")
    coordinator.receive(s1)
    handoff=create_handoff(s1,to_platform="github",
      to_workspace_reference="github://owner/repo/tree/reconstruction/operating-work-lifecycle-state",
      required_references=["docs/allowed.md"],allowed_scope=["docs/allowed.md"],
      pending_action="inspect and update one authorized file",return_contract="ResultPacket",
      checkpoint_reference="CKPT-010")
    accept_handoff(handoff,target_platform="github",
      target_workspace_reference=handoff.to_workspace_reference,
      allowed_scope=gh.allowed_scope,authority_check=lambda packet:packet.work_id=="W-1")
    p2=packet("github",["docs/allowed.md"],["docs/allowed.md"],handoff.to_workspace_reference)
    s2=coordinator.open_session(p2,"github-worker"); coordinator.dispatch(s2,p2)
    gh.write_file("docs/allowed.md","cross-platform result")
    gh.run_tests("pytest -q",["docs/allowed.md"])
    commit=gh.commit("cross-platform scoped commit",["docs/allowed.md"],request_id="cross-commit-1")
    gh.record_result_candidate(s2,p2,action_performed="write, test, commit, read-back",
      result_references=[commit["commit_sha"]],modified_references=["docs/allowed.md"],
      test_results=[{"passed":True}],proposed_resulting_state="git://"+commit["commit_sha"])
    assert coordinator.receive(s2).operation_status is OperationStatus.SUCCESS
    assert s2.result_reference is not None
    assert derive_resume(current_state_reference="git://"+commit["commit_sha"],
      pending_action=None,target_platform="chatgpt",workspace_session_status="RESULT_RECEIVED",
      result_status="OUTPUT_VALID",references_resolved=True)["resume_position"]=="STOP"
