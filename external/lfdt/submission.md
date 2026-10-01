# Prepared LFDT Lab Proposal — MessageBench

**Unsubmitted draft; owner approval required.** Date checked: 1 October 2026.

## Mission and scope

Proposed Lab name: MessageBench, subject to naming review. Existing product/name collision and trademark clearance have not been established. Alternatives for counsel discussion: PreservationWorks, PairAssure, MessageRetain; these are unsearched suggestions, not cleared marks or available domains. Buy no domains.

Short description: MessageBench checks whether externally supplied financial-message file pairs preserve the information promised by a versioned engineering contract. It runs offline, executes no adapter, and produces deterministic, redacted reports with explicit coverage limits.

Scope and history: Initial engineering candidate 0.2.0-rc.1 developed by Aksum Labs with coding-agent assistance in September 2026. It supports pacs.008.001.08 and pacs.002.001.10 only. Original Apache-2.0 code, contracts and synthetic cases are available for inspection. No previous organization history, deployments or external maintainers are invented.

Problem: Two messages can both satisfy a schema while a transformation truncates a reference, changes an identifier, or removes a repeated remittance item. The relevant test is a declared relationship between source and target, not just single-message validity.

LFDT mission fit: The possible fit is reusable assurance at interoperability boundaries in financial software that may be used alongside decentralized systems. The tool itself implements **no blockchain, ledger, cryptographic identity or settlement functionality**. Fit is a genuine steward decision and may be weaker than FINOS. Do not embellish decentralized functionality to secure admission.

Relation to existing projects: Hyperledger Cacti connects heterogeneous environments; Besu and Fabric provide execution/ledger systems. MessageBench can check externally emitted financial-message file pairs independently of those systems. It neither replaces nor integrates with them today. No tested compatibility or partnership is claimed. Existing LFDT Labs must be rechecked by the owner at submission; source inspection cannot prove global novelty.

## Lab details

Activity: Software only. Engineering contracts are machine-readable test policies, not Community Specifications or national standards.

Architecture: bounded local files → secure XML/XSD validation → exact-version extraction → typed preservation contracts → coverage classification → deterministic JSON/text/HTML/JUnit and reproducibility hashes. No server, database, cloud, telemetry or adapter execution.

Maturity: 100 synthetic paired cases; 140 passing tests; 99/102 core semantic branches (97.06%); 40/40 targeted mutants killed; 200 XML documents with matching XSD classifications across lxml and xmlschema; 100,000 parser fuzz iterations and 10,000 contract mutations. Version remains 0.2.0-rc.1. Independent human review and outside use are absent. A useful initial benchmark exists, but this is not a mature multi-maintainer project.

License: Original code and synthetic fixtures Apache-2.0. Bundled two-message XSDs retain SWIFTStandards-2005 terms. Those assets are not Apache-2.0 or represented as OSI-approved; LFDT counsel/stewards must determine whether this ancillary standards-asset treatment is acceptable or requires an asset-free packaging boundary. Do not relicense third-party schema bytes.

Initial committers: Owner supplies real GitHub profile URLs for accountable human maintainers. A bot is not an independent reviewer or substitute for a human committer.

Sponsor: No steward or sponsor has agreed. Owner may identify a willing Lab steward after authorized outreach.

Roadmap: Independent review of contracts/corpus; maintain the two-message scope; language-neutral adapter demonstrations; community-selected semantic edge cases; security response and provenance; future schema additions only after cleared rights. No promised camt release date.

## Assets and contribution

Pre-existing repository: https://github.com/aksum-labs/messagebench

No trademark/domain transfer is preauthorized. Existing copyright and third-party asset boundaries must remain traceable. If existing history lacks DCO, a **human with actual contribution authority** must decide whether to obtain sign-offs or prepare the permitted signed-off squash for a separate LFDT import. Do not fabricate retroactive DCO attestations or rewrite this public history to appear compliant. LFDT can discuss a new Lab name if the owner retains the existing brand.

## Contact and additional information

Contact: Owner chooses an organization-controlled public contact or profile. No private personal email is inserted into the public form. Entity signatory: owner supplies a person legally authorized for AKSUM LABS OÜ, only if an asset assignment is proposed.

Evidence: README, docs/reproduce.md, evidence/rights-register.json, evidence/review-packet.json, evidence/scorecard-public.json when earned, SECURITY-EVIDENCE.md, paper/messagebench-benchmark.md. Badge and signature statuses must be read from the current recognition matrix at filing time.

No independent human review or institutional adoption has been established. No certification, production-safety, national-standard or regulator/vendor endorsement claim is made. camt.053.001.08 is excluded because joint-contributor redistribution permission was not established. A PASS covers only listed assertions, never the whole document.

Submission creates a formal representation. Do not file this draft without owner approval of contact, signatory, licensing treatment, DCO disposition, and neutral-governance/transfer choices.
