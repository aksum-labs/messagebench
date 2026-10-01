# External Recognition Completion Report

MessageBench 0.2.0-rc.1 · 1 October 2026 · Aksum Labs

**Automatable recognition work completed; genuine human decisions remain explicitly gated.** The repository is public and protected, seven actual hosted workflows succeeded, the public Scorecard is 7.1/10, an authentic signed candidate was verified locally, Pages is live, and Software Heritage completed a full archive. No fabricated review, adoption, certification, badge or institutional relationship is claimed. No fees paid.

Evidence refers to main source `ad10253e1d0d9a07282ab78290f024cdbf5a111b`. Later evidence and the release-guard correction use a protected PR; they do not inherit main's signing or hosted test result. Version remains 0.2.0-rc.1 and two exact message versions. The original 389-item engineering completion report is preserved separately; this recognition mandate has 213 explicit requirements.

## A. Public repository status

[Public repository](https://github.com/aksum-labs/messagebench): main, corporate commit identity and organization-owned `aksum-labs-publisher[bot]` writes. Actual read-back verifies private vulnerability reporting, secret scanning/push protection, Dependabot security updates, read-only Actions defaults, squash-only merge and immutable releases. Main requires checks, dependencies, dependency-review and analyze; one code-owner approval, stale-review dismissal, last-push approval, admin enforcement, linear history and resolved conversations. No force push/deletion. Release tags prohibit update/deletion with no bypass actors. The release-review environment requires the organization team, prevents self-approval and admin bypass, and permits exactly main and the RC tag. See `evidence/github-settings.json`, `evidence/tag-rules-admin-readback.json` and `docs/github-hardening-report.md`.

GitHub hides ruleset bypass actors from read-only callers. The corrected release guard binds a privileged company-App read-back to the exact current ruleset fields/timestamps and fails closed on mismatch; CI receives no administrative write secret. Live read-only validation succeeded. Two real semantic/rights review decisions are still required before release. One maintainer team member is not two independent reviewers.

[Company-bot PR #7](https://github.com/aksum-labs/messagebench/pull/7) carries the refreshed evidence and correction. Required human approval is not bypassed or fabricated.

## B. Actual hosted CI

All seven workflows below succeeded at the named main commit. Checks includes formatting, typing, unit/golden/property/integration/security tests, 97.06% semantic branch coverage, targeted mutation checks, bounded parser/contract fuzzing, differential XSD, license/manifest/secret checks, SAST and clean build. Dependency vulnerability audit, CodeQL, dependency-review and long fuzz campaigns succeeded. Candidate preparation generated an SBOM including native XML dependencies and verified clean offline installation. Main hosted tests: **149 passed**; the protected release-guard PR source 7d620ae has **154 hosted passing tests**, with successful CodeQL, dependency review and actual read-only-token platform verification. Original paper measurement remains 140 tests at its stated original source.

| Workflow | Actual run | Conclusion |
|---|---|---|
| Checks | [36838413275](https://github.com/aksum-labs/messagebench/actions/runs/36838413275) | success |
| CodeQL | [36838413249](https://github.com/aksum-labs/messagebench/actions/runs/36838413249) | success |
| Dependency review | [36838826401](https://github.com/aksum-labs/messagebench/actions/runs/36838826401) | success |
| Scheduled security | [36838830192](https://github.com/aksum-labs/messagebench/actions/runs/36838830192) | success |
| OpenSSF Scorecard | [36838836697](https://github.com/aksum-labs/messagebench/actions/runs/36838836697) | success |
| Build and attest candidate snapshot | [36838833434](https://github.com/aksum-labs/messagebench/actions/runs/36838833434) | success |
| Documentation | [36838839643](https://github.com/aksum-labs/messagebench/actions/runs/36838839643) | success |

Exact source, jobs, steps and artifact digests: `evidence/hosted-recognition.json`. Filtered test proof: `evidence/hosted-checks-excerpt.txt`. PR results are separately source-bound in `evidence/recognition-pr-ci.json`, `evidence/hosted-pr-checks-excerpt.txt` and `evidence/hosted-readonly-release-controls.txt`. Checks run 36843481802, CodeQL run 36843481848 and dependency-review run 36843481803 all succeeded at 7d620ae. Later receipt-only updates require their own checks before merge. No later commit is attributed to an earlier run.

## C. OpenSSF Scorecard

**7.1/10**, actual published result on 1 October 2026. [Viewer](https://scorecard.dev/viewer/?uri=github.com/aksum-labs/messagebench), [public API](https://api.scorecard.dev/projects/github.com/aksum-labs/messagebench). Official immutable-pinned action, publish_results, job-scoped OIDC and SARIF upload ran successfully. A full CLI run agrees. README uses the real public badge. No score is promised.

| Check | Score |
|---|---:|
| Dependency-Update-Tool | 10 |
| Security-Policy | 10 |
| Code-Review | 0 |
| CI-Tests | -1 |
| Dangerous-Workflow | 10 |
| Packaging | -1 |
| Maintained | 0 |
| SAST | 10 |
| Pinned-Dependencies | 10 |
| Token-Permissions | 10 |
| Binary-Artifacts | 10 |
| CII-Best-Practices | 0 |
| License | 10 |
| Vulnerabilities | 10 |
| Fuzzing | 0 |
| Contributors | 0 |
| Signed-Releases | -1 |
| Branch-Protection | 8 |

Negative one is unavailable/unscored. Genuine short history, contributor/review history and lack of a granted Passing badge explain low scores; no fake activity was created. Custom bounded fuzzing exists even though the detector assigns Fuzzing zero. Details: `evidence/scorecard-public.json`, `evidence/scorecard-full-public.json`, `docs/scorecard-remediation.md`.

## D. OpenSSF Best Practices Passing

**READY-FOR-OWNER-APPROVAL**, no official project page or granted badge. The current official 67 criteria are hash-recorded in `evidence/openssf-current-criteria.json`; repository evidence and exact responses are prepared in `docs/openssf-best-practices-submission.md`. Real account ownership, secure-design competence, accountable human response commitments and ancillary-schema FLOSS interpretation require human/official decisions. No-report applicability can be assessed honestly; percentages and historical maintenance cannot be invented. A prepared checklist is not Passing.

## E. OSPS Baseline

Current 2026.08.28 Level 1: 24 controls assessed in `evidence/osps-baseline-level1.json`. Real main/tag enforcement is verified. Account MFA, human operating commitments and ancillary rights classification remain owner decisions. This is a self-assessment, not an awarded certification, badge or SLSA level.

## F. Signed release/provenance

**ACHIEVED authentic signed main-branch candidate; READY-FOR-OWNER-APPROVAL reviewed RC release.** [Snapshot run 36838833434](https://github.com/aksum-labs/messagebench/actions/runs/36838833434), [attestation 51751545](https://github.com/aksum-labs/messagebench/attestations/51751545), [signed candidate artifact](https://github.com/aksum-labs/messagebench/actions/runs/36838833434/artifacts/11149734913).

Exact verified identity:

```text
https://github.com/aksum-labs/messagebench/.github/workflows/snapshot.yml@refs/heads/main
issuer: https://token.actions.githubusercontent.com
```

Manifest SHA-256: `d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a`.
Signed artifact ZIP SHA-256: `59fe072e57e45a8ad800ed4bd416572b227d119654c4277821015a6b2660148f`.

The actual signed ZIP was downloaded through the company App, its platform digest checked, **all 31 manifest files verified**, exact Cosign identity verified locally, and source provenance matched ad10253. Evidence: `evidence/hosted-artifact-local-verification.json`, `evidence/hosted-signature-verification.txt`. It includes wheel/sdist, offline bundle, native-inclusive SBOM, checksums and toolchain/dependency/schema/contract/corpus provenance. Finite Actions retention is not permanent archival. Same-agent local verification is not independent review or independent reproduction. Repeated unsigned builds matched only under the documented same-environment experiment.

No formal tag-backed reviewed release exists. The prepared publication workflow requires two authentic hash-bound review decisions and protected environment approval, verifies exact tag/workflow OIDC identity and assets, then publishes an RC prerelease. See `docs/release-publication.md`; the actual platform controls are already enforced. No owner admin-bypass toggle remains necessary.

## G. LFDT submission

**READY-FOR-OWNER-APPROVAL.** All five requested package files exist under `external/lfdt/`. Primary-source free Lab Proposal route researched; no paid membership or proposal submitted. Real contacts, committer/DCO authority, neutral governance/trademark/transfer decisions and owner representation approval are required. Fit with LFDT's mission is candidly uncertain; MessageBench is not marketed as blockchain or sovereign infrastructure.

## H. FINOS routes

**READY-FOR-OWNER-APPROVAL.** Existing-project contribution is free; a new-project proposal needs a genuine Member sponsor. Morphir, Common Domain Model and Legend were inspected for substantive fit; archived DataHelix rejected. Proposal, technical charter and unsent sponsorship request prepared in `external/finos/`. No sponsor, relationship, submission or acceptance claimed.

## I. Upstream contribution

**READY-FOR-OWNER-APPROVAL.** mx20022 has a narrowly scoped executable Rust two-test patch: lexical leading-zero accounts and repeated Ethiopic remittance, with parseable semantic-loss mutations. Both tests passed against exact upstream commit `810cfa2e486745ca3a779c460a7768e1923f860a`; paired documents pass the exact XSD. No parser defect is falsely alleged. Proposal, patch, tests, evidence and contribution plan are in `external/upstream/mx20022/`. No PR sent. Real legal contribution identity/agreements and authorization are needed; a personal-account substitution is prohibited by the owner.

## J. Paper and brief

**ACHIEVED.** Public 9-page engineering preprint and 2-page CTO/central-bank brief, figures, reproducibility appendix and citation metadata: [paper directory](https://github.com/aksum-labs/messagebench/tree/main/paper). Original measured evidence: 100 paired synthetic cases, 140 tests, 99/102 semantic branches (97.06%), 40/40 defined targeted mutants, 200 differential-XSD documents, 100,000 parser iterations and 10,000 contract mutations. Benchmark: 1,000 comparisons cycling six pairs, 80.624042 pairs/s, p50 11.740749 ms, p95 15.584327 ms, peak RSS 40360 KiB, under disclosed conditions. No bank defect prevalence, independent corpus review, peer review or production SLA claimed. Later operational tests are separately counted above.

## K. Citation/archive

**ACHIEVED** software/paper CFF, AUTHORS/CONTRIBUTORS, Codemeta and explicit license metadata. **ACHIEVED Software Heritage full archival**: save request 2520811 succeeded; main revision ad10253 verified in snapshot:

```text
swh:1:snp:68c8e8f3c5a263c3f9c21855ec9399c7550e70fa
swh:1:rev:ad10253e1d0d9a07282ab78290f024cdbf5a111b
```

[Archived origin](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/aksum-labs/messagebench). Receipt, visit and snapshot evidence are retained. This snapshot does not include later PR changes. **Zenodo READY-FOR-OWNER-APPROVAL**: real account authorization and software/paper deposit metadata required; no DOI. Exact free setup in `docs/citation-and-archival.md`.

## L. Remaining human/account actions

- Review and merge the actual company-bot evidence/release-guard PR without bypassing main protection.
- Supply two genuine independent semantic/rights reviews bound to the prepared packet; then authorize the reviewed tag/release through the protected environment.
- Enable organization MFA and reduce extra registered App grants; all issued task tokens are already purpose/repo restricted. Decide accountable human maintenance/security response and competence attestations.
- Authorize official Best Practices registration and honest legal applicability responses; resolve ancillary-schema FLOSS interpretation with the official program where needed.
- Approve LFDT representation, real contacts, DCO/trademark/neutral-governance decisions; approve FINOS sponsor outreach and upstream legal contribution identity/agreements.
- Authorize Zenodo integration and separately accurate software/paper deposits.

No further Administration/Actions installation approval is requested: it is accepted and verified. No admin-bypass manual setting remains outstanding.

## M. External-party decisions and history

There are no unsubmitted foundation proposals falsely described as under review. LFDT stewards, FINOS members, upstream maintainers and official badge operators decide only after authorized submissions. Genuine maintenance, approved external contribution and response history cannot be synthesized. Current network failure and Software Heritage anti-bot behavior are resolved; neither remains a technical blocker.

## N. Public URLs

- https://aksum-labs.github.io/messagebench/
- https://api.scorecard.dev/projects/github.com/aksum-labs/messagebench
- https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/aksum-labs/messagebench
- https://github.com/aksum-labs/messagebench
- https://github.com/aksum-labs/messagebench/actions/runs/36838413249
- https://github.com/aksum-labs/messagebench/actions/runs/36838413275
- https://github.com/aksum-labs/messagebench/actions/runs/36838826401
- https://github.com/aksum-labs/messagebench/actions/runs/36838830192
- https://github.com/aksum-labs/messagebench/actions/runs/36838833434
- https://github.com/aksum-labs/messagebench/actions/runs/36838833434/artifacts/11149734913
- https://github.com/aksum-labs/messagebench/actions/runs/36838836697
- https://github.com/aksum-labs/messagebench/actions/runs/36838839643
- https://github.com/aksum-labs/messagebench/attestations/51751545
- https://github.com/aksum-labs/messagebench/blob/main/CITATION.cff
- https://github.com/aksum-labs/messagebench/pull/7
- https://github.com/aksum-labs/messagebench/tree/main/paper
- https://scorecard.dev/viewer/?uri=github.com/aksum-labs/messagebench

No Best Practices project page, formal RC release URL, DOI, foundation listing or upstream PR URL exists. Prepared submission destinations are recorded in the recognition matrix and are not acceptance receipts. Pages is actually deployed; its later PR revision needs main merge before deployment.

## O. Evidence hashes and reproduction

All evidence, workflow, paper, submission and documentation hashes are in `evidence/recognition-hashes.json`. Scope/source boundaries are explicit; the manifest and this report exclude recursive self-hashes. Actual hosted artifact digests, wheel/sdist hashes and signed manifest are recorded separately in the verification evidence.

```sh
python scripts/check_recognition.py
python scripts/check_licenses.py
python scripts/check_secrets.py
python -m pytest -q
python scripts/review_packet.py verify  # exit 3 until real reviews are supplied
messagebench corpus verify
python scripts/check_coverage.py evidence/coverage.json
```

`docs/reproduce.md` contains exact differential-XSD, mutation, long fuzz, benchmark, build, offline-install and signature verification commands. Hosted steps/run IDs are retained in evidence. Corporate CLI tools remain outside the public repository; no private key/token or personal push credentials are bundled.

## P. Permitted public claims

- Public, offline, adapter-neutral preservation-contract software under Apache-2.0 for original code/fixtures, with ancillary standard-schema terms separately documented.
- Exact pacs.008.001.08 and pacs.002.001.10 support, scoped assertions and visible unexamined information; no live scheme rules.
- Named-source synthetic engineering results, seven successful hosted workflows, 7.1 published Scorecard, live Pages and Software Heritage full archive.
- Authentic main-branch signed candidate and exact-identity verification locally; prepared reviewed-release workflow.
- Public preprint/brief and citation metadata; substantive tested upstream patch and complete free foundation submission packages prepared.

## Q. Prohibited claims

No NBE/EthSwitch/SWIFT/ISO/BIS/foundation approval or certification; no Passing badge, baseline award, SLSA level, DOI, formal reviewed RC release, v0.5/v1.0, independent human review/reproduction, bank adoption, production safety, complete-document preservation, camt support or proprietary Ethiopian rules. No submitted foundation/upstream proposal or Member sponsor. A company bot prevents personal public push attribution in these operations; it cannot hide ownership from GitHub itself.

## Exhaustive mandate accounting

213 explicit rows, sections 0–20: ACHIEVED: 197, BLOCKED-BY-REQUIRED-HUMAN-HISTORY: 1, READY-FOR-OWNER-APPROVAL: 15. Preparation is distinguished from submission, review, acceptance and publication. No PARTIAL state.

| ID | Requirement | Disposition | Evidence and next action |
|---|---|---|---|
| 00.01 | Zero fees | ACHIEVED | external/rejected-paid-recognition.md, external/recognition-matrix.json, evidence/hosted-recognition.json — No payment, institutional outreach or formal foundation application occurred; actual company-bot hosted actor is recorded. |
| 00.02 | No fabricated endorsements, reviews or adoption | ACHIEVED | external/rejected-paid-recognition.md, external/recognition-matrix.json, evidence/hosted-recognition.json — No payment, institutional outreach or formal foundation application occurred; actual company-bot hosted actor is recorded. |
| 00.03 | No fabricated history or certifications | ACHIEVED | external/rejected-paid-recognition.md, external/recognition-matrix.json, evidence/hosted-recognition.json — No payment, institutional outreach or formal foundation application occurred; actual company-bot hosted actor is recorded. |
| 00.04 | No personal-account public publishing | ACHIEVED | external/rejected-paid-recognition.md, external/recognition-matrix.json, evidence/hosted-recognition.json — No payment, institutional outreach or formal foundation application occurred; actual company-bot hosted actor is recorded. |
| 00.05 | Formal submission authorization respected | ACHIEVED | external/rejected-paid-recognition.md, external/recognition-matrix.json, evidence/hosted-recognition.json — No payment, institutional outreach or formal foundation application occurred; actual company-bot hosted actor is recorded. |
| 01.01 | Public visibility | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.02 | Default main | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.03 | Description | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.04 | Topics | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.05 | Repository-native documentation URL | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.06 | Discussions | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.07 | Issues | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.08 | Private vulnerability reporting | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.09 | Security policy | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.10 | CODEOWNERS team write access | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.11 | Dependabot configuration | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.12 | Dependency review | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.13 | CodeQL and Bandit | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.14 | Secret scanning | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.15 | Push protection | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.16 | Immutable release setting | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.17 | Least-privilege Actions default | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.18 | SHA-pinned Actions | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.19 | Job-scoped OIDC | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.20 | No unsafe pull_request_target | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.21 | Read-back of actual applied settings | ACHIEVED | evidence/github-settings.json, evidence/hosted-recognition.json, .github/CODEOWNERS — Verified public/settings read-back and successful hosted checks at 2bb62cb. Newly revised SECURITY.md is locally prepared for final company upload. |
| 01.22 | Main branch protection | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.23 | No force push to main | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.24 | Required PR review | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.25 | Required status checks | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.26 | Protected immutable version tags | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.27 | Enforced release environment review | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.28 | Final configuration read-back | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.29 | Dependabot security-update activation | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.30 | Optional Pages deployment | ACHIEVED | docs/github-hardening-report.md, .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 01.31 | Organization MFA and App registration grant reduction | READY-FOR-OWNER-APPROVAL | docs/github-hardening-report.md — Actual owner account readiness and reduction of extra registered permissions are required; issued task tokens were narrowly scoped. |
| 02.01 | Hosted formatting | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.02 | Hosted typing | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.03 | Hosted unit tests | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.04 | Hosted golden tests | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.05 | Hosted property tests | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.06 | Hosted integration tests | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.07 | Hosted targeted mutation campaign | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.08 | Hosted parser fuzz smoke | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.09 | Hosted contract fuzz smoke | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.10 | Hosted differential XSD | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.11 | Hosted security corpus | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.12 | Hosted license checks | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.13 | Hosted Python dependency audit | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.14 | Hosted secret scan | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.15 | Hosted SAST | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.16 | Hosted manifest validation | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.17 | Hosted native-inclusive SBOM | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.18 | Hosted clean build | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.19 | Hosted fresh offline install | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.20 | Hosted Scorecard | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.21 | Run IDs and source SHA | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.22 | Artifact hashes and conclusions | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.23 | Actual successful run links and failure reporting | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-checks-excerpt.txt — Actual seven hosted workflows succeeded at ad10253; Checks ran 149 tests. Updated evidence PR CI is distinct; no inferred result for later commits. |
| 02.24 | Hosted runs for final prepared documentation/workflow commit | ACHIEVED | evidence/recognition-pr-ci.json, evidence/hosted-pr-checks-excerpt.txt, evidence/hosted-readonly-release-controls.txt — Actual protected PR source 7d620ae passed Checks (154 tests and read-only live release controls), CodeQL and dependency review. Exact run/job evidence retained. Human merge is separate and not bypassed. |
| 03.01 | Official immutable-pinned action | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.02 | Public scan | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.03 | publish_results | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.04 | Job-only id-token | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.05 | Least privileges elsewhere | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.06 | Safe job configuration | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.07 | SARIF upload | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.08 | Actual overall score | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.09 | All 18 checks recorded | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.10 | Full CLI cross-check | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.11 | Remediation plan | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.12 | Earned badge markup prepared | ACHIEVED | evidence/scorecard-public.json, .github/workflows/scorecard.yml, docs/scorecard-remediation.md, README.md — Actual published 7.1/10 at ad10253; official action and full CLI agree, all 18 checks recorded. Badge refers to earned public result; no score gaming. |
| 03.13 | Rescan after protection and final badge upload | ACHIEVED | docs/github-hardening-report.md — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 04.01 | Current official Passing criteria | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.02 | All 67 criterion assessments and applicability | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.03 | Repository evidence per criterion | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.04 | No false badge claim | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.05 | Shortest honest satisfaction path | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.06 | Current OSPS Level 1 assessment | ACHIEVED | evidence/openssf-current-criteria.json, evidence/osps-baseline-level1.json, docs/openssf-best-practices-submission.md — Current source hashes/date retained; technical public/CI prerequisites reassessed from actual evidence. |
| 04.07 | Authorized account application | READY-FOR-OWNER-APPROVAL | docs/openssf-best-practices-submission.md — No project page or badge obtained. Owner/assessor must resolve identity, competence and ancillary-license classification honestly. |
| 04.08 | Secure-design competence attestation | READY-FOR-OWNER-APPROVAL | docs/openssf-best-practices-submission.md — No project page or badge obtained. Owner/assessor must resolve identity, competence and ancillary-license classification honestly. |
| 04.09 | Responsible human maintenance commitment | READY-FOR-OWNER-APPROVAL | docs/openssf-best-practices-submission.md — No project page or badge obtained. Owner/assessor must resolve identity, competence and ancillary-license classification honestly. |
| 04.10 | Ancillary schema FLOSS interpretation | READY-FOR-OWNER-APPROVAL | docs/openssf-best-practices-submission.md — No project page or badge obtained. Owner/assessor must resolve identity, competence and ancillary-license classification honestly. |
| 04.11 | Official Passing issuance | READY-FOR-OWNER-APPROVAL | docs/openssf-best-practices-submission.md — No project page or badge obtained. Owner/assessor must resolve identity, competence and ancillary-license classification honestly. |
| 04.12 | Response-history criteria | BLOCKED-BY-REQUIRED-HUMAN-HISTORY | evidence/openssf-current-criteria.json — No invented response percentages. Owner may seek official no-report applicability interpretation before waiting unnecessarily. |
| 05.01 | Candidate wheel and sdist build | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.02 | Source and toolchain provenance | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.03 | Dependency hashes | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.04 | Schema hashes | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.05 | Contract hashes | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.06 | Corpus hash | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.07 | CycloneDX native SBOM | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.08 | SHA256SUMS | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.09 | Cosign bundle | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.10 | GitHub OIDC signature | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.11 | Exact workflow and ref verification | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.12 | GitHub artifact attestation | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.13 | Two same-host unsigned builds compared | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. |
| 05.14 | Fresh offline bundle installation | ACHIEVED | evidence/hosted-recognition.json, evidence/hosted-signature-verification.txt, .github/workflows/snapshot.yml, evidence/local-recognition-offline-install.json — Authenticated main-branch candidate only. Manifest SHA d8aaffbf9eceb4c146d6619eca8fae2b16fefc5697de054b567c93ac28fc862a; attestation 51751545. All 31 manifest files and exact Cosign identity verified locally. No independent reproduction claim. Refreshed release-preparation bundle also verified locally with socket calls denied, at source 8ff219c; not independently reviewed. |
| 05.15 | Reviewed tag-backed signing approval | READY-FOR-OWNER-APPROVAL | .github/workflows/publish-reviewed-release.yml, docs/release-publication.md — Tag-specific workflow prepared and actionlint checked locally; enable only after real review and actual environment protection. No tag-backed signature exists yet. |
| 05.16 | Tag-specific publication/signing workflow | READY-FOR-OWNER-APPROVAL | .github/workflows/publish-reviewed-release.yml, docs/release-publication.md, scripts/release_guard.py, tests/integration/test_release_handoffs.py, evidence/local-release-preparation.json — Prepared source includes actual API response handling and version-matched privileged rule read-back. Formal execution still requires genuine reviewed packet and environment approval. |
| 06.01 | Complete scope-labelled RC release notes | ACHIEVED | docs/release-notes-0.2.0-rc.1.md — Includes exact message scope, limits, synthetic evidence, security/rights/reproduction/Scorecard/Best Practices links; no approval claims. |
| 06.02 | Create reviewed v0.2.0-rc.1 tag and publish formal prerelease | READY-FOR-OWNER-APPROVAL | docs/release-publication.md, .github/workflows/publish-reviewed-release.yml — Requires two authenticated independent reviews and protected owner approval. Current signed snapshot is not this release. |
| 07.01 | Current LFDT process research | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.02 | Project summary and problem | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.03 | Architecture and maturity | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.04 | Governance and contributor model | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.05 | Licensing and security | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.06 | Roadmap and reproducibility | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.07 | OpenSSF and Scorecard disclosure | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.08 | Mission fit and complementary rationale | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.09 | Neutral governance and Aksum contribution | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.10 | Transfer and trademark implications | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.11 | Free Lab route and DCO assessment | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.12 | Complete five-file package | ACHIEVED | external/lfdt/README.md, external/lfdt/submission.md, external/lfdt/technical-summary.md, external/lfdt/governance-readiness.md, external/lfdt/faq.md — Current Lab Proposal issue form documented; no paid membership prerequisite asserted. Mission fit is candidly uncertain, not transformed into a blockchain claim. |
| 07.13 | Formal Lab submission and legal contact/transfer authority | READY-FOR-OWNER-APPROVAL | external/lfdt/submission.md — Owner supplies genuine human contacts, DCO authority and formal representation approval; no submission, acceptance or ownership transfer. |
| 08.01 | Three existing FINOS contribution targets | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.02 | Inspect actual contribution rules | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.03 | Concrete substantive improvement plans | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.04 | Avoid archived or cosmetic targets | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.05 | New-project proposal | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.06 | Business problem and solution | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.07 | Roadmap and existing materials | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.08 | Team/contributor commitment template | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.09 | Governance plan | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.10 | Technical charter | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.11 | Unsent sponsor request | ACHIEVED | external/finos/upstream-targets.md, external/finos/project-proposal.md, external/finos/technical-charter-draft.md, external/finos/sponsor-request.md — Morphir, Common Domain Model and Legend inspected. DataHelix archived and rejected. Free existing-project route distinguished from member-sponsored new project. |
| 08.12 | FINOS outreach/contribution authorization | READY-FOR-OWNER-APPROVAL | external/finos/sponsor-request.md — No outreach sent and no sponsor exists. Owner must authorize representation and real contributor legal agreements before contact. |
| 08.13 | Real Member sponsorship and formal proposal | READY-FOR-OWNER-APPROVAL | external/finos/sponsor-request.md — No outreach sent and no sponsor exists. Owner must authorize representation and real contributor legal agreements before contact. |
| 09.01 | Prior-art targets inspected | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.02 | Strongest narrow upstream improvement selected | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.03 | Original fixture and executable tests | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.04 | Tested Rust patch | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.05 | Proposal and PR plan | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.06 | Evidence and no duplication claim | ACHIEVED | external/upstream/mx20022/proposal.md, external/upstream/mx20022/upstream.patch, external/upstream/mx20022/evidence.json — Two new mx20022 tests pass at pinned upstream 810cfa2e486745ca3a779c460a7768e1923f860a. Parser accepts transformed semantic changes; no upstream defect or merged contribution claimed. |
| 09.07 | Submit upstream PR with actual legal contribution identity | READY-FOR-OWNER-APPROVAL | external/upstream/mx20022/patch-or-pr-plan.md — Prepared tested patch; no fake DCO/CLA or personal-account PR. Upstream acceptance not presumed. |
| 10.01 | Abstract and motivation | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.02 | Problem definition and validity distinction | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.03 | Preservation contracts | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.04 | Corpus design | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.05 | Threat model | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.06 | Methodology and baselines | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.07 | Measured results and failure classes | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.08 | Coverage limits and false assurance | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.09 | Prior art | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.10 | Reproducibility | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.11 | Limitations and future work | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.12 | Rights and conclusion | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.13 | 9-page preprint PDF | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.14 | Figures and appendix | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.15 | Separate citation metadata | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 10.16 | 2-page technical brief | ACHIEVED | paper/messagebench-benchmark.md, paper/messagebench-benchmark.pdf, paper/technical-brief.pdf, paper/reproducibility-appendix.md — Only measured synthetic evidence; six-pair 1,000-comparison benchmark 80.624 pairs/s is bounded and environment-specific. No bank rates or peer-review claims. |
| 11.01 | CITATION.cff | ACHIEVED | CITATION.cff, AUTHORS, CONTRIBUTORS, codemeta.json, docs/citation-and-archival.md — Public corporate attribution and citation metadata; archival identifiers absent. |
| 11.02 | AUTHORS and CONTRIBUTORS | ACHIEVED | CITATION.cff, AUTHORS, CONTRIBUTORS, codemeta.json, docs/citation-and-archival.md — Public corporate attribution and citation metadata; archival identifiers absent. |
| 11.03 | Codemeta project metadata | ACHIEVED | CITATION.cff, AUTHORS, CONTRIBUTORS, codemeta.json, docs/citation-and-archival.md — Public corporate attribution and citation metadata; archival identifiers absent. |
| 11.04 | SPDX and separate asset terms | ACHIEVED | CITATION.cff, AUTHORS, CONTRIBUTORS, codemeta.json, docs/citation-and-archival.md — Public corporate attribution and citation metadata; archival identifiers absent. |
| 11.05 | Free software and separate paper DOI pathways | ACHIEVED | CITATION.cff, AUTHORS, CONTRIBUTORS, codemeta.json, docs/citation-and-archival.md — Public corporate attribution and citation metadata; archival identifiers absent. |
| 11.06 | Zenodo account authorization and actual DOI deposit | READY-FOR-OWNER-APPROVAL | docs/citation-and-archival.md — Owner legal account/integration and genuine metadata approval required; no DOI yet. |
| 11.07 | Software Heritage save and actual snapshot verification | ACHIEVED | docs/citation-and-archival.md — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 12.01 | Public Scorecard signal | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.02 | Best Practices evidence | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.03 | OSPS disclosure | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.04 | CodeQL | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.05 | Dependency review and updates | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.06 | Secret scanning | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.07 | Artifact attestation | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.08 | Sigstore | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.09 | Native-inclusive SBOM | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.10 | SLSA-compatible provenance without level claim | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 12.11 | Public security evidence disclosure | ACHIEVED | SECURITY-EVIDENCE.md, evidence/hosted-recognition.json — Measured automated checks separated from independent review and awards; no claimed SLSA level. |
| 13.01 | Professional free repository-native landing | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.02 | Demo and architecture | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.03 | Supported scope and security | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.04 | Benchmark and recognition status | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.05 | Citation and contribution | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.06 | Roadmap | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.07 | Prepared static Pages site and pinned workflow | ACHIEVED | docs/index.md, site/index.html, .github/workflows/pages.yml — Repository-native docs public. Pages workflow is prepared and linted locally, not a verified deployed site. |
| 13.08 | Actual GitHub Pages publication and URL verification | ACHIEVED | .github/workflows/pages.yml — Network recovered. Company App published ad10253, applied/read-back actual controls; hosted documentation deployed and SWH full visit/snapshot confirmed. See exact supporting evidence. |
| 14.01 | Financial Infrastructure Assurance portfolio positioning | ACHIEVED | docs/aksum-open-source-positioning.md — No future tools announced as products or institutional relationships claimed. |
| 14.02 | Separation from sovereign settlement research | ACHIEVED | docs/aksum-open-source-positioning.md — No future tools announced as products or institutional relationships claimed. |
| 14.03 | Unannounced future tools kept as research possibilities | ACHIEVED | docs/aksum-open-source-positioning.md — No future tools announced as products or institutional relationships claimed. |
| 15.01 | Compact institutional overview | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.02 | Technical abstract and architecture diagram | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.03 | Benchmark and security summary | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.04 | License and actual earned signals | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.05 | Foundation and citation status | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.06 | Repository/paper URLs and release limits | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 15.07 | No NBE-proposal positioning | ACHIEVED | external/messagebench-institutional-brief.md — Dossier prepared, actual public candidate attestation linked; no formal release or earned foundation listing falsely implied. |
| 16.01 | Machine-readable all-target recognition matrix | ACHIEVED | external/recognition-matrix.json — Only mandated terminal dispositions used. Technical-environment blockers are explicit, not disguised as human approval. |
| 16.02 | Required free/paid and applicability fields | ACHIEVED | external/recognition-matrix.json — Only mandated terminal dispositions used. Technical-environment blockers are explicit, not disguised as human approval. |
| 16.03 | Prepared/submitted/accepted distinguished | ACHIEVED | external/recognition-matrix.json — Only mandated terminal dispositions used. Technical-environment blockers are explicit, not disguised as human approval. |
| 16.04 | Date/source/URLs and exact blockers | ACHIEVED | external/recognition-matrix.json — Only mandated terminal dispositions used. Technical-environment blockers are explicit, not disguised as human approval. |
| 16.05 | All minimum target categories | ACHIEVED | external/recognition-matrix.json — Only mandated terminal dispositions used. Technical-environment blockers are explicit, not disguised as human approval. |
| 17.01 | Paid membership filter | ACHIEVED | external/rejected-paid-recognition.md — No fee paid; some legitimate fee-based programs simply outside scope, not disparaged. |
| 17.02 | Paid awards/certification/listings rejected | ACHIEVED | external/rejected-paid-recognition.md — No fee paid; some legitimate fee-based programs simply outside scope, not disparaged. |
| 17.03 | Paid conference/standards/audit prerequisite filter | ACHIEVED | external/rejected-paid-recognition.md — No fee paid; some legitimate fee-based programs simply outside scope, not disparaged. |
| 17.04 | Separate rejected routes record | ACHIEVED | external/rejected-paid-recognition.md — No fee paid; some legitimate fee-based programs simply outside scope, not disparaged. |
| 18.01 | Every recognition target explicitly accounted for | ACHIEVED | external/recognition-matrix.json, external/mandate-accounting.json — Accounting complete; unresolved real outcomes still disclosed as blocked/owner-ready, not success. |
| 18.02 | No vague pending or PARTIAL target states | ACHIEVED | external/recognition-matrix.json, external/mandate-accounting.json — Accounting complete; unresolved real outcomes still disclosed as blocked/owner-ready, not success. |
| 19.01 | Completion report A through Q | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Report prepared locally; final publication and enforcement remain genuine environment blockers. |
| 19.02 | All public URLs | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Report prepared locally; final publication and enforcement remain genuine environment blockers. |
| 19.03 | All evidence hashes | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Current file hashes listed separately from actual platform artifact digests; no recursive/self-hash claim. |
| 19.04 | Public allowed/prohibited claims | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Report prepared locally; final publication and enforcement remain genuine environment blockers. |
| 19.05 | Human/account and external blockers | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Report prepared locally; final publication and enforcement remain genuine environment blockers. |
| 19.06 | Exact final five summary categories | ACHIEVED | EXTERNAL_RECOGNITION_COMPLETION_REPORT.md, evidence/recognition-hashes.json — Report prepared locally; final publication and enforcement remain genuine environment blockers. |
| 20.01 | Public software exists and tests run | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.02 | Claims reproducible within scope | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.03 | Visible security controls | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.04 | Authentic candidate provenance | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.05 | Original licensing and separate asset limits | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.06 | Constructive substantive upstream preparation | ACHIEVED | evidence/hosted-recognition.json, SECURITY-EVIDENCE.md, external/upstream/mx20022/evidence.json — Earned public engineering credibility; no invented reviews, certifications or paid visibility. |
| 20.07 | Fully hardened final public release and independent verification | READY-FOR-OWNER-APPROVAL | docs/release-publication.md, docs/github-hardening-report.md — Public protection, hosted evidence and signed snapshot are verified. Formal reviewed release and independent verification require genuine human reviews and protected owner approval; no network blocker remains. |
| 01.32 | Disable release-environment administrator bypass and verify it | ACHIEVED | evidence/github-settings.json, evidence/release-controls-live-verification.json — Actual API accepted false; GET read-back confirms can_admins_bypass:false. Earlier missing documentation was not proof of impossibility. |

## Required final summary

**ACHIEVED NOW:** hardened public GitHub repository; seven successful hosted workflows; public 7.1/10 Scorecard; authentic signed/attested candidate with all 31 files and exact OIDC identity verified locally; live Pages; full Software Heritage archive; 9-page preprint, 2-page brief and citation metadata; tested upstream patch; complete security/rights/zero-cost submission evidence.

**READY TO SUBMIT:** honest Best Practices application; LFDT Lab package; FINOS free contribution/sponsor routes; upstream PR; Zenodo deposits. Protected evidence PR and reviewed RC require real owner/reviewer approval. None of these formal external applications has been sent.

**WAITING ON EXTERNAL PARTY:** no foundation/upstream decision is pending on an unsent proposal. Official outcomes can follow authorized submissions. Software Heritage archival itself is complete.

**BLOCKED BY REAL-WORLD HISTORY:** actual contributor review, sustained accountable maintenance and genuine response history. Official no-report applicability can be considered honestly; no fake activity.

**REJECTED:** paid membership/listing/award/certification/sponsorship/audit-prerequisite routes; cosmetic/unfit upstream changes; unsupported approval or adoption claims. No money spent.

Automatable work and evidence preparation do not constitute the remaining genuine human approvals, official badge issuance or external acceptance.
