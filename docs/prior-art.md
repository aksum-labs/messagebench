# Prior art and the bounded contribution

Review date: 2026-09-29. The GitHub commits API was rechecked with an end-of-day cutoff;
the five heads below match the research snapshots. A recent commit and an unarchived
repository are evidence of activity, not a guarantee of ongoing maintenance.
This is a selected-source inspection, not an exhaustive proof that no equivalent exists.
No claim of inventing loss detection, paired-file testing, XML validation or contract tests.

| Project / inspected commit | Observed capability and overlap | Boundary and reuse decision |
|---|---|---|
| [Prowide ISO 20022](https://github.com/prowide/prowide-iso20022/tree/4f9e43996fca625e5affcb32adb3c03b910c05ab) | Java models, parsing and serialization; broad message coverage. README separates commercial validation offerings. | Do not regenerate a competing model/parser. A future integration can consume Prowide-produced XML. No adapter-independent, declarative pair-preservation contract plus coverage corpus workflow was located in inspected entry points. |
| [mx20022](https://github.com/socrates8300/mx20022/tree/b650c81f60311801f240efea3f9cc6df9adb70f9) | Rust parsing, generated schema constraints, scheme validation, MT/MX translation, round-trip tests and explicit data-loss warnings. | Translation warnings already solve part of the problem inside its translators. Reuse upstream adapters; avoid another translator. Proposed addition: externally supplied file pairs and an adapter-neutral preservation promise that also reports omissions from tested scope. Its translator targets differ from this initial exact version. |
| [iso20022-cbpr-ur](https://github.com/phoughton/iso20022-cbpr-ur/tree/f6a8d27b6ff62ac4c5cc87457cfb1a7058935c26) | Python business-rule packs, advisory outcomes, optional user-supplied XSD, examples, and rule-to-XPath coverage instrumentation. | Coverage reporting itself is not new. Its inspected engine evaluates individual messages against usage rules. Do not copy rule packs with unclear underlying rights. Preserve the distinction between usage validity and a pair-specific declared preservation promise. |
| [Cognis iso20022](https://github.com/cognis-digital/iso20022/tree/d7903979b5dbc74967f93eaa5688d5d5db984b06) | Inspected `iso20022/core.py`, `cli.py`, smoke tests: standard-library XML parsing and lint checks for identifiers, amounts, dates and counts. | Repository description mentions diff/translation; the inspected CLI exposes `validate` and does not implement the full advertised paired-preservation workflow. Run as a concrete single-message lint baseline; do not equate marketing text with verified functionality. |
| [Mojaloop Testing Toolkit](https://github.com/mojaloop/ml-testing-toolkit/tree/bd1bc7e90e4c9cc84b606b868a04dfd744f6338b) | Rich API/scenario testing and FSP/hub onboarding, with FSPIOP/ISO transformation facades. | Reuse TTK for Mojaloop protocol/integration tests. Rebuilding it is unjustified. Our proposed boundary is offline supplied XML pairs, without simulating a hub or calling APIs. General test frameworks can express assertions; “not built in” does not mean “impossible.” |

Inspected handles:

- Prowide: `README.md`, repository tree, license; commercial scope not executed.
- mx20022: `crates/mx20022-translate/src/lib.rs`, `tests/translation.rs`,
  `crates/mx20022-parse/tests/roundtrip*.rs`, validation source and CLI entry points.
- CBPR-UR: `src/cbpr_rules/engine.py` (`_validate_tree`, `rule_xpaths`), `schema.py`.
- Cognis: `iso20022/core.py` (`validate_string`), `cli.py` (`_build_parser`), smoke tests.
- Mojaloop: `src/lib/mocking/transformers/fspiopToISO20022.js`, toolkit guide and README.

Source hashes and exact commits are recorded in `evidence/prior-art-snapshots.json`.
Cognis baseline execution, when generated, is in `evidence/baseline.json`; the other four
projects were source-inspected, not installed or benchmarked. No universal comparison claim.

## Decision before expansion

There is a plausible gap in the **combination** of explicit pair-preservation semantics,
adapter-independent file handoff, a reusable independently reviewed corpus, honest coverage,
and deterministic redacted evidence. The small executable proof demonstrates the pair oracle;
the independent corpus review has **not** happened. Thus differentiation is supported for the
proof, not yet established for a public standalone release at comparable engineering effort.

If reviewers identify an equivalent maintained workflow, stop expansion. Propose original
synthetic pairs and a preservation-contract extension upstream. Prioritize mx20022 for adapter
examples and round-trip evidence, CBPR-UR for separation of applicability and preservation,
or Mojaloop when the actual need is protocol testing. Do not send a proposal without user
authorization. No upstream outreach or contribution has been made in this sprint.

## Additional follow-up: Pactus / iso20022-mcp

Inspected 29 September 2026 at commit
[`634f3bff3b2927653427835c48ee03f3577191df`](https://github.com/deniskarlinsky/iso20022-mcp/tree/634f3bff3b2927653427835c48ee03f3577191df)
(committed 12 May 2026). The README, Python source tree,
[`core/validators.py`](https://github.com/deniskarlinsky/iso20022-mcp/blob/634f3bff3b2927653427835c48ee03f3577191df/src/pactus/core/validators.py)
and MCP tool registration were inspected. Its four message parsers and four XSD validators
are useful overlapping infrastructure. Validation takes one XML document and uses lxml
XMLSchema; the inspected MCP interface has no paired preservation-contract or coverage
accounting tool. This is source inspection, not an execution benchmark or proof about all
future releases. Do not rebuild its MCP assistant interface here; reuse upstream parsing
models if a future integration needs them. MessageBench's bounded paired-file oracle,
explicit contract semantics and declared-coverage reports remain a different contribution.
