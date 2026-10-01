# Reviewed release publication — exact remaining actions

Current actual artifact: a signed main-branch candidate snapshot at source commit `2bb62cb1e0dcbbb91d265bb824eda274cbd9b217`. No `v0.2.0-rc.1` tag or formal release has been published. No independent human review has occurred.

## Human review and approval

1. Give two genuine independent reviewers `evidence/review-packet.json`, `docs/fixture-review.md`, the corpus, contracts, coverage limits and rights register. Use the blank `docs/reviewer-form.template.json`; a coding agent must not fill in real review decisions.
2. Authenticate their identity, expertise, independence and decisions through an accountable human. Software checks hash/decision consistency only. Put their authorized decisions under `reviews/`. Run `python scripts/review_packet.py verify`; it must return 0. All packet assets must still match their reviewed hashes.
3. Publish the reviewed metadata through the company App using approved public reviewer handles. Never expose personal identifiers without their authorization.
4. Verify actual main protection, immutable version tags and `release-review` required reviewers, prevention of self-review and admin bypass. Use Selected branches and tags with exact policies for branch `main` and tag `v0.2.0-rc.1`; protected-branches-only is insufficient for this tag workflow. The last evidence snapshot does not establish these protections; do not enable signing/publication merely because YAML contains an environment.
5. Owner approves this exact RC release and enables `REVIEWED_RELEASE_ENABLED=true`. This is genuine authorization, not an automated reviewer attestation.

## Technical publication path prepared

`.github/workflows/publish-reviewed-release.yml` is a locally actionlint-checked workflow for exactly `refs/tags/v0.2.0-rc.1`. It is not yet uploaded or run. It builds and tests clean source, compares two same-host unsigned builds, generates native-inclusive SBOM/provenance, verifies a fresh offline install, checks the authenticated review packet, signs and verifies the manifest, creates GitHub attestation, then publishes a prerelease after protected environment approval.

The company App creates the exact immutable tag on the reviewed commit; never recreate an existing tag or rewrite source history. An annotated Git tag is not a cryptographically signed tag. Required review and owner approval are separate from signing.

Expected tag-specific Cosign identity:

```text
https://github.com/aksum-labs/messagebench/.github/workflows/publish-reviewed-release.yml@refs/tags/v0.2.0-rc.1
```

Issuer: `https://token.actions.githubusercontent.com`. Verify the signature against that exact identity/ref and verify every `SHA256SUMS` entry. The current snapshot signature uses a different workflow and main ref; it cannot be substituted as a tag signature.

The publication job uses job-scoped Contents write and GitHub's workflow token, never personal push credentials. It uploads wheel, sdist, manifest, Cosign bundle, SBOM, source/toolchain/input provenance and a complete offline bundle. GitHub provides source archives from the exact tag. No PyPI upload or hosted financial service is created. Release notes are in `docs/release-notes-0.2.0-rc.1.md`.

Read back the actual release tag/commit, prerelease state, immutable state and each asset digest after creation. Capture the exact successful run and verification logs. Configure free archival only with authorized accounts and verify resulting DOI/SWHIDs separately.

## Current execution boundary

Company-App API/push requests currently fail DNS in the restricted execution environment. Final workflow/evidence upload, main/tag/environment enforcement and future dispatch must resume with company-App networking. The connected personal GitHub identity may read evidence but must not perform public writes. This is a technical environment blocker, not another request for the already accepted App permissions.

## Runtime checks against actual platform controls

Each tag workflow job calls `scripts/release_guard.py` before build/sign/publication work. It fails closed if the exact public repository, protected main, required company-team approval with prevention of self-review, disabled admin bypass, exact main/tag deployment policies or immutable version-tag rules are absent or unreadable. This verifies platform configuration, not human review authenticity. The separate packet verification and accountable human identity check remain mandatory.

The official REST environment update parameters inspected on 1 October do not document an admin-bypass setter. Do not treat an unlisted JSON field as proof of enforcement. An account owner can deselect **Allow administrators to bypass configured protection rules** in environment settings, then the App/guard must read back `can_admins_bypass: false`. This is the documented account-setting path; it is not evidence that the setting has been saved here. [GitHub environment configuration](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments), [deployment branch/tag policy API](https://docs.github.com/en/rest/deployments/branch-policies?apiVersion=2026-03-10).

The publication job verifies the signed manifest identity again after artifact download, and generates the offline ZIP checksum with a relative basename so recipients can run `sha256sum -c offline-archive.sha256` in their download directory. Bundle documentation describes attached signature/review status without falsely calling every signed snapshot an unsigned local bundle.
