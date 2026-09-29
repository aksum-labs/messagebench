# Gate report — 29 September 2026

**Release decision: NOT READY — FIX REQUIRED.**

Delivered: local 0.1.0a2 engineering alpha candidate, with 68 synthetic pairs, two message
versions, offline CLI, four report formats and local release tooling. Development continued
under the owner's explicit approval recorded in docs/expansion-decision.md. Independent human
review is still pending; approval to continue is not evidence of such review. Nothing was published.

## Technical proposition

Gate A's executable proposition passes. Four initial defects preserve XML well-formedness
and exact XSD validity: leading-zero account loss, truncated end-to-end reference, removed
repeated remittance item, and changed currency. Identity and permitted regenerated message ID
pass. XML parsing, lxml XSD, the second Python xmlschema processor and the inspected Cognis
lint engine accept the defective targets. Their different scope is not a defect in those tools.
See evidence/baseline.json for input hashes and processor/source versions.

Full initial Gate 1 remains administratively incomplete because independent reviewers have
not signed the hashed six-case packet. Expected classifications were recorded separately from
oracle execution and retained; they are not represented as independent review.

Prowide, mx20022, iso20022-cbpr-ur, Cognis, Mojaloop Testing Toolkit and Pactus overlap in
parsing, validation, translation or testing. Selected source inspection found no exact combined
adapter-neutral paired preservation-contract/corpus workflow at comparable scope. This is a
bounded finding, not exhaustive novelty proof. Reuse lxml/jsonschema rather than rewriting
validation engines. See docs/prior-art.md and the upstream contingency.

## Correctness evidence

- 68 synthetic source/target cases; all recorded classifications match, including intentional failures.
- 3 contracts, 31 assertion declarations, 26 extractable fields; independent fixture reviews: zero.
- Exact families: pacs.008.001.08 and pacs.002.001.10. camt.053.001.08 excluded pending asset rights review.
- 114 passing tests. Core comparator/extractor/association branch coverage: 80/84 (95.24%).
  Whole-package branches: 279/342 (81.58%). See evidence/coverage.json and test-run-current.txt.
- 33/33 targeted oracle/association mutants killed. Not a whole-program mutation score.
- Golden canonical report hashes, property/metamorphic tests, security regressions and 1,000
  deterministic parser fuzz-smoke iterations pass. This is not sustained fuzzing.
- No known unresolved failing test in the delivered scope. Independent audit has not occurred.

| Gate | Result | Evidence or remaining condition |
|---|---|---|
| A technical proposition | PASS executable portion | Four schema-valid losses detected; valid controls pass; no private scheme rules |
| B correctness | PARTIAL | Recorded corpus matches; required unknown/incomplete checks block PASS; independent review pending |
| C completeness | PARTIAL | Required assertion mutations and parser regressions pass; reviewed-corpus criterion pending |
| D portability | PASS scoped demonstration | Separate Node.js synthetic adapter hands off files without modifying MessageBench; not independent external adoption |
| E differentiation | SUPPORTED, bounded | Beyond parser/XSD baselines; honest prior-art inspection, no global absence proof |
| F release hygiene | PARTIAL | Local tests, locks, SBOM, source/licensing inventory and workflows; hosted CI and organizational settings unverified |
| G public claims | PASS local scope | No official standards, certification, endorsement or production-safety claim |

## Security

Threat model: docs/threat-model.md. Python dependency audit: 59 pinned distributions, zero
reported advisories in this run. Bandit reports one LOW renderer-only ElementTree import;
no medium/high finding. XML parsing uses hardened lxml, not that renderer import.

The supplied native wheel uses lxml 6.1.3, libxml2 2.15.4, libxslt 1.1.45 and libiconv 1.19.
Runtime rejects older libxml2/libxslt profiles. Selected primary-source native advisory triage
is in evidence/native-advisory-review.json. No confirmed unresolved critical/high exploitable
finding was identified in these bounded checks; complete historical native vulnerability
coverage and independent security review are not claimed. An advisory-free Python scan alone
is not native-library assurance. There is no hard OS CPU/RSS sandbox.

Default reports omit raw XML, account identifiers, names, values and free text. Hashes are
metadata, not anonymization. XML quotas, entity/DTD/network/XInclude rejection, path defenses,
closed contracts and HTML escaping are tested. No adapter execution or runtime network exists.

## Rights

Original code and synthetic fixtures: Apache-2.0. Two unmodified ISO XSDs are separately covered
by retained SWIFTStandards terms and ISO repository policy; see NOTICE and the full rights
register. The official downloads returned 403, so pinned public mirrors and documented
provenance checks were used. No paid publication or proprietary scheme profile is bundled.

The offline bundle includes original native source archives and rebuild instructions:
lxml BSD-3-Clause, libxml2/libxslt MIT, libiconv LGPL-2.1-or-later. Native LGPL source/notices
must travel with redistribution. camt.053 is excluded because asset-specific redistribution
basis remains unresolved; this is not a claim that redistribution is forbidden.

## Performance and release evidence

Measured 1,000 small pairs: 83.528335 pairs/s; p50 11.408343 ms; p95 15.103128 ms;
peak RSS 40,504 KiB. This includes catalog compilation and cycles six initial pairs on
Linux/WSL2, i9-14900HX, Python 3.12.3. Full environment and method: evidence/benchmark.json.
These are local measurements, not production capacity promises.

The release build script compares two separate clean source-copy wheel/sdist builds. Claim
byte equivalence only when the delivered build-evidence.json says true. Native wheel
reproducibility, independent reproduction and identity-backed signing are not claimed.
Checksums and provenance are integrity evidence, not signatures.

OpenSSF: Passing readiness documentation and scheduled Scorecard workflow prepared; no badge
or actual Scorecard score. Public history, real maintainer/disclosure ownership, branch
protection, required human release approval and hosted CI must be established by the owner.
See docs/openssf-readiness.md and docs/github-publication.md. Public release remains subject
to human review. Exact reproduction commands: docs/reproduce.md.
