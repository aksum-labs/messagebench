# FINAL_COMPLETION_REPORT — MessageBench

> Historical engineering acceptance snapshot (29 September 2026). Current publication/security/recognition state is recorded in EXTERNAL_RECOGNITION_COMPLETION_REPORT.md. This historical report is not a current visibility or badge claim. The current 389-item crosswalk is FINAL_COMPLETION_REPORT_CURRENT.md.

Reference date: 29 September 2026. Engineering candidate: **0.2.0-rc.1** (Python package 0.2.0rc1).

Every original mandate section 0–37 is accounted for below. Technical automation is complete within the cleared two-message scope. Authentic human review, rights-holder clarification for the excluded third version, and account-owner actions are explicitly separated. Nothing was published or represented as independently approved.

**389 requirement dispositions: 372 PASS; 17 BLOCKED-BY-HUMAN; 0 IMPOSSIBLE-WITH-EVIDENCE.**

No global impossibility is asserted for camt redistribution: the reviewed public sources did not establish complete permission. Exclusion is definitive for this release; a rights holder or qualified human determination could change a future release.

## Verified technical result

Both XML documents can parse and pass the exact XSD while an adapter loses a leading zero, truncates a reference, drops repeated remittance or changes a currency. The preservation contract detects these defects. Identity and explicitly allowed message-ID regeneration pass. Parser/XSD scope is not misrepresented as an upstream bug.

100 original paired cases; 13 generated security/workflow scenarios with controls; 10 contracts; 38 required assertion declarations; 27 extractable fields; 140 passing pytest tests; 99/102 core semantic branches (97.06%); 40/40 targeted mutants killed; 200 documents with matching XSD classification across two processors. No whole-program mutation or whole-document preservation claim.

100,000 parser fuzz iterations and 10,000 contract mutations completed with no unexpected exception/acceptance in these bounded campaigns. The dated Python audit enumerates 60 pinned distributions and reports zero known vulnerabilities. Native advisory analysis is separate and source-bounded. SBOM validation, dependency license checks, read-only workflow lint, secret scanning, SAST and the full offline check runner completed. See evidence/local-acceptance.json and the linked evidence per item.

Measured 1,000-pair benchmark: 80.62 pairs/s; p50 11.741 ms; p95 15.584 ms; peak RSS 40360 KiB. Six small original proof pairs cycled; full compare in-process with warm file cache; no CLI startup or service-level guarantee. CPU/RAM/OS/library versions are recorded in evidence/benchmark.json.

The delivery bundle contains clean-source build evidence, unsigned wheel/sdist checksums, source commit/input provenance, offline runtime wheels, native original sources and license notices, SBOM and a fresh outside-checkout installation record. Identical unsigned Python artifacts are checked across two clean source copies in the same environment. Native-wheel and independent reproduction are not claimed.

## Human-only handoffs

1. Two real independent reviewers inspect docs/fixture-review.md and docs/technical-review-checklist.md, approve exact packet hashes and all case outcomes, and perform rights/security review. A responsible human authenticates their identity and independence. No review decisions have been invented.
2. Aksum's account owner supplies real organization/maintainer identities, applies the generated scripts/owner_setup.py payloads, enables private disclosure and branch/tag/environment protections, runs hosted CI, and authorizes publication.
3. After authentic review and environment protection, the owner enables the protected OIDC signing workflow. The exact workflow identity is verified before using the signature. Badge application/public Scorecard need the actual public repository.
4. camt.053.001.08 needs authoritative redistribution clearance before future implementation/distribution. The prepared inquiry is not sent without instructions. No camt support is claimed or silently substituted.

Version v0.5 requires three cleared versions and genuine corpus review; v1.0 also requires stable public API, independent review, outside use and governance. Completing local engineering cannot manufacture those real-world facts.

## Exact reproduction commands

Use docs/quickstart.md for the hash-pinned development/native setup; docs/offline-install.md for the supplied offline bundle. From repository root:

```sh
messagebench compare corpus/negative/reference-truncated.source.xml corpus/negative/reference-truncated.target.xml  # expected exit 1
messagebench corpus verify corpus/index.json  # expected exit 0, 100 matches
python scripts/check_all.py --out /tmp/aksum-checks-new --actionlint /path/to/actionlint
python scripts/baseline.py
python scripts/mutations.py
python scripts/differential_xsd.py
python scripts/security_corpus.py
python fuzz/smoke.py --iterations 100000
python fuzz/contracts.py --iterations 10000
python scripts/benchmark.py
python scripts/check_licenses.py
python scripts/review_packet.py verify  # expected exit 3 until genuine review
python scripts/completion_report.py --check
python scripts/reproducible_build.py ../clean-release-new --require-clean
python scripts/prepare_bundle.py --release ../clean-release-new --native /path/to/native-build --archives /path/to/native-sources --out ../review-bundle-new
python scripts/release_provenance.py --bundle ../review-bundle-new
```

Connected developer-only checks are explicitly separate: `pip-audit --strict --disable-pip --no-deps -r dependency-lock.txt -f json`; `python scripts/fetch_dev_tools.py --out /tmp/tools-new actionlint scorecard cosign`. Installed MessageBench never downloads, invokes an adapter or contacts a service.

## Exhaustive original-mandate accounting

### Original section 0

**00.01 — PASS — Validate genuine technical purpose before expansion**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/expansion-decision.md](docs/expansion-decision.md), [GATE_REPORT.md](GATE_REPORT.md).

**00.02 — PASS — Enforce and record acceptance gates**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/expansion-decision.md](docs/expansion-decision.md), [GATE_REPORT.md](GATE_REPORT.md).

**00.03 — PASS — Reshape when rights or upstream overlap require it**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/expansion-decision.md](docs/expansion-decision.md), [GATE_REPORT.md](GATE_REPORT.md).

**00.04 — PASS — Prefer substance over release labeling**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/expansion-decision.md](docs/expansion-decision.md), [GATE_REPORT.md](GATE_REPORT.md).

**00.05 — PASS — Do not claim v1.0 without its criteria**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/expansion-decision.md](docs/expansion-decision.md), [GATE_REPORT.md](GATE_REPORT.md).


### Original section 1

**01.01 — PASS — MessageBench name and messagebench repository slug (owner naming revision, 2026-09-30)**

Owner requested the neutral public name MessageBench without the Aksum prefix. Organization ownership and corporate commit identity remain Aksum Labs. Evidence: [README.md](README.md), [docs/api.md](docs/api.md).

**01.02 — PASS — Offline declared-preservation product contract**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/api.md](docs/api.md).

**01.03 — PASS — Primary and secondary users documented**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/api.md](docs/api.md).

**01.04 — PASS — Compare information promises rather than parse success**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/api.md](docs/api.md).


### Original section 2

**02.01 — PASS — No payment initiation**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.02 — PASS — No routing**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.03 — PASS — No settlement**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.04 — PASS — No balances or account service**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.05 — PASS — No SWIFT connectivity**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.06 — PASS — No EATS connectivity**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.07 — PASS — No EthSwitch connectivity**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.08 — PASS — No live APIs**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.09 — PASS — No customer KYC**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.10 — PASS — No sanctions screening**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.11 — PASS — No AML decisioning**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.12 — PASS — No universal MT/MX translation**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.13 — PASS — No CBDC**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.14 — PASS — No DvP/PvP**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.15 — PASS — No government securities**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.16 — PASS — No stablecoins**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.17 — PASS — No wallets**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.18 — PASS — No hosted financial service**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.19 — PASS — No national standards or NBE rulemaking**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.20 — PASS — No Ethiopian account-number standards**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.21 — PASS — No official conformance or certification**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.22 — PASS — No public bank rankings**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.23 — PASS — No live bank testing**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.24 — PASS — No financial-institution scraping or probing**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.25 — PASS — No inferred proprietary EATS/EIPS/EthSwitch rules**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).

**02.26 — PASS — No NBE/EthSwitch/SWIFT/ISO endorsement or production-safety claims**

Runtime is a bounded local-file comparator. No connectors, server, custody, adapter execution or institutional-rule implementation exists; exclusions are explicit. Evidence: [README.md](README.md), [src/aksum_messagebench](src/aksum_messagebench), [LIMITATIONS.md](LIMITATIONS.md).


### Original section 3

**03.01 — PASS — Initial proof limited to pacs.008.001.08**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.02 — PASS — Identity control**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.03 — PASS — Leading-zero identifier-loss case**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.04 — PASS — Truncated reference case**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.05 — PASS — Removed repeated remittance case**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.06 — PASS — Permitted regenerated message ID control**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.07 — PASS — Additional currency-preservation defect**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.08 — PASS — At least two defective targets remain well-formed and exact-XSD-valid**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.09 — PASS — XSD alone accepts declared semantic defects**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.10 — PASS — MessageBench detects defects**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.11 — PASS — Correct transformations pass**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.12 — PASS — Permitted changes avoid false positives**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.13 — PASS — Deterministic repeatable evidence**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.14 — PASS — No proprietary Ethiopian rules**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.15 — PASS — Bundled proof assets zero-fee with retained terms**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.16 — PASS — Selected maintained prior art does not provide the exact combined workflow**

Implemented and verified within the declared offline scope. Evidence: [corpus/gate1-index.json](corpus/gate1-index.json), [evidence/baseline.json](evidence/baseline.json), [tests/golden](tests/golden), [docs/prior-art.md](docs/prior-art.md), [evidence/rights-register.json](evidence/rights-register.json).

**03.17 — BLOCKED-BY-HUMAN — Independent review of at least six initial pairs**

Two genuine independent human reviewers must examine the hash-bound packet and record decisions. The owner allowed development continuation; no independent approval is fabricated. Evidence: [docs/fixture-review.md](docs/fixture-review.md), [evidence/review-packet.json](evidence/review-packet.json), [docs/reviewer-form.template.json](docs/reviewer-form.template.json).


### Original section 4

**04.01 — PASS — Inspect Prowide ISO 20022**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.02 — PASS — Inspect mx20022**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.03 — PASS — Inspect iso20022-cbpr-ur**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.04 — PASS — Inspect Cognis**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.05 — PASS — Inspect Mojaloop Testing Toolkit**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.06 — PASS — Record parsing/XSD/business-rule overlap**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.07 — PASS — Record warnings and round-trip overlap**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.08 — PASS — Assess adapter-independent contracts and reusable corpus**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.09 — PASS — Assess coverage accounting**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.10 — PASS — Record exact sources and reuse decisions**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).

**04.11 — PASS — Do not exaggerate novelty**

Implemented and verified within the declared offline scope. Evidence: [docs/prior-art.md](docs/prior-art.md), [evidence/prior-art-snapshots.json](evidence/prior-art-snapshots.json), [evidence/prior-art-pactus.json](evidence/prior-art-pactus.json), [evidence/baseline.json](evidence/baseline.json).


### Original section 5

**05.01 — PASS — Python 3.12+**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.02 — PASS — Use lxml instead of an XSD engine rewrite**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.03 — PASS — Use jsonschema Draft 2020-12**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.04 — PASS — pytest and Hypothesis**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.05 — PASS — Use Decimal/hashlib/json and standard library**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.06 — PASS — Pin exact dependencies**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).

**05.07 — PASS — Produce full dependency inventory**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [dependency-lock.txt](dependency-lock.txt), [dependency-lock-hashed.txt](dependency-lock-hashed.txt), [evidence/dependency-inventory.json](evidence/dependency-inventory.json).


### Original section 6

**06.01 — PASS — Bounded reader to exact schema validation**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.02 — PASS — Version-specific fact extraction**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.03 — PASS — Versioned preservation contracts**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.04 — PASS — Typed deterministic comparison**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.05 — PASS — Coverage accounting**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.06 — PASS — JSON/text/HTML/JUnit output**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.07 — PASS — Reproducibility manifest**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.08 — PASS — No server/database/cloud/telemetry/accounts**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.09 — PASS — No runtime downloads or network**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).

**06.10 — PASS — Users execute adapters independently**

Implemented and verified within the declared offline scope. Evidence: [docs/architecture.md](docs/architecture.md), [src/aksum_messagebench](src/aksum_messagebench), [docs/file-handoff.md](docs/file-handoff.md), [scripts/reproducible_build.py](scripts/reproducible_build.py).


### Original section 7

**07.01 — PASS — Regular-file size and symlink/path/URL protections**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.02 — PASS — DTD/entity/XInclude/network rejection**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.03 — PASS — Exact QName and namespace enforcement**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.04 — PASS — Depth/element/text limits**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.05 — PASS — Hash-pinned local schema catalog**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.06 — PASS — Provenance and original QName paths**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.07 — PASS — Field presence and extractor version**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.08 — PASS — Closed non-executable JSON contracts**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.09 — PASS — Exact text comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.10 — PASS — Exact identifier comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.11 — PASS — Decimal comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.12 — PASS — Decimal-plus-currency comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.13 — PASS — Presence comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.14 — PASS — Ordered-list comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.15 — PASS — Multiset comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.16 — PASS — Explicit keyed repeated-item comparator**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.17 — PASS — Allowed regeneration**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.18 — PASS — Explicit normalization**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.19 — PASS — Examined/excluded/unsupported/unexamined categories**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.20 — PASS — Deterministic synthetic fixtures/manifests/defects**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.21 — PASS — Review metadata without invented reviewers**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.22 — PASS — Deterministic redacted report renderers**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.23 — PASS — Offline CLI and stable exit codes**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench](src/aksum_messagebench), [tests](tests), [schemas](schemas), [corpus](corpus), [docs/api.md](docs/api.md).

**07.24 — BLOCKED-BY-HUMAN — camt.053 extractor module with cleared exact schema**

Excluded under the uncertain-rights rule. An authoritative redistribution confirmation or qualified human rights determination is required before this asset/module enters the distributable; no support is claimed. Evidence: [docs/camt053-asset-review.md](docs/camt053-asset-review.md).


### Original section 8

**08.01 — PASS — inspect command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.02 — PASS — compare command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.03 — PASS — corpus verify command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.04 — PASS — suite command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.05 — PASS — report command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.06 — PASS — regression command**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.07 — PASS — No shell-command execution flag**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).

**08.08 — PASS — No plugins/URL input/dynamic dependency installation**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/cli.py](src/aksum_messagebench/cli.py), [tests/integration/test_cli.py](tests/integration/test_cli.py), [tests/integration/test_workflows.py](tests/integration/test_workflows.py).


### Original section 9

**09.01 — PASS — Exit 0 success**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.02 — PASS — Exit 1 assertion/input failure**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.03 — PASS — Exit 2 CLI/configuration error**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.04 — PASS — Exit 3 incomplete/unsupported required evidence**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.05 — PASS — Exit 4 safety/resource rejection**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.06 — PASS — Exit 5 internal error**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.07 — PASS — Exact precedence 5 > 4 > 2 > 3 > 1 > 0**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).

**09.08 — PASS — Retain observed safe results**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/errors.py](src/aksum_messagebench/errors.py), [tests/unit/test_exit_precedence.py](tests/unit/test_exit_precedence.py), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/workflows.py](src/aksum_messagebench/workflows.py).


### Original section 10

**10.01 — PASS — Draft 2020-12 closed contract schema**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).

**10.02 — PASS — All required contract metadata fields**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).

**10.03 — PASS — Authority enum and engineering-contract defaults**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).

**10.04 — PASS — Draft/reviewed/deprecated status enum**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).

**10.05 — PASS — Assertion IDs/fields/comparators/cardinality/missing/required**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).

**10.06 — PASS — No executable expressions**

Implemented and verified within the declared offline scope. Evidence: [schemas/contracts.schema.json](schemas/contracts.schema.json), [contracts](contracts), [src/aksum_messagebench/contracts.py](src/aksum_messagebench/contracts.py), [tests/security/test_files_contracts.py](tests/security/test_files_contracts.py).


### Original section 11

**11.01 — PASS — Identifiers stay strings with leading zeroes**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.02 — PASS — Scheme/issuer and institution context separate**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.03 — PASS — No assumed IBAN or invented national check digits**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.04 — PASS — Exact Decimal amount semantics**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.05 — PASS — Independent currency equality**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.06 — PASS — Lexical amount input retained**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.07 — PASS — Instructed and settlement amounts distinct**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.08 — PASS — Exact Unicode by default**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.09 — PASS — No silent trim/case folding/transliteration/normalization**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.10 — PASS — Explicit NFC only when declared**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.11 — PASS — Ethiopic preservation data**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.12 — PASS — Bounded XSD Gregorian timestamp semantics**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.13 — PASS — Unknown timezone/calendar yields INDETERMINATE**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.14 — PASS — Repeated multiplicity and order/multiset semantics**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.15 — PASS — Explicit single-item association**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.16 — PASS — Unique declared batch keys**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.17 — PASS — No amount/name matching heuristic**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.18 — PASS — Ambiguous keys INDETERMINATE**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).

**11.19 — PASS — Message-ID regeneration only under declared permission**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/comparators.py](src/aksum_messagebench/comparators.py), [src/aksum_messagebench/time_semantics.py](src/aksum_messagebench/time_semantics.py), [src/aksum_messagebench/association.py](src/aksum_messagebench/association.py), [corpus/semantic](corpus/semantic), [tests/unit/test_time_semantics.py](tests/unit/test_time_semantics.py), [docs/api.md](docs/api.md).


### Original section 12

**12.01 — PASS — PASS/FAIL/NOT_APPLICABLE/UNSUPPORTED/INDETERMINATE model**

Implemented and verified within the declared offline scope. Evidence: [schemas/report.schema.json](schemas/report.schema.json), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/unit/test_reports.py](tests/unit/test_reports.py).

**12.02 — PASS — Required unsupported/indeterminate checks prevent PASS**

Implemented and verified within the declared offline scope. Evidence: [schemas/report.schema.json](schemas/report.schema.json), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/unit/test_reports.py](tests/unit/test_reports.py).

**12.03 — PASS — Scope notice in every report**

Implemented and verified within the declared offline scope. Evidence: [schemas/report.schema.json](schemas/report.schema.json), [src/aksum_messagebench/engine.py](src/aksum_messagebench/engine.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/unit/test_reports.py](tests/unit/test_reports.py).


### Original section 13

**13.01 — PASS — Default reports omit names/accounts/raw XML/payment values/free text**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).

**13.02 — PASS — Report metadata limited to paths/IDs/codes/counts/hashes/versions**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).

**13.03 — PASS — Sanitized parser errors**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).

**13.04 — PASS — No production inputs in CI artifacts**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).

**13.05 — PASS — Hashes explicitly not anonymization**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).

**13.06 — PASS — No telemetry**

Implemented and verified within the declared offline scope. Evidence: [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [tests/integration/test_gate.py](tests/integration/test_gate.py), [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [SECURITY.md](SECURITY.md).


### Original section 14

**14.01 — PASS — UTF-8 and LF canonical output**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/golden](tests/golden), [tests/property/test_invariants.py](tests/property/test_invariants.py).

**14.02 — PASS — Stable ordering and JSON serialization**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/golden](tests/golden), [tests/property/test_invariants.py](tests/property/test_invariants.py).

**14.03 — PASS — No timestamp in canonical results**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/golden](tests/golden), [tests/property/test_invariants.py](tests/property/test_invariants.py).

**14.04 — PASS — Wall-clock data separated into build/benchmark evidence**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/golden](tests/golden), [tests/property/test_invariants.py](tests/property/test_invariants.py).

**14.05 — PASS — Golden-hash regression checks**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/reports.py](src/aksum_messagebench/reports.py), [tests/golden](tests/golden), [tests/property/test_invariants.py](tests/property/test_invariants.py).


### Original section 15

**15.01 — PASS — At least 24 fixtures and target 60 exceeded**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.02 — PASS — Identity copy**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.03 — PASS — Prefix rename with same QName**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.04 — PASS — Foreign namespace with familiar names**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.05 — PASS — Leading-zero loss**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.06 — PASS — Account institution context loss**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.07 — PASS — Decimal rounding**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.08 — PASS — Currency change**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.09 — PASS — Reference truncation**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.10 — PASS — Removed remittance repetition**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.11 — PASS — Duplicated remittance repetition**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.12 — PASS — Altered Ethiopic text**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.13 — PASS — Permitted regenerated message ID**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.14 — PASS — Unsupported extension**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.15 — PASS — Ambiguous batch association**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.16 — PASS — Optional absence on both sides**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.17 — PASS — Invalid target XSD**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.18 — PASS — DTD/entity expansion attack**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.19 — PASS — Remote schema/entity attempt**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.20 — PASS — Deep XML**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.21 — PASS — Oversized input**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.22 — PASS — HTML payload**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.23 — PASS — Malformed contract**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.24 — PASS — Unsupported namespace**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.25 — PASS — Missing required adapter output**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.26 — PASS — Excluded-field behavior**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.27 — PASS — Unexamined-field coverage**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.28 — PASS — Positive controls for failure classes**

Implemented and verified within the declared offline scope. Evidence: [corpus/index.json](corpus/index.json), [corpus/semantic/index.json](corpus/semantic/index.json), [evidence/security-corpus.json](evidence/security-corpus.json), [scripts/security_corpus.py](scripts/security_corpus.py), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py).

**15.29 — BLOCKED-BY-HUMAN — Genuine independent release-corpus review**

100 paired scenarios and 13 safety/workflow probes are prepared; genuine human decisions and reviewer authentication cannot be generated automatically. Evidence: [evidence/review-packet.json](evidence/review-packet.json), [docs/fixture-review.md](docs/fixture-review.md).


### Original section 16

**16.01 — PASS — pacs.008.001.08 priority implemented**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/extractors](src/aksum_messagebench/extractors), [schemas/catalog.json](schemas/catalog.json), [README.md](README.md).

**16.02 — PASS — pacs.002.001.10 priority implemented**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/extractors](src/aksum_messagebench/extractors), [schemas/catalog.json](schemas/catalog.json), [README.md](README.md).

**16.03 — PASS — No further message families before rigor**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/extractors](src/aksum_messagebench/extractors), [schemas/catalog.json](schemas/catalog.json), [README.md](README.md).

**16.04 — PASS — No claim these versions are used by Ethiopian rails**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/extractors](src/aksum_messagebench/extractors), [schemas/catalog.json](schemas/catalog.json), [README.md](README.md).

**16.05 — BLOCKED-BY-HUMAN — camt.053.001.08 third-family support**

Rights-specific human clarification is required before future implementation of this excluded version; no fabricated extractor or permissive substitute XSD. Evidence: [docs/camt053-asset-review.md](docs/camt053-asset-review.md).


### Original section 17

**17.01 — PASS — Unit tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.02 — PASS — Golden tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.03 — PASS — Property tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.04 — PASS — Metamorphic tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.05 — PASS — Targeted mutation tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.06 — PASS — Parser fuzzing**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.07 — PASS — Contract fuzzing**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.08 — PASS — Integration tests**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.09 — PASS — Second mature XSD processor over release corpus**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.10 — PASS — At least 90% core branch coverage**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.11 — PASS — Every required declaration has a killing mutation witness**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.12 — PASS — All recorded corpus classifications match**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.13 — PASS — No confirmed unresolved critical/high exploitable finding in bounded scans**

Implemented and verified within the declared offline scope. Evidence: [tests](tests), [evidence/coverage.json](evidence/coverage.json), [evidence/rule-coverage.json](evidence/rule-coverage.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/differential-xsd.json](evidence/differential-xsd.json), [evidence/fuzz-extended.txt](evidence/fuzz-extended.txt), [evidence/contract-fuzz.json](evidence/contract-fuzz.json), [evidence/native-advisory-review.json](evidence/native-advisory-review.json), [evidence/dependency-audit.json](evidence/dependency-audit.json).

**17.14 — BLOCKED-BY-HUMAN — Independent correctness/security review**

Actual external review must be performed and authenticated by humans; automated tests and source inspection are not substituted for it. Evidence: [docs/fixture-review.md](docs/fixture-review.md), [docs/technical-review-checklist.md](docs/technical-review-checklist.md).


### Original section 18

**18.01 — PASS — Actual CPU/RAM/OS/Python/native versions/corpus recorded**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).

**18.02 — PASS — Benchmark 1000 small pairs**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).

**18.03 — PASS — Measured throughput**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).

**18.04 — PASS — Measured p50 and p95 latency**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).

**18.05 — PASS — Measured peak RSS**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).

**18.06 — PASS — No invented performance claims**

Implemented and verified within the declared offline scope. Evidence: [scripts/benchmark.py](scripts/benchmark.py), [evidence/benchmark.json](evidence/benchmark.json).


### Original section 19

**19.01 — PASS — 5 MiB input limit**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).

**19.02 — PASS — Depth 64**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).

**19.03 — PASS — 100000 XML elements**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).

**19.04 — PASS — 1 MiB single text node**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).

**19.05 — PASS — 1000 assertions**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).

**19.06 — PASS — Practical CPU/wall-clock/address-space limits**

Implemented and verified within the declared offline scope. Evidence: [src/aksum_messagebench/input_guard.py](src/aksum_messagebench/input_guard.py), [src/aksum_messagebench/xml_reader.py](src/aksum_messagebench/xml_reader.py), [src/aksum_messagebench/runtime_limits.py](src/aksum_messagebench/runtime_limits.py), [tests/security/test_process_limits.py](tests/security/test_process_limits.py).


### Original section 20

**20.01 — PASS — Malicious XML threat and tests**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.02 — PASS — Malicious contract threat and tests**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.03 — PASS — Schema traversal defenses**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.04 — PASS — Symlink/path defenses**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.05 — PASS — Report privacy defenses**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.06 — PASS — HTML injection defenses**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.07 — PASS — False-assurance scope controls**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.08 — PASS — Dependency compromise controls**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.09 — PASS — Untrusted PR read-only/no-secrets controls**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).

**20.10 — PASS — No dangerous adapter execution boundary**

Implemented and verified within the declared offline scope. Evidence: [docs/threat-model.md](docs/threat-model.md), [tests/security](tests/security), [tests/integration/test_coverage_privacy.py](tests/integration/test_coverage_privacy.py), [.github/workflows/checks.yml](.github/workflows/checks.yml), [dependency-lock-hashed.txt](dependency-lock-hashed.txt).


### Original section 21

**21.01 — PASS — Complete package metadata and policy files**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [pyproject.toml](pyproject.toml), [docs](docs), [src](src), [schemas](schemas), [contracts](contracts), [corpus](corpus), [tests](tests), [fuzz](fuzz), [examples](examples), [evidence](evidence), [.github](.github).

**21.02 — PASS — Source modules and supported extractors**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [pyproject.toml](pyproject.toml), [docs](docs), [src](src), [schemas](schemas), [contracts](contracts), [corpus](corpus), [tests](tests), [fuzz](fuzz), [examples](examples), [evidence](evidence), [.github](.github).

**21.03 — PASS — Schemas/contracts/corpus/tests/fuzz/examples**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [pyproject.toml](pyproject.toml), [docs](docs), [src](src), [schemas](schemas), [contracts](contracts), [corpus](corpus), [tests](tests), [fuzz](fuzz), [examples](examples), [evidence](evidence), [.github](.github).

**21.04 — PASS — Architecture/security/reproduction/contributor documentation**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [pyproject.toml](pyproject.toml), [docs](docs), [src](src), [schemas](schemas), [contracts](contracts), [corpus](corpus), [tests](tests), [fuzz](fuzz), [examples](examples), [evidence](evidence), [.github](.github).

**21.05 — PASS — Evidence inventory and GitHub preparation files**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [pyproject.toml](pyproject.toml), [docs](docs), [src](src), [schemas](schemas), [contracts](contracts), [corpus](corpus), [tests](tests), [fuzz](fuzz), [examples](examples), [evidence](evidence), [.github](.github).


### Original section 22

**22.01 — PASS — README starts with reproducible schema-valid-loss demo**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.02 — PASS — Problem and non-goals**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.03 — PASS — Quickstart**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.04 — PASS — Exact namespaces**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.05 — PASS — Tested and unexamined fields**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.06 — PASS — Security and limitations**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.07 — PASS — No-certification disclaimer**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.08 — PASS — Sample output**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.09 — PASS — Architecture diagram**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.10 — PASS — File-handoff integration**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.11 — PASS — Contribution instructions**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).

**22.12 — PASS — Amharic introduction omitted rather than unreviewed machine translation**

English engineering documentation is complete; the optional reviewed Amharic introduction is intentionally omitted as the mandate permits. Evidence: [README.md](README.md), [docs/quickstart.md](docs/quickstart.md), [docs/fields.md](docs/fields.md).


### Original section 23

**23.01 — PASS — Original code Apache-2.0**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.02 — PASS — Original synthetic fixtures Apache-2.0**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.03 — PASS — Rights register with source/version/hash/terms/status/modification/decision**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.04 — PASS — No paid ISO publications**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.05 — PASS — No proprietary SWIFT usage profiles**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.06 — PASS — No commercial BIC directories**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.07 — PASS — No vendor fixtures**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.08 — PASS — No private EATS/EthSwitch specifications**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.09 — PASS — Uncertain camt asset excluded**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.10 — PASS — Useful zero-fee default repository**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).

**23.11 — PASS — Native LGPL source/notices/rebuild materials**

Implemented and verified within the declared offline scope. Evidence: [LICENSE](LICENSE), [NOTICE](NOTICE), [evidence/rights-register.json](evidence/rights-register.json), [evidence/dependency-license-policy.json](evidence/dependency-license-policy.json), [evidence/native-source-pins.json](evidence/native-source-pins.json), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [docs/camt053-asset-review.md](docs/camt053-asset-review.md).


### Original section 24

**24.01 — PASS — PR formatting**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.02 — PASS — PR typing**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.03 — PASS — PR unit/golden/property tests**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.04 — PASS — Bounded parser and contract fuzz smoke**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.05 — PASS — Secret scanning**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.06 — PASS — Dependency advisory scanning**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.07 — PASS — Dependency license checks**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.08 — PASS — SAST**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.09 — PASS — Manifest/corpus validation**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.10 — PASS — Actions pinned to commit SHA**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.11 — PASS — Read-only default token**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.12 — PASS — No pull_request_target on contributor code**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.13 — PASS — No secret-dependent PR jobs**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.14 — PASS — Scheduled dependency updates**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.15 — PASS — Longer fuzzing**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.16 — PASS — Scorecard configuration**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.17 — PASS — Protected manual release workflow configuration**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.18 — PASS — Clean build and install check**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.19 — PASS — SBOM/checksums**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.20 — PASS — Sigstore signing and identity verification configuration**

Implemented and verified within the declared offline scope. Evidence: [.github/workflows/checks.yml](.github/workflows/checks.yml), [.github/workflows/security.yml](.github/workflows/security.yml), [.github/workflows/release.yml](.github/workflows/release.yml), [.github/dependabot.yml](.github/dependabot.yml), [evidence/actionlint.txt](evidence/actionlint.txt), [scripts/check_all.py](scripts/check_all.py).

**24.21 — BLOCKED-BY-HUMAN — Actual hosted CI runs and repository protections**

Owner must create/authorize the real repository, configure required reviewers and enable/dispatch the protected workflow. No remote exists in this checkout; no organizational identity or approval is fabricated. Evidence: [scripts/owner_setup.py](scripts/owner_setup.py), [docs/github-publication.md](docs/github-publication.md), [.github/workflows/release.yml](.github/workflows/release.yml).

**24.22 — BLOCKED-BY-HUMAN — Actual human release approval**

Owner must create/authorize the real repository, configure required reviewers and enable/dispatch the protected workflow. No remote exists in this checkout; no organizational identity or approval is fabricated. Evidence: [scripts/owner_setup.py](scripts/owner_setup.py), [docs/github-publication.md](docs/github-publication.md), [.github/workflows/release.yml](.github/workflows/release.yml).

**24.23 — BLOCKED-BY-HUMAN — Actual organization-identity Sigstore signature**

Owner must create/authorize the real repository, configure required reviewers and enable/dispatch the protected workflow. No remote exists in this checkout; no organizational identity or approval is fabricated. Evidence: [scripts/owner_setup.py](scripts/owner_setup.py), [docs/github-publication.md](docs/github-publication.md), [.github/workflows/release.yml](.github/workflows/release.yml).


### Original section 25

**25.01 — PASS — SBOM includes Python and native XML dependencies**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.02 — PASS — Wheel/sdist SHA-256**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.03 — PASS — Source commit and toolchain provenance**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.04 — PASS — Dependency lock hashes**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.05 — PASS — Schema hashes**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.06 — PASS — Contract hashes**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.07 — PASS — Corpus manifest hash**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.08 — PASS — Attempt reproducible unsigned builds**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).

**25.09 — PASS — Claim byte equivalence only on measured matching builds**

Implemented and verified within the declared offline scope. Evidence: [evidence/sbom.cdx.json](evidence/sbom.cdx.json), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py), [scripts/release_provenance.py](scripts/release_provenance.py).


### Original section 26

**26.01 — PASS — All current Passing criteria assessed**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.02 — PASS — Clear license/contribution/build/install/release/security docs**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.03 — PASS — Tests/static/dynamic analysis**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.04 — PASS — Dependency inventory/update process**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.05 — PASS — Threat model and SBOM**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.06 — PASS — Scorecard installed and local checks executed**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.07 — PASS — No badge or score promise**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.08 — PASS — Silver/Gold feasibility pathway**

Implemented and verified within the declared offline scope. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [evidence/openssf-passing-assessment.json](evidence/openssf-passing-assessment.json), [evidence/scorecard-local.json](evidence/scorecard-local.json), [evidence/developer-tool-pins.json](evidence/developer-tool-pins.json).

**26.09 — BLOCKED-BY-HUMAN — Public history and actual human governance controls**

Public account ownership, accountable maintainers, authentic reviews and badge account/application are real owner/human operations. Local files and a source-only Scorecard run cannot establish them. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [docs/github-publication.md](docs/github-publication.md).

**26.10 — BLOCKED-BY-HUMAN — Actual OpenSSF badge application/achievement**

Public account ownership, accountable maintainers, authentic reviews and badge account/application are real owner/human operations. Local files and a source-only Scorecard run cannot establish them. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [docs/github-publication.md](docs/github-publication.md).

**26.11 — BLOCKED-BY-HUMAN — Full public-repository Scorecard execution**

Public account ownership, accountable maintainers, authentic reviews and badge account/application are real owner/human operations. Local files and a source-only Scorecard run cannot establish them. Evidence: [docs/openssf-readiness.md](docs/openssf-readiness.md), [docs/github-publication.md](docs/github-publication.md).


### Original section 27

**27.01 — PASS — Repository description**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.02 — PASS — Topics/tags**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.03 — PASS — Social preview text**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.04 — PASS — About text**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.05 — PASS — Release notes**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.06 — PASS — Bug and feature templates**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.07 — PASS — Security reporting instructions**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.08 — PASS — Contributor and maintainer guides**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.09 — PASS — Prepare for Aksum Labs ownership**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.10 — PASS — Do not publish automatically**

Implemented and verified within the declared offline scope. Evidence: [docs/github-publication.md](docs/github-publication.md), [docs/release-notes-0.2.0-rc.1.md](docs/release-notes-0.2.0-rc.1.md), [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/maintainer-guide.md](docs/maintainer-guide.md), [scripts/owner_setup.py](scripts/owner_setup.py).

**27.11 — BLOCKED-BY-HUMAN — Actual organization ownership/account configuration and publication**

The user requested preparation and human review before publication. Account owner supplies verified organization/maintainer identities and executes the prepared plan. Evidence: [docs/github-publication.md](docs/github-publication.md), [scripts/owner_setup.py](scripts/owner_setup.py).


### Original section 28

**28.01 — PASS — Use approved neutral public positioning**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [NOTICE](NOTICE), [docs/github-publication.md](docs/github-publication.md).

**28.02 — PASS — No official approval/certification/national-standard labels**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [NOTICE](NOTICE), [docs/github-publication.md](docs/github-publication.md).

**28.03 — PASS — No institutional logos**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [NOTICE](NOTICE), [docs/github-publication.md](docs/github-publication.md).


### Original section 29

**29.01 — PASS — Concrete schema-valid semantic-loss baseline**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).

**29.02 — PASS — Parser PASS**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).

**29.03 — PASS — XSD PASS**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).

**29.04 — PASS — Preservation rule FAIL**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).

**29.05 — PASS — Existing-tool overlap disclosed**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).

**29.06 — PASS — Added paired-comparison layer demonstrated**

Implemented and verified within the declared offline scope. Evidence: [evidence/baseline.json](evidence/baseline.json), [docs/prior-art.md](docs/prior-art.md), [README.md](README.md).


### Original section 30

**30.01 — PASS — Gate A executable proposition**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.02 — PASS — Gate B automated correctness/incomplete-evidence behavior**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.03 — PASS — Gate C technical test completeness**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.04 — PASS — Gate D nontrivial language-neutral handoff**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.05 — PASS — Gate E bounded differentiation**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.06 — PASS — Gate F local engineering hygiene**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.07 — PASS — Gate G public-claim safety**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence/corpus-verification.json](evidence/corpus-verification.json), [evidence/mutation-results.json](evidence/mutation-results.json), [evidence/file-handoff.json](evidence/file-handoff.json), [evidence/local-acceptance.json](evidence/local-acceptance.json).

**30.08 — BLOCKED-BY-HUMAN — Gate B/C independent-review portions**

Only genuine independent reviewers and actual owner-controlled hosted settings remain; technical subchecks are separately evidenced. Evidence: [docs/fixture-review.md](docs/fixture-review.md), [docs/github-publication.md](docs/github-publication.md).

**30.09 — BLOCKED-BY-HUMAN — Gate F hosted/human release portions**

Only genuine independent reviewers and actual owner-controlled hosted settings remain; technical subchecks are separately evidenced. Evidence: [docs/fixture-review.md](docs/fixture-review.md), [docs/github-publication.md](docs/github-publication.md).


### Original section 31

**31.01 — PASS — Check exact maintained upstream equivalent stop condition**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).

**31.02 — PASS — Check public-asset rights stop condition**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).

**31.03 — PASS — Check private-rule dependency stop condition**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).

**31.04 — PASS — Check value beyond XSD stop condition**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).

**31.05 — PASS — Check scheme-authority dependency stop condition**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).

**31.06 — PASS — Prepare upstream contingency if a stop condition is established**

No standalone-project stop condition established by bounded investigation. Uncertain camt asset is excluded; core cleared functionality remains useful. No unsolicited upstream outreach. Evidence: [docs/prior-art.md](docs/prior-art.md), [docs/upstream-contingency.md](docs/upstream-contingency.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [evidence/baseline.json](evidence/baseline.json).


### Original section 32

**32.01 — PASS — Full repository**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.02 — PASS — Working package**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.03 — PASS — CLI**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.04 — PASS — Minimum fixture count exceeded**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.05 — PASS — Contracts**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.06 — PASS — Test suite**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.07 — PASS — Coverage report**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.08 — PASS — Mutation evidence**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.09 — PASS — Fuzz/security tests**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.10 — PASS — Benchmark**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.11 — PASS — SBOM**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.12 — PASS — Release artifacts**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.13 — PASS — Checksums**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.14 — PASS — Unsigned provenance artifacts**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.15 — PASS — Documentation**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.16 — PASS — README demo**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.17 — PASS — Prior-art comparison**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.18 — PASS — Rights register**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.19 — PASS — OpenSSF assessment**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.20 — PASS — Gate report**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.21 — PASS — Release-readiness report**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.22 — PASS — Limitations**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.23 — PASS — Exact reproduction commands**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [FINAL_COMPLETION_REPORT.md](FINAL_COMPLETION_REPORT.md), [docs/reproduce.md](docs/reproduce.md), [evidence](evidence), [scripts/reproducible_build.py](scripts/reproducible_build.py), [scripts/prepare_bundle.py](scripts/prepare_bundle.py).

**32.24 — BLOCKED-BY-HUMAN — Identity-backed signed public release artifacts**

Signing tooling and protected job are implemented and linted. Genuine OIDC/account identity and approved execution require the owner; no synthetic signature is misrepresented as Aksum approval. Evidence: [.github/workflows/release.yml](.github/workflows/release.yml), [docs/github-publication.md](docs/github-publication.md).


### Original section 33

**33.01 — PASS — Gate report technical answers**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).

**33.02 — PASS — Correctness counts and measured coverage/mutations**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).

**33.03 — PASS — Security/advisory/SBOM/redaction answers**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).

**33.04 — PASS — Asset rights and remaining human determinations**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).

**33.05 — PASS — OpenSSF met controls and human blockers**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).

**33.06 — PASS — Explicit release decision**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence).


### Original section 34

**34.01 — PASS — Version recommendation**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.02 — PASS — Exact supported namespaces/fields**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.03 — PASS — Unsupported features and limitations**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.04 — PASS — Security/licensing caveats**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.05 — PASS — Allowed and forbidden claims**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.06 — PASS — External-review status**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).

**34.07 — PASS — v1.0 criteria assessment**

Implemented and verified within the declared offline scope. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [LIMITATIONS.md](LIMITATIONS.md), [docs/fields.md](docs/fields.md).


### Original section 35

**35.01 — PASS — Semver-compatible prerelease identifier**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [CHANGELOG.md](CHANGELOG.md), [RELEASE_READINESS.md](RELEASE_READINESS.md).

**35.02 — PASS — Do not call automated completion v1.0**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [CHANGELOG.md](CHANGELOG.md), [RELEASE_READINESS.md](RELEASE_READINESS.md).

**35.03 — PASS — At least 100 scenarios prepared for review**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [CHANGELOG.md](CHANGELOG.md), [RELEASE_READINESS.md](RELEASE_READINESS.md).

**35.04 — PASS — Version boundaries reflect actual capabilities**

Implemented and verified within the declared offline scope. Evidence: [pyproject.toml](pyproject.toml), [CHANGELOG.md](CHANGELOG.md), [RELEASE_READINESS.md](RELEASE_READINESS.md).

**35.05 — BLOCKED-BY-HUMAN — v0.5 three-cleared-version/reviewed-corpus criteria**

No v0.5/v1.0 promotion until actual rights/review/governance requirements are met. Preparing 100 cases is not obtaining 100 independent case approvals. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [docs/fixture-review.md](docs/fixture-review.md).

**35.06 — BLOCKED-BY-HUMAN — v1.0 external review/use/governance and stable-public-API approval**

No v0.5/v1.0 promotion until actual rights/review/governance requirements are met. Preparing 100 cases is not obtaining 100 independent case approvals. Evidence: [RELEASE_READINESS.md](RELEASE_READINESS.md), [docs/camt053-asset-review.md](docs/camt053-asset-review.md), [docs/fixture-review.md](docs/fixture-review.md).


### Original section 36

**36.01 — PASS — Technical value before polish**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).

**36.02 — PASS — Correctness and semantic precision**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).

**36.03 — PASS — Security and corpus before claims**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).

**36.04 — PASS — Reproducibility and rights**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).

**36.05 — PASS — Documentation/release/OpenSSF preparation**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).

**36.06 — PASS — No correctness sacrifice for appearance**

Implemented and verified within the declared offline scope. Evidence: [GATE_REPORT.md](GATE_REPORT.md), [evidence](evidence), [docs/expansion-decision.md](docs/expansion-decision.md).


### Original section 37

**37.01 — PASS — One-command reproducible schema-valid loss demonstration**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/reproduce.md](docs/reproduce.md), [scripts/check_all.py](scripts/check_all.py), [evidence/review-packet.json](evidence/review-packet.json).

**37.02 — PASS — Exact violated rule inspectable**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/reproduce.md](docs/reproduce.md), [scripts/check_all.py](scripts/check_all.py), [evidence/review-packet.json](evidence/review-packet.json).

**37.03 — PASS — Unexamined coverage inspectable**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/reproduce.md](docs/reproduce.md), [scripts/check_all.py](scripts/check_all.py), [evidence/review-packet.json](evidence/review-packet.json).

**37.04 — PASS — Offline verification and honest scope**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/reproduce.md](docs/reproduce.md), [scripts/check_all.py](scripts/check_all.py), [evidence/review-packet.json](evidence/review-packet.json).

**37.05 — PASS — Substance suitable for skeptical technical review**

Implemented and verified within the declared offline scope. Evidence: [README.md](README.md), [docs/reproduce.md](docs/reproduce.md), [scripts/check_all.py](scripts/check_all.py), [evidence/review-packet.json](evidence/review-packet.json).
