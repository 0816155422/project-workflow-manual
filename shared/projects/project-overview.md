# Project Overview

**Status:** PROPOSED — review and approve before relying on this as canonical memory.

## Project
Shared AI Memory Workspace in 0816155422/project-workflow-manual.

## Intended outcome
A structured, version-controlled workspace where a person explicitly provides approved project files to ChatGPT, Jamin, Claude, Gemini, or another reviewed platform. AI returns proposed changes without silently importing previous conversations.

## Existing assets
- Dashboard source: hap-aicc/index.html
- GitHub Actions read/write runner: .github/workflows/api-runner.yml
- Separate MCP HTTP implementation: api/mcp.js and MCP_API.md; not assumed hosted
- GitHub Pages workflow: .github/workflows/deploy-pages.yml

## Boundaries
This is document and coordination storage, not a real-time database. An allowlist entry does not mean a platform is connected or automatic synchronization exists.
