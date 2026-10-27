# GitHub Pages Deployment Guide

The current Pages workflows publish `hap-aicc/`. The `public/` and `static-site/` folders are reference layouts, not the current deployment source.

1. Check Settings → Pages for the configured source.
2. Inspect the latest Actions run and confirm the uploaded artifact path.
3. Confirm deployment success before checking the published URL.
4. Avoid concurrent deployments.

Both `.github/workflows/hap-aicc-pages.yml` and `.github/workflows/deploy-pages.yml` currently perform similar deployments. Review run history, select one canonical workflow, and only then disable/remove the duplicate.