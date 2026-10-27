# Memory Manifest

## Purpose
Maintain clear boundaries between approved shared memory, pending review items, platform snapshots, private/local-only material, and archives.

## Memory classes
### Approved shared memory
Location: `shared/`. Reviewed, versioned content approved for reuse. No secrets or sensitive personal data.

### Pending memory
Location: `pending/`. Drafts awaiting human review. Promotion occurs only through the manual approval workflow or an explicitly reviewed pull request.

### Platform memory
Location: `platforms/`. Explicit exports, snapshots, prompts, and sync rules for individual AI platforms. This is not a live memory store and must not auto-import arbitrary chat history.

### Private memory
Location: `private/`. The directory is a placeholder only. Do not commit private or sensitive content; use secure local-only storage outside this repository.

### Archive memory
Location: `archives/`. Historical records retained for traceability. Do not overwrite historical entries.

## Security rules
- Never store tokens, passwords, API keys, SSH keys, or credentials.
- Do not persist sensitive personal information.
- Secret scanning is best-effort and is not a guarantee.
- Manually review content before approval.

## Sync rules
- Promote files from `pending/` to `shared/` only through the approved process.
- Record approvals and sync actions in the audit log.
- The sync workflow refuses to overwrite existing destinations; use a reviewed pull request for changes.
