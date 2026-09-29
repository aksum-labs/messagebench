# Maintainer guide

Run docs/reproduce.md before review. Never collect production inputs in issues or CI artifacts.
Review rights, declared semantics, targeted mutations and coverage before accepting an extractor.
Golden hash changes require an explanation separating metadata migration from behavior changes.
Use exact dependency pins and review native dependencies as well as Python advisories.

For a local release, commit a clean source tree, run scripts/reproducible_build.py with
--require-clean and prepare the platform-specific offline bundle. Verify hashes and install it
in a fresh environment outside the checkout. Preserve source archives/notices for native LGPL
redistribution. Do not claim signatures or independent reproduction from hashes alone.

Before publication follow docs/github-publication.md: actual owner handles, private vulnerability
reporting, required reviews, branch protection and release-review environment approval must be
configured by the organization. The provided workflow prepares unsigned artifacts; it does
not publish. Record actual external reviews before upgrading release readiness.
