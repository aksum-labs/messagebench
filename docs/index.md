# MessageBench documentation

Offline checks for declared information preservation across financial-message adapters.

Start with the [reproducible demo](../README.md), [quickstart](quickstart.md) and [file handoff](../examples/file-handoff/README.md). Two schema-valid messages can still differ in a field the adapter promised to preserve. A PASS covers only the listed assertions.

| Inspect | Reference |
|---|---|
| Exact two-message scope and untested information | [Field inventory](fields.md), [limitations](../LIMITATIONS.md) |
| Architecture and contract semantics | [Architecture](architecture.md), [contracts](contracts.md), [API](api.md) |
| Security and dependency boundaries | [Threat model](threat-model.md), [security evidence](../SECURITY-EVIDENCE.md) |
| Measured benchmark | [Preprint](../paper/messagebench-benchmark.md), [9-page PDF](../paper/messagebench-benchmark.pdf), [2-page brief](../paper/technical-brief.pdf) |
| Public Scorecard and badge status | [Recognition matrix](../external/recognition-matrix.json), [remediation](scorecard-remediation.md), [Best Practices](openssf-best-practices-submission.md) |
| Reproduction and release verification | [Commands](reproduce.md), [offline install](offline-install.md), [verification](release-verification.md) |
| Citation and contribution | [CITATION.cff](../CITATION.cff), [archival](citation-and-archival.md), [contributor guide](../CONTRIBUTING.md) |
| Roadmap and governance | [Release readiness](../RELEASE_READINESS.md), [governance](../GOVERNANCE.md) |

Only pacs.008.001.08 and pacs.002.001.10 are supported. No camt support, institution approval, certification, independent review or whole-document preservation is implied. Roadmap: independent review, actual upstream adapter examples, maintained synthetic edge cases and cleared future assets. No operational payment features are planned.
