"""GitHub workspace adapter over an injected, permission-scoped host client.

No credentials are embedded and Codespaces are never created automatically.
"""
from fnmatch import fnmatch
from ..models import AdapterResult, OperationStatus, OutputStatus, new_id
from ..packets import create_result_packet

class GitHubWorkspaceAdapter:
    adapter_id = "github-workspace-adapter-v1"
    platform = "github"

    def __init__(self, client=None, *, repository, branch, allowed_scope, development_workspace=None):
        if not repository or not branch:
            raise ValueError("repository and working branch are required")
        if branch == "main":
            raise ValueError("main is never an allowed workspace branch")
        self.client = client
        self.repository = repository
        self.branch = branch
        self.allowed_scope = tuple(allowed_scope)
        self.development_workspace = development_workspace
        self.sessions = {}
        self.branch_head = None
        self.commit_requests = {}

    def _result(self, op, status, ref=None, error=None, external=None):
        return AdapterResult(self.adapter_id, self.platform, ref, op, status,
                             external_reference=external, error=error)

    def _in_scope(self, path):
        return any(path == p or fnmatch(path, p) for p in self.allowed_scope)

    def _require_client(self):
        if self.client is None:
            raise RuntimeError("authorized GitHub host client is not connected")

    def resolve_workspace(self, reference):
        if self.client is None:
            return self._result("resolve_workspace", OperationStatus.NOT_ACCESSIBLE,
                                reference, "No authorized GitHub host client supplied.")
        try:
            self.client.get_repository(self.repository)
            branch = self.client.get_branch(self.repository, self.branch)
            self.branch_head = branch.get("sha")
            dev = None
            if self.development_workspace:
                try:
                    dev = self.client.get_development_workspace(self.development_workspace)
                except (NotImplementedError, PermissionError, LookupError):
                    dev = None
            return self._result("resolve_workspace", OperationStatus.SUCCESS,
                reference or f"github://{self.repository}/tree/{self.branch}",
                error="Development workspace unavailable or inaccessible; repository working branch selected." if not dev else None,
                external=self.branch_head)
        except LookupError as exc:
            return self._result("resolve_workspace", OperationStatus.NOT_FOUND, reference, str(exc))
        except PermissionError as exc:
            return self._result("resolve_workspace", OperationStatus.NOT_ACCESSIBLE, reference, str(exc))
        except Exception as exc:
            return self._result("resolve_workspace", OperationStatus.UNKNOWN, reference, str(exc))

    def create_session(self, packet):
        if packet.target_platform != "github":
            return self._result("create_session", OperationStatus.BLOCKED, error="Target platform mismatch.")
        if not set(packet.allowed_scope).issubset(set(self.allowed_scope)):
            return self._result("create_session", OperationStatus.BLOCKED, error="Packet scope exceeds adapter scope.")
        sid = new_id("WSS")
        self.sessions[sid] = {"packet": packet, "status": "CREATED", "result": None}
        return self._result("create_session", OperationStatus.SUCCESS,
            f"github://{self.repository}/tree/{self.branch}", external=sid)

    def dispatch_work(self, session, packet):
        record = self.sessions.get(session.workspace_session_id)
        if record is None:
            return self._result("dispatch_work", OperationStatus.NOT_FOUND, session.workspace_reference)
        if packet.allowed_scope != record["packet"].allowed_scope:
            return self._result("dispatch_work", OperationStatus.BLOCKED, session.workspace_reference, "Scope mismatch.")
        record["status"] = "ACTIVE"
        return self._result("dispatch_work", OperationStatus.SUCCESS, session.workspace_reference,
                            external=session.workspace_session_id)

    def read_file(self, path):
        if not self._in_scope(path):
            raise PermissionError("path outside Allowed Scope")
        self._require_client()
        return self.client.get_file(self.repository, path, self.branch)

    def write_file(self, path, content):
        if not self._in_scope(path):
            raise PermissionError("path outside Allowed Scope")
        if self.branch == "main":
            raise PermissionError("writes to main are prohibited")
        self._require_client()
        return self.client.put_file(self.repository, path, content, self.branch)

    def run_tests(self, command, paths):
        if not paths or any(not self._in_scope(p) for p in paths):
            raise PermissionError("test scope is empty or outside Allowed Scope")
        self._require_client()
        return self.client.run_tests(self.repository, self.branch, command, paths)

    def commit(self, message, paths, *, request_id):
        if self.branch == "main":
            raise PermissionError("commits to main are prohibited")
        if not request_id:
            raise ValueError("idempotency request_id is required")
        if request_id in self.commit_requests:
            raise FileExistsError("duplicate commit request blocked")
        if not paths or any(not self._in_scope(p) for p in paths):
            raise PermissionError("commit includes paths outside Allowed Scope")
        self._require_client()
        result = self.client.commit(self.repository, self.branch, message, paths)
        self.commit_requests[request_id] = result
        return result

    def record_result_candidate(self, session, packet, *, action_performed, result_references=None,
        created_references=None, modified_references=None, test_results=None, errors=None,
        limitations=None, proposed_resulting_state=None, continuation=None, valid=True):
        record = self.sessions[session.workspace_session_id]
        if record["result"] is not None:
            raise FileExistsError("duplicate repository Result Packet blocked")
        result = create_result_packet(packet=packet, session=session,
            result_status=OutputStatus.OUTPUT_VALID if valid else OutputStatus.OUTPUT_INVALID,
            action_performed=action_performed, result_references=result_references,
            created_references=created_references, modified_references=modified_references,
            test_results=test_results, errors=errors, limitations=limitations,
            proposed_resulting_state=proposed_resulting_state, continuation=continuation)
        record["result"] = result
        return result

    def get_result_packet(self, session):
        record = self.sessions.get(session.workspace_session_id)
        result = record.get("result") if record else None
        return result if hasattr(result, "result_packet_id") else None

    def receive_result(self, session):
        record = self.sessions.get(session.workspace_session_id)
        if record is None:
            return self._result("receive_result", OperationStatus.NOT_FOUND, session.workspace_reference)
        if record["result"] is None:
            return self._result("receive_result", OperationStatus.UNKNOWN, session.workspace_reference,
                                "No repository result recorded.")
        external = record["result"].result_packet_id if hasattr(record["result"], "result_packet_id") else record["result"].get("commit_sha")
        return self._result("receive_result", OperationStatus.SUCCESS, session.workspace_reference, external=external)

    def get_session_status(self, session):
        record = self.sessions.get(session.workspace_session_id)
        if record is None:
            return self._result("get_session_status", OperationStatus.NOT_FOUND, session.workspace_reference)
        return self._result("get_session_status", OperationStatus.SUCCESS, session.workspace_reference)

    def close_session(self, session):
        record = self.sessions.get(session.workspace_session_id)
        if record is None:
            return self._result("close_session", OperationStatus.NOT_FOUND, session.workspace_reference)
        record["status"] = "CLOSED"
        return self._result("close_session", OperationStatus.SUCCESS, session.workspace_reference,
                            external=session.workspace_session_id)
