# FINOS sponsored contribution proposal

Status: READY-FOR-OWNER-APPROVAL. No sponsor, membership or submission is claimed. The free route is a willing existing FINOS Member sponsor, not a membership purchase. Current primary rules: [participation](https://community.finos.org/docs/journey/participate/) and [governance](https://community.finos.org/docs/governance/).

Business problem: Integration QA often validates each message while preservation promises across adapters need separately specified and repeatable tests. Synthetic loss examples demonstrate the distinction; no bank defect prevalence or adoption is measured.

Proposed solution: MessageBench checks whether externally supplied financial-message file pairs preserve the information promised by a versioned engineering contract. It runs offline, executes no adapter, and produces deterministic, redacted reports with explicit coverage limits.

Current state: 0.2.0-rc.1, pacs.008.001.08 and pacs.002.001.10 only. 100 synthetic paired cases; 140 passing tests; 99/102 core semantic branches (97.06%); 40/40 targeted mutants killed; 200 XML documents with matching XSD classifications across lxml and xmlschema; 100,000 parser fuzz iterations and 10,000 contract mutations. Supporting materials: README, contracts, corpus, threat model, rights register, reproduction guide and benchmark paper.

Team: Aksum Labs is the current steward; coding-agent assistance is disclosed. Owner must designate real accountable developers/security maintainers and their contribution availability. No staffed team size or outside contributor commitment is invented.

Roadmap: independently review corpus and contract semantics; maintain exact-version extraction; integrate by file handoff with real upstream adapters; publish scope-labelled evidence; respond to actual community feedback. Cleared schemas only; no operational payments or universal translator.

Contribution commitment proposed for owner approval: retain core Apache-2.0 source/corpus, maintain synthetic reproductions, review compatibility and security, support a transparent issue/PR process. Hours and named maintainers must be supplied by humans before commitment.

Governance: FINOS technical charter and contribution/IP policies apply if accepted; neutral maintainer selection based on real work, public decisions and review. Foundation CLA or corporate authority must be completed by an authorized human. Third-party schema terms cannot be overwritten by a contribution agreement.

Licensing caveat: original materials Apache-2.0; bundled XSDs use separate SWIFTStandards terms. Sponsor and FINOS must assess ancillary schema compatibility before accepting transfer or distribution. camt is excluded.

No independent human review or institutional adoption has been established. No certification, production-safety, national-standard or regulator/vendor endorsement claim is made. camt.053.001.08 is excluded because joint-contributor redistribution permission was not established. A PASS covers only listed assertions, never the whole document.
