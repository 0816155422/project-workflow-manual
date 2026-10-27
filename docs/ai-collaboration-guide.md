# AI Collaboration Guide

This repository supports multi-AI collaboration through approved files, not automatic memory merging.

- Treat reviewed files under `shared/` as authoritative shared context.
- Treat `pending/` as unapproved drafts.
- Platform directories contain manually curated snapshots and prompt templates.
- Export platform snapshots explicitly and record source, date, and reviewer.
- Do not import arbitrary chat history automatically.
- Do not store secrets, credentials, or sensitive personal information.
- Be transparent about uncertainty and never claim an action succeeded without evidence.