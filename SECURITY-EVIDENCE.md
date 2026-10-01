# Security evidence — measured controls and boundaries

MessageBench 0.2.0-rc.1 is a public engineering candidate. This distinguishes actual automated evidence, authentic builder identity, independent review and external awards.

## Automated engineering evidence

100 synthetic pairs; 140 tests; 99/102 selected core semantic branches (97.06%); 40/40 defined targeted mutants; agreement on 200 documents across lxml/libxml2 and xmlschema; 100,000 parser fuzz iterations; 10,000 contract mutations. Exact reproduction commands are in docs/reproduce.md. These establish neither real-bank defect rates nor independent review or complete-document preservation.

Runtime disables DTD/entities/XInclude/network resolution, uses resource limits, closed contracts, safe local inputs and redacted/escaped reports, and executes no adapter. See docs/threat-model.md and LIMITATIONS.md. Native components appear in CycloneDX 1.6 SBOM and source/advisory/rights inventories. Python pip-audit does not scan native libraries.

## Actual hosted controls

At commit `2bb62cb1e0dcbbb91d265bb824eda274cbd9b217`, Checks, CodeQL, dependency review, Scorecard, long parser/contract fuzzing and candidate build/signature workflows all succeeded. Run IDs, job/step conclusions and artifact digests are in evidence/hosted-recognition.json. Hosted Checks reproduced 140 tests and 97.06% core branch coverage. Later local documentation/settings changes are not covered by those run IDs.

The public Scorecard result is **6.4/10**, all 18 checks recorded in evidence/scorecard-public.json. Main protection and enforced release-environment review are not yet verified; public response and review history are absent. See docs/github-hardening-report.md.

## Authentic candidate provenance

[Snapshot run 36831373116](https://github.com/aksum-labs/messagebench/actions/runs/36831373116) completed a clean build, two same-host matching unsigned builds, native-inclusive SBOM, fresh offline installation, checksum verification, Cosign signing and exact identity verification. GitHub [attestation 51734116](https://github.com/aksum-labs/messagebench/attestations/51734116) authenticates checksum manifest SHA-256 `f49dc8dc5d04f12b6f48d68438da995ea20adb840aec867252111d6888f6e580`.

Verified identity: `https://github.com/aksum-labs/messagebench/.github/workflows/snapshot.yml@refs/heads/main`; issuer: `https://token.actions.githubusercontent.com`. This authenticates a main-branch snapshot, not a release tag or human approval. Evidence: evidence/hosted-signature-verification.txt. Signed artifact ZIP SHA-256: `d2f57d3b0f4f259b78edfb3dfd5549ecf145192a7fe1eed04a909098c836296e`. Artifact expires 31 October 2026; no durable archive is implied. Verification happened in the hosted signing job, not an independent environment.

## Human review, rights and awards

No independent human review, external adoption, staffed response history, Best Practices badge, OSPS award, DOI or foundation acceptance is claimed. No SLSA level is claimed from provenance. Original code/corpus Apache-2.0; standard XSDs retain separate terms. camt.053 is excluded. Bounded fuzzing is not exhaustive assurance, and resource limits are not an OS sandbox. This project does not operate payments or certify conformance. Use SECURITY.md for private synthetic disclosures.
