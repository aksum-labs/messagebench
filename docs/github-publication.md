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

## Concrete owner plan

Generate files using the actual organization/repository, two real handles and corresponding
numeric GitHub user IDs (examples below are placeholders, not assigned maintainers):

```sh
python scripts/owner_setup.py --repo ACTUAL_ORG/aksum-messagebench \
  --maintainer REAL_HANDLE_ONE --maintainer REAL_HANDLE_TWO \
  --reviewer-id REAL_NUMERIC_ID_ONE --reviewer-id REAL_NUMERIC_ID_TWO \
  --out /tmp/messagebench-owner-plan
```

The command only writes a plan; it performs no GitHub calls. Inspect and execute the generated
OWNER_COMMANDS.sh after publication approval. It configures two branch approvals, code owners,
strict CI checks, no force pushes, private vulnerability reporting, a protected release
review environment, controlled tag creation and immutable existing release tags. Use the
current GitHub REST API; do not apply these settings to an unrelated existing repository.
The plan also includes read-back commands to verify settings after application.

Enable `RELEASE_SIGNING_ENABLED=true` only after real review records are in `reviews/`, the
review checker passes, and the environment requires a separate human approver. The sign job
uses a pinned Cosign executable and GitHub OIDC, verifies the exact repository/workflow/ref
identity, and retains a Sigstore bundle. Only that job requests `id-token: write`; PR jobs
remain read-only. The workflow never publishes a GitHub release or package automatically.

Actual execution of this plan, hosted checks, account identity, disclosure ownership and
publication approval are BLOCKED-BY-HUMAN. There is no configured remote in the delivered
checkout. No account authority is inferred from the intended organization name.
