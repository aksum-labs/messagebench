# Reviewed release publication — exact remaining actions

Current actual artifact: a signed main-branch candidate snapshot at source commit `2bb62cb1e0dcbbb91d265bb824eda274cbd9b217`. No `v0.2.0-rc.1` tag or formal release has been published. No independent human review has occurred.

## Human review and approval

1. Give two genuine independent reviewers `evidence/review-packet.json`, `docs/fixture-review.md`, the corpus, contracts, coverage limits and rights register. Use the blank `docs/reviewer-form.template.json`; a coding agent must not fill in real review decisions.
2. Authenticate their identity, expertise, independence and decisions through an accountable human. Software checks hash/decision consistency only. Put their authorized decisions under `reviews/`. Run `python scripts/review_packet.py verify`; it must return 0. All packet assets must still match their reviewed hashes.
3. Publish the reviewed metadata through the company App using approved public reviewer handles. Never expose personal identifiers without their authorization.
4. Verify actual main protection, immutable version tags and `release-review` required reviewers, prevention of self-review and admin bypass. Use Selected branches and tags with exact policies for branch `main` and tag `v0.2.0-rc.1`; protected-branches-only is insufficient for this tag workflow. These controls are now established by actual App read-back. Genuine review and owner approval remain mandatory; YAML alone is still not proof.
5. Owner approves this exact RC release and enables `REVIEWED_RELEASE_ENABLED=true`. This is genuine authorization, not an automated reviewer attestation.

## Technical publication path prepared

`.github/workflows/publish-reviewed-release.yml` is a locally actionlint-checked workflow for exactly `refs/tags/v0.2.0-rc.1`. Its prepared main version is public; the API-visibility correction and privileged record are in the protected review PR. The formal tag workflow has not run. It builds and tests clean source, compares two same-host unsigned builds, generates native-inclusive SBOM/provenance, verifies a fresh offline install, checks the authenticated review packet, signs and verifies the manifest, creates GitHub attestation, then publishes a prerelease after protected environment approval.

The company App creates the exact immutable tag on the reviewed commit; never recreate an existing tag or rewrite source history. An annotated Git tag is not a cryptographically signed tag. Required review and owner approval are separate from signing.

Expected tag-specific Cosign identity:

```text
https://github.com/aksum-labs/messagebench/.github/workflows/publish-reviewed-release.yml@refs/tags/v0.2.0-rc.1
```

Issuer: `https://token.actions.githubusercontent.com`. Verify the signature against that exact identity/ref and verify every `SHA256SUMS` entry. The current snapshot signature uses a different workflow and main ref; it cannot be substituted as a tag signature.

The publication job uses job-scoped Contents write and GitHub's workflow token, never personal push credentials. It uploads wheel, sdist, manifest, Cosign bundle, SBOM, source/toolchain/input provenance and a complete offline bundle. GitHub provides source archives from the exact tag. No PyPI upload or hosted financial service is created. Release notes are in `docs/release-notes-0.2.0-rc.1.md`.

Read back the actual release tag/commit, prerelease state, immutable state and each asset digest after creation. Capture the exact successful run and verification logs. Configure free archival only with authorized accounts and verify resulting DOI/SWHIDs separately.

## Actual controls and read-only API visibility

Networking recovered and company-App publication/configuration succeeded. Actual main/tag/environment data is in evidence/github-settings.json. Administrator bypass was disabled by the API and read back false; no manual toggle is still needed.

GitHub omits ruleset bypass actors from callers without ruleset write access. The protected workflow keeps its token read-only for these checks. The company App's administrative read-back is committed as evidence/tag-rules-admin-readback.json and included in the hash-bound human review packet. The guard requires the live rule ID, timestamps and relevant public fields to match that record exactly before using its explicit bypass list. Missing/stale/mismatched data or a nonempty bypass list fails closed. This avoids giving CI a write-capable App key and does not infer safety from omitted data. [GitHub rule API](https://docs.github.com/en/rest/repos/rules?apiVersion=2026-03-10#get-a-repository-ruleset).

Actual live control validation is evidence/release-controls-live-verification.json. Source review must cover the record and guard correction before the exact tag is approved. The owner must authenticate reviewers; software verifies only hash/decision consistency. No reviews have been fabricated.

The publication job verifies the exact tag-workflow signature again after download. The offline ZIP checksum uses a relative basename, so recipients can verify it in their download directory. Local preparation can reuse cleared wheels via --wheel-cache with --no-index; no package index is needed.
