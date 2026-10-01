# Security evidence — measured controls and boundaries

MessageBench 0.2.0-rc.1 is an engineering candidate. This page distinguishes actual automated evidence from human review, authentic builder identity and external awards.

## Automated engineering evidence

100 synthetic pairs; 140 passing tests; 99/102 selected core semantic branches; 40/40 defined targeted mutants; agreement on 200 documents across lxml/libxml2 and xmlschema; 100,000 parser fuzz iterations; 10,000 contract mutations. Evidence files and exact reproduction commands are in docs/reproduce.md. These results do not establish real-bank defect rates, independent review or complete-document preservation.

The runtime disables XML DTD/entities/XInclude/network resolution, uses resource limits, closed contracts, safe local inputs and redacted/escaped reports, and executes no adapter. See docs/threat-model.md and LIMITATIONS.md. Native components appear in CycloneDX 1.6 SBOM and source/advisory/rights inventories. Python pip-audit does not scan native libraries.

## Hosted controls and provenance

Actual hosted run IDs, commits, artifact hashes and conclusions are recorded in evidence/hosted-recognition.json when available. Historical Checks run 36739025005 passed at commit 2267eb3b42126fe65a87468d73e07b5218999626; it is not evidence for a later commit or every new workflow. CodeQL, dependency review, public Scorecard, snapshot build/offline installation and OIDC signing are configured separately; configured files alone are not successful executions.

A snapshot signature authenticates its exact workflow/ref and checksum manifest. It does not attest independent technical review or approval of a formal release. Formal release.yml preserves its independent-review gate. No SLSA level is claimed from provenance alone. Two matching unsigned builds in one environment are not independent reproduction.

## Review, badges and operational limits

No authenticated independent human review, outside adoption, staffed response history or official institutional approval is claimed. No Best Practices badge or baseline certification is obtained merely by a checklist. Actual Scorecard/badge status is in external/recognition-matrix.json. Public platform controls are read back in evidence/github-settings.json.

Original code/corpus Apache-2.0; standard XSDs retain separate terms. camt.053 is excluded. Resource limits are not an OS sandbox and fuzzing is bounded. This project does not operate payments or certify conformance. Use SECURITY.md for synthetic private disclosures and do not upload customer inputs.
