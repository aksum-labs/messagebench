# Aksum MessageBench

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

Aksum MessageBench helps financial-software engineers test whether message adapters preserve
declared payment information. It runs offline on synthetic fixtures or institution-local
files and produces reproducible, scope-labelled results.

**Status: Gate 1 proof, `0.1.0a1`; NOT READY FOR PUBLIC RELEASE.** Six fixture pairs and five
assertions demonstrate the proposition. Independent human review required by the mandate
has not occurred. [Gate report](GATE_REPORT.md), [readiness](RELEASE_READINESS.md),
[review packet](docs/fixture-review.md). There is no v0.5 or v1.0 claim.

## What it checks

Exact namespace: `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08`.
This is an engineering scope choice, not a claim about the versions used by any Ethiopian system.
Exactly one transaction per source and target is required for transaction comparisons.

| Field | Declared semantics |
|---|---|
| `GrpHdr/MsgId` | Nonempty value may be regenerated; equality is not promised. |
| `CdtTrfTxInf/PmtId/EndToEndId` | Exact identifier string. |
| `CdtTrfTxInf/DbtrAcct/Id/Othr/Id` | Exact identifier string, including leading zeros. |
| `CdtTrfTxInf/RmtInf/Ustrd` | Unicode-exact multiset, preserving multiplicity. |
| `CdtTrfTxInf/IntrBkSttlmAmt` and `@Ccy` | Decimal numeric equality AND exact currency. |

Account scheme/issuer and agent context, IBAN alternative, names, dates, instructed amount,
fees, structured remittance, supplementary data and all other fields are **not** covered by
these five assertions. Coverage counts unexamined leaves/attributes explicitly. XML validity
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

## Reproduce the six-case proof

```sh
PYTHONPATH=src python -m aksum_messagebench corpus verify corpus/index.json
PYTHONPATH=src python scripts/baseline.py
PYTHONPATH=src python -m pytest -q
```

Corpus verification exit 0 means **all expected classifications match**, including four
expected failures. It does not approve four defective transformations or attest independent
review. The baseline script also uses the development-only `xmlschema` processor.

`compare` supports `--format json|text|html|junit` and `--out NEW_FILE`. Existing files are
not overwritten. `inspect` validates a local file. Canonical JSON has stable ordering and
no timestamps. HTML is escaped, static and has no remote assets. JUnit represents required
incomplete checks as errors. `suite`, `report` and `regression` commands, keyed batches,
other message versions, and a reviewed 24/60-case release corpus are deferred behind Gate 1.

## Trust boundary

Only local regular files through symlink-free POSIX paths are accepted. Maximum input 5 MiB;
depth 64; 100,000 elements; text node 1 MiB; contract assertions 1,000. DTDs, entities,
XInclude, processing instructions and instance schema-location hints are rejected. The
single bundled XSD is pinned in code and the catalog. Contracts have a closed JSON schema;
no executable logic or downloaded expressions. Linux/Python 3.12 was tested; Windows native
execution fails closed because equivalent file-handle protection is not implemented.

Reports contain metadata and declared field paths, not XML or extracted payment values.
Hashes are metadata, not anonymization. Run unknown files in an institution-controlled
restricted environment; this program is not an operating-system sandbox. See
[threat model](docs/threat-model.md), [limitations](LIMITATIONS.md) and [security](SECURITY.md).

**Pass means only the listed assertions passed for these inputs and versions.**

Original code/fixtures: Apache-2.0. The unmodified ISO XSD has separate royalty-free
SWIFTStandards terms; do not relabel or sell the standard itself. See [NOTICE](NOTICE) and
[rights register](evidence/rights-register.json). Development downloads happen only during
explicit environment preparation, never while evaluating messages.

[Contribute](CONTRIBUTING.md) · [Prior art](docs/prior-art.md) ·
[Reproduce evidence](docs/reproduce.md) · [Fixture review](docs/fixture-review.md)
