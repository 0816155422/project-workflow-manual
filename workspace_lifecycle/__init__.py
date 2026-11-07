"""Cross-platform Workspace Lifecycle coordination layer."""
from .models import *
from .session import WorkspaceCoordinator
from .packets import create_work_packet, create_result_packet
from .handoff import create_handoff, accept_handoff
from .persistence import PersistenceBoundary
from .checkpoint import CheckpointBoundary
from .resume import derive_resume
