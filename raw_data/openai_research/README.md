# OpenAI research raw evidence

This directory stores traceable research notes derived from public, authoritative OpenAI sources. Each source has a JSONL index record, a short raw-text research note, and a metadata JSON record.

## Provenance and integrity
- Only public official OpenAI pages are included in this initial batch.
- `sources.jsonl` is append-only: add new lines; do not rewrite or remove prior records.
- `raw/` and `metadata/` records are immutable snapshots. Corrections should create a new versioned record that references the prior record rather than overwriting it.
- `Verified` means the URL, title, publication date, and excerpt were checked against the named official source at ingestion time. It does not imply independent replication of the source's claims.
- Excerpts are deliberately short. Raw text files are research notes, not full-page copies.
- Never store secrets, credentials, access tokens, or API keys here.
- When a source cannot be checked, mark it `Unverified`; do not infer missing metadata.

## Schema
Each `sources.jsonl` row contains `source_id`, `title`, `source_url`, `publisher`, `publish_date`, `category`, `summary`, `excerpt`, `tags`, `confidence_level`, `verification_status`, `notes`, and `ingested_at`. Each record must include a timestamp and canonical source URL.

## Initial ingestion
The initial batch contains three official OpenAI pages: a deep research system card, a third-party evaluation playbook, and the GPT-6 Astra safety overview. See `manifest.json` for counts.
