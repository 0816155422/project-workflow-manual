# Approval Process

1. Draft a Markdown, JSON, or TXT file under `pending/`.
2. Run **Validate Shared Memory** or open a pull request for validation.
3. Review source, purpose, accuracy, privacy, and necessity manually.
4. Confirm that no secret, credential, or sensitive personal data is present.
5. Run **Sync Approved Memory** manually with a source under `pending/`, a new destination under `shared/`, and a concise approval note.
6. Confirm the workflow succeeded and created a commit.
7. Check `logs/approval-log.md` and the repository commit history.
8. For changes to existing approved files, use a reviewed pull request; the sync workflow intentionally refuses overwrite.

A passing automated scan is not proof that content is safe. The person approving the workflow is responsible for the decision.
