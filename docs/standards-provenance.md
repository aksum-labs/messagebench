# Standards and provenance

The [ISO archive](https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive?page=6)
lists pacs.008.001.08 / FIToFICustomerCreditTransferV08 and SWIFT as its submitter.
[Official XSD download](https://www.iso20022.org/message/14231/download) returned HTTP 403
from this environment. The byte-preserved XSD was fetched from the exact mx20022 commit
in schemas/catalog.json. A separate moov-io mirror normalized identically after removing
blank formatting text/comments. It was not shortened to a hand-written sample schema.

[ISO repository IPR policy](https://www.iso20022.org/intellectual-property-rights) and
[SWIFTStandards terms](https://www.iso20022.org/sites/default/files/documents/D7/SWIFTStandards_LIC_OUT_V5_.pdf)
are the recorded rights basis. Royalty-free use/supporting software and sublicensing are
covered in sections 2/4; section 3 restrictions remain. The standard is unmodified, supplied
at no fee, and retains third-party terms. Apache-2.0 applies to original project code/fixtures.
No certification or endorsement is conveyed; the XSD does not include payment-scheme rules.

Other specifications: JSON Schema Draft 2020-12 for owned contracts/manifests; SHA-256 for
identity/integrity; XML Schema 1.0 via mature processors; JUnit-compatible reports; CycloneDX
1.6 dependency inventory. No proprietary usage guidelines, institution specifications,
identifier directories or paid ISO publications are redistributed.

Asset hashes/terms are in evidence/rights-register.json. Independent human provenance review
remains part of the unsatisfied first gate. The legal source documents are provided as a
traceable basis, not relabeled as an OSI-approved license for the standard.
