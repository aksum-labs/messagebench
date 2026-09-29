# Gate report — 29 September 2026

**Release decision: NOT READY — FIX REQUIRED.**

Deliverable: local `0.1.0a1` Gate 1 proof and review packet. The A–Z/v0.5 mandate has **not**
been completed. Expansion stopped at the mandatory independent-human-review gate, not at an
arbitrary time/token budget. No GitHub repository or public package was published.

## Technical proposition

Gate A's executable proposition passes: four meaningful losses are detected while both
files remain well-formed and pass the full exact-version XSD. They are leading-zero debtor
account loss, end-to-end reference truncation, one repeated remittance item removed, and
currency changed with numeric amount preserved. Identity and permitted regenerated message
ID controls pass. No proprietary scheme rule is involved.

The Python XML parser, lxml/libxml2 XSD processor, separate `xmlschema` processor, and inspected
Cognis lint engine accept these targets. That is expected for their different scopes, not a
finding that those tools are defective. `evidence/baseline.json` records exact input hashes,
processor versions and Cognis source hash. Other named prior-art tools were source-inspected,
not executed. See docs/prior-art.md for overlap and limitations.

The proposed contribution is a portable paired-file preservation oracle with explicit
comparison semantics, reviewed reusable corpus, scope accounting and deterministic reports.
Parsing, loss warnings, round-trip tests and rule coverage already exist elsewhere. The
independent-review portion of the contribution is still missing.

**Full Acceptance Gate 1: NOT SATISFIED.** The six pairs have no independent human reviewers.
The build specification calls for two human reviewers; no human/AI independence is fabricated.
Expected outcomes were recorded before implementation and retained unchanged, which is useful
provenance but does not satisfy that prerequisite. See GATE_FAILURE.md and docs/fixture-review.md.

## Correctness evidence

- Corpus: **6 pairs / 12 XML files**; **6/6** pre-recorded classifications match (4 failure, 2 pass).
- Independent fixture-review count: **0**; the corpus is not called independently reviewed.
- Assertions: **5** (4 preservation rules, 1 permitted-regeneration rule).
- Version: **pacs.008.001.08 only**; no pacs.002/camt.053 support claim.
- Test items: **91 passing**, including unit, integration, golden, property and parser/contract
  fuzz-smoke tests; Hypothesis settings are visible in tests/property/test_invariants.py.
- Comparator/extractor branch coverage: **53/54 = 98.15%**, measured with coverage.py.
  Whole-package branch coverage is **178/220 = 80.91%**; do not substitute one metric for the other.
- Mutation results: **5/5 targeted oracle mutations killed**. Four bypass preservation assertions;
  one wrongly forbids permitted regeneration. This is not a whole-program mutation score.
- Golden hashes: all six canonical result hashes pinned; no timestamps or input values in results.
- Security regressions: DTD including UTF-16, entities, remote resources, XInclude, schema hints,
  depth/text/size/name limits, symlink/FIFO/traversal, malicious contract fields, report escaping.
- Known issue fixed: parser cleanup masking explicit safety-rejection codes.
- No unresolved failing test is known in this scope; absence of independent review and deferred
  features remain material limitations, not completed work.

## Gates B–G

| Gate | Result | Reason |
|---|---|---|
| B correctness | PARTIAL | Author-recorded expectations match; required unknown/incomplete evidence blocks PASS. Independent review outstanding. |
| C completeness | PARTIAL | Initial assertion/control mutations and deterministic safety tests pass; release corpus/review targets not met. |
| D portability | PARTIAL | File boundary has no adapter-language dependency. No independently implemented external adapter use demonstrated. |
| E differentiation | SUPPORTED, bounded | Pair-preservation proof exceeds parser/XSD/lint baselines; selected source review found no exact bundled workflow. No exhaustive absence/comparable-effort proof. |
| F release hygiene | NOT PASSED | Local checks/artifacts/SBOM exist; public CI, signing, native-advisory review, maintained disclosure channel and approvals are not established. |
| G claims | PASS for local packet | Narrow versions/scope, no official/regulator/vendor/certification claims, limitations visible. |

## Security and rights

Threat model: docs/threat-model.md. Python dependency scan: **54 packages, zero known advisories**
in this run; `evidence/dependency-audit.json`. This does not include complete native libxml2/libxslt
advisory coverage and is not a proof of absence of exploitable vulnerabilities. Native versions
are included in `evidence/sbom.cdx.json`; their advisory review is still pending. SAST is in
`evidence/bandit.json`; its low-severity XML import finding is a renderer-only use, not an XML
parser entry point, and is documented in docs/release-verification.md.

XML hardening and default report redaction have tests. Runtime has no network/adapters/plugins.
The application is not an OS sandbox; no hard process CPU/RSS limit is implemented.

Bundled external assets: unmodified full pacs.008.001.08 XSD, its SWIFTStandards license PDF,
and Apache-2.0 license text. Origins/hashes/terms/inclusion decisions are in the rights register.
ISO XSD terms remain separate; paid/proprietary/vendor/customer material is excluded. Official
schema download returned 403, so pinned mirrors were used and structural equivalence checked.
Independent human provenance review is outstanding; no vague Apache relicensing claim is made.

## OpenSSF and release

No Best Practices badge or Scorecard result. Prepared controls and missing public/governance
criteria are in docs/openssf-readiness.md. No invented maintainer credentials, review signatures,
branch protection, CI pass or signing identity. Local wheel/sdist and offline bundle are for
review only. Reproducible-build measurements/checksums are supplied with the local artifacts;
only the actually measured unsigned artifact equivalence may be claimed.

Next required action: two independent human fixture/provenance reviews of the hashed six-case
packet. Then continue the authorized implementation toward a rigorous 24-case v0.1 and, if
all subsequent gates pass, three-version/60-reviewed-case v0.5. If reviewers establish a
maintained equivalent, use docs/upstream-contingency.md instead. See docs/reproduce.md for commands.
