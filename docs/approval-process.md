# Approval Process

1. Draft a Markdown, JSON, or TXT file under `pending/`.
2. Run validation or open a pull request for validation.
3. Review source, accuracy, privacy, and necessity manually.
4. Confirm no secrets, credentials, or sensitive personal data are present.
5. Run **Sync Approved Memory** with a source under `pending/`, a new destination under `shared/`, and an approval note.
6. Confirm the workflow succeeded and created a commit.
7. Check `logs/approval-log.md` and commit history.
8. For changes to existing approved files, use a reviewed pull request; sync intentionally refuses overwrite.

A passing automated scan is not proof that content is safe.