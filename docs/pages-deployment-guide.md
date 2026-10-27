# GitHub Pages Deployment Guide

## Current deployment source
The existing Pages workflows publish the `hap-aicc/` directory. The `public/` and `static-site/` directories are reference layouts and are not the current deployment source.

## Deployment checks
1. Open repository Settings → Pages and verify the configured source.
2. Open Actions and inspect the latest Pages workflow run.
3. Confirm the upload artifact uses the intended directory.
4. Confirm deployment succeeds before checking the published URL.
5. Avoid running multiple deploy workflows concurrently.

## Workflow consolidation
Both `.github/workflows/hap-aicc-pages.yml` and `.github/workflows/deploy-pages.yml` currently perform similar deployments. Keep only one canonical workflow enabled after reviewing run history and Settings → Pages. Do not delete either workflow until the canonical choice is confirmed.
