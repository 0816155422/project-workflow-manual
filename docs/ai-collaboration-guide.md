# AI collaboration guide

## Starting a session
Give the AI the repository URL and exact approved files relevant to the task. Ask it to list sources used and identify missing context. Do not assume repository access unless a connected tool or uploaded file provides it.

## Switching platforms
Export only the context needed for the task, review for privacy, then provide the same selected files to the next platform. Do not export full chat histories by default.

## Returning changes
Ask for proposed file content or a diff, rationale, and sources. Human review is required before content becomes approved shared memory.

## Conflict resolution
If sources disagree, do not silently merge them. Record sources and dates, then ask the repository owner to decide.

## Limitations
An allowlist is a policy document, not technical access control. GitHub Pages is static hosting, not a secure authenticated write backend. A write API needs authentication, least privilege, validation, audit policy, and deployment review.
