# MessageBench

```sh
# From this checkout after installing the pinned dependencies (docs/quickstart.md):
PYTHONPATH=src python -m aksum_messagebench compare \
  corpus/negative/reference-truncated.source.xml \
  corpus/negative/reference-truncated.target.xml
```

```text
source XSD: PASS (XSD_VALID)
target XSD: PASS (XSD_VALID)
FAIL PRESERVE-END-TO-END-ID (PRESERVATION_CHANGED)
```

Exit **1** is the expected successful reproduction of the injected defect.
In these public synthetic files, `INV-2026-000123` became `INV-2026-000`.
Default reports deliberately omit values. **Schema-valid does not necessarily mean
transformation-correct.** For the unchanged control, use `corpus/positive/identity.source.xml`
and `corpus/positive/identity.target.xml`; its exit code is 0.

MessageBench helps financial-software engineers test whether message adapters preserve
declared payment information. It runs offline on synthetic fixtures or institution-local
files and produces reproducible, scope-labelled results.

**Status: engineering release candidate `0.2.0rc1`; human approval is required for publication.** There are 100 original
synthetic fixture pairs across two message versions. Independent human review has not occurred.
The owner authorized continued development before that review; see the [decision](docs/expansion-decision.md).
[Gate report](GATE_REPORT.md), [current progress](docs/implementation-progress.md),
[readiness](RELEASE_READINESS.md). No v0.5 or v1.0 claim.

## What it checks

Exact namespaces: `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08` and
`urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10`.
This is an engineering scope choice, not a claim about the versions used by any Ethiopian system.
The default contract uses exactly one transaction per message. The extended contract uses
unique declared transaction IDs; reordering is allowed, and ambiguous or changed key sets
produce incomplete evidence. No amount/name matching heuristic exists.

| Field | Declared semantics |
|---|---|
| `GrpHdr/MsgId` | Nonempty value may be regenerated; equality is not promised. |
| `CdtTrfTxInf/PmtId/EndToEndId` | Exact identifier string. |
| `CdtTrfTxInf/DbtrAcct/Id/Othr/Id` | Exact identifier string, including leading zeros. |
| `CdtTrfTxInf/RmtInf/Ustrd` | Unicode-exact multiset, preserving multiplicity. |
| `CdtTrfTxInf/IntrBkSttlmAmt` and `@Ccy` | Decimal numeric equality AND exact currency. |

The table describes the five-assertion default proof contract. The optional extended contract
adds account scheme/issuer, selected agent identifiers, IBAN alternatives, names and instructed
amount. The pacs.002 contract preserves selected original references, status and reason data.
See the [exact field inventory](docs/fields.md). Only explicitly contracted creation datetimes are compared; fees, structured remittance and
supplementary data remain unexamined or unsupported unless explicitly covered. Coverage counts unexamined leaves/attributes explicitly. XML validity
is not a business-rule or operational-validity claim. The initial narrow account check is
**not** a claim that complete account identity/context survived.

## File handoff and architecture

```text
source.xml → your separately run adapter → target.xml
     └──────────── MessageBench reads these two files ─────┘

bounded reads → secure XML → exact XSD → version-specific facts
→ declarative contract → typed comparisons → coverage → deterministic reports
```

MessageBench does not run adapters. It has no network clients, server, telemetry, database,
account system, payment initiation, routing, settlement, live API, custody, or certification.
No private EATS/EIPS/EthSwitch rules are included. No regulator or vendor endorsement.

## Verify the corpus and reproduce the baseline

```sh
PYTHONPATH=src python -m aksum_messagebench corpus verify corpus/index.json
PYTHONPATH=src python scripts/baseline.py
PYTHONPATH=src python -m pytest -q
```

Corpus verification exit 0 means **all expected classifications match**, including deliberately defective targets. It does not approve four defective transformations or attest independent
review. The baseline script uses the original six-case `corpus/gate1-index.json` and the development-only
`xmlschema` processor. The default corpus command checks all 100 cases with their versioned contracts.

`compare` supports `--format json|text|html|junit` and `--out NEW_FILE`. Existing files are
not overwritten. `inspect` validates a local file. Canonical JSON has stable ordering and
no timestamps. HTML is escaped, static and has no remote assets. JUnit represents required
incomplete checks as errors. `suite` accepts separately produced adapter outputs; `report` converts validated comparison
or suite reports; `regression` compares equivalent evidence scopes. See [file handoff](docs/file-handoff.md)
and the separately run [Node.js synthetic example](examples/file-handoff/README.md).

## Trust boundary

Only local regular files through symlink-free POSIX paths are accepted. Maximum input 5 MiB;
depth 64; 100,000 elements; text node 1 MiB; contract assertions 1,000. DTDs, entities,
XInclude, processing instructions and instance schema-location hints are rejected. The
bundled XSDs are pinned in code and the catalog. Contracts have a closed JSON schema;
no executable logic or downloaded expressions. Linux/Python 3.12 was tested; Windows native
execution fails closed because equivalent file-handle protection is not implemented.

Reports contain metadata and declared field paths, not XML or extracted payment values.
Hashes are metadata, not anonymization. Run unknown files in an institution-controlled
restricted environment; this program is not an operating-system sandbox. See
[threat model](docs/threat-model.md), [limitations](LIMITATIONS.md) and [security](SECURITY.md).

**Pass means only the listed assertions passed for these inputs and versions.**

Original code/fixtures: Apache-2.0. The unmodified ISO XSDs have separate royalty-free
SWIFTStandards terms; do not relabel or sell the standard itself. See [NOTICE](NOTICE) and
[rights register](evidence/rights-register.json). Development downloads happen only during
explicit environment preparation, never while evaluating messages. The tested native XML stack
is a local pinned build; follow [native build instructions](docs/native-build.md). Ordinary
PyPI wheels can contain different native versions. camt.053 assets remain under
[separate rights review](docs/camt053-asset-review.md).

[Contribute](CONTRIBUTING.md) · [Prior art](docs/prior-art.md) ·
[Reproduce evidence](docs/reproduce.md) · [Fixture review](docs/fixture-review.md)
