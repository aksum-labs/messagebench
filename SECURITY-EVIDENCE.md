# Security evidence — actual controls and bounded assurance

Public engineering candidate 0.2.0-rc.1. Actual public main: ad10253e1d0d9a07282ab78290f024cdbf5a111b. No reviewed formal release, institutional approval or independent-human review.

## Automated and hosted evidence

100 synthetic pairs, 40/40 defined targeted mutants, 200 matching differential-XSD document classifications, 100,000 parser iterations and 10,000 contract mutations. Core branches 99/102 (97.06%). The original paper records 140 tests at its historical measured source; updated main hosted Checks ran 149. The further guard-record correction uses a separate protected PR and its tests are accounted separately. No bank defect prevalence, complete-document guarantee or independent reproduction is inferred.

Seven hosted workflows succeeded at ad10253: Checks, CodeQL, dependency review, long security/fuzzing, Scorecard, candidate build/signing and Pages. Exact runs/jobs/steps/artifact hashes are evidence/hosted-recognition.json. No result is assigned to an untested later source.

Runtime remains offline: secure bounded XML; DTD/entities/XInclude/network resolution disabled; closed non-executable contracts; local inputs; redacted/escaped reports; no adapter execution. Native-inclusive CycloneDX SBOM and rights/advisory inventories are included. Python pip-audit does not scan native libraries. Resource limits are not an OS sandbox and fuzzing is bounded.

## Actual public controls

Strict protected-main checks and real code-owner approval; no admin/force-push/deletion bypass for main; immutable version-tag update/deletion rules; required company-team release approval; prevention of self-review; administrator environment bypass disabled; exact branch/tag deployment policies. Private vulnerability reporting, secret scanning/push protection, dependency updates and read-only workflow defaults are read back. Evidence: github-settings.json and release-controls-live-verification.json.

Read-only ruleset API responses omit bypass actors. The App's privileged record is version-matched to live public metadata before the guard uses it; omissions are not treated as empty. A stale/missing record fails closed. No App private key or write-capable administrative secret is placed in CI. That correction must be reviewed/merged before formal publication. Real reviewers are still mandatory.

## Signed candidate and local verification

[Run 36838833434](https://github.com/aksum-labs/messagebench/actions/runs/36838833434) built clean source, compared two same-host unsigned Python artifacts, generated native SBOM/provenance and verified fresh offline installation. It signed the checksum manifest and verified exact workflow identity. [Attestation 51751545](https://github.com/aksum-labs/messagebench/attestations/51751545) authenticates manifest SHA-256 d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a.

Identity: https://github.com/aksum-labs/messagebench/.github/workflows/snapshot.yml@refs/heads/main. Issuer: https://token.actions.githubusercontent.com. Signed ZIP SHA-256: 59fe072e57e45a8ad800ed4bd416572b227d119654c4277821015a6b2660148f. Local download matched the platform digest, verified all 31 manifest entries and reverified that signature outside the hosted build. See hosted-artifact-local-verification.json. This is verification by the same agent, not an independently reproduced build or human review. It is a main snapshot, not a tag-backed reviewed release.

## Earned signals and unresolved human work

Public Scorecard 7.1/10 at ad10253, confirmed by full 18-check CLI scan. Live Pages documentation and completed Software Heritage snapshot are earned. No Best Practices Passing badge, OSPS award, SLSA level, DOI, LFDT/FINOS acceptance or sponsor exists. Original code/corpus Apache-2.0; bundled standard schemas retain separate terms; camt.053 excluded. Real MFA readiness, ongoing maintenance/response commitments, legal/account attestations, independent review and protected PR approval cannot be fabricated. SECURITY.md gives the enabled private reporting route.
