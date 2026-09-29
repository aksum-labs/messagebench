# Publication preparation

Nothing in this sprint publishes the repository. Proposed slug: `aksum-messagebench`.
Intended owner: the Aksum Labs organization; its actual GitHub handle must be verified.

Description / About text:

> Offline preservation tests for financial-message adapters: versioned contracts, synthetic fixtures and reproducible, scope-labelled evidence.

Topics: `financial-infrastructure`, `iso20022`, `testing`, `data-quality`, `python`,
`offline`, `open-source`, `payments`.

Social preview text: “Both messages parse. Did the transformation preserve what it promised?”
Use Aksum-owned artwork only. Do not use regulator, scheme or vendor logos.

Before enabling release preparation:

1. Review GATE_REPORT.md, RELEASE_READINESS.md, asset rights and security evidence.
2. Assign real maintainer/security handles; update CODEOWNERS and enable private vulnerability reporting.
3. Protect main and release tags, require a separate review, disallow force pushes and require CI.
4. Create the `release-review` environment with required human reviewers and main-only deployment branches.
5. Only after those checks set repository variable `RELEASE_PREPARATION_ENABLED=true`.
6. Run the manual preparation workflow. It builds review artifacts, not a public release.
7. Human maintainers decide whether to publish and obtain identity-backed signatures/provenance.

Workflow files do not themselves enable branch protection, private reporting or reviewer
requirements. These settings and hosted CI results are unverified until the real repository
is created and configured. No badge, organizational membership or endorsement is implied.
