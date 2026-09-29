# Independent fixture review handoff

**Status: BLOCKED-BY-HUMAN.** No independent human review is asserted. The owner authorized
continued development, not fabrication of reviewer decisions. All technical preparation is complete.

The packet covers all 100 source/target pairs, their expected outcomes, controls, exact input
hashes, contracts, schemas, extractor source and rights notices. It includes the original six
Gate 1 pairs unchanged. Thirteen generated safety/workflow scenarios have positive controls
and separate evidence in evidence/security-corpus.json.

Preparation and verification:

```sh
python scripts/review_packet.py prepare
python scripts/review_packet.py verify
# Expected exit 3 until two genuine independent human approvals are recorded.
```

Reviewers should first read README.md, docs/contracts.md, docs/fields.md, the threat model,
rights register and camt exclusion decision. Verify input/asset hashes, inspect the exact
XSD and declared comparator semantics, then determine expected outcomes without trusting
the implementation output. Run the corpus and baseline only after recording that judgment.
Pay particular attention to zeros, issuer/institution context, multiplicity, normalization,
key uniqueness, fractional time precision, permitted regeneration and unexamined information.

Each reviewer copies docs/reviewer-form.template.json to `reviews/<real-handle>.json`, supplies
a real handle/date, explicitly attests human authorship and independence, and replaces every
NOT_REVIEWED decision with APPROVE or REQUEST_CHANGES. Approve rights/scope only if actually
reviewed. Do not use fictional identities or AI-generated approval forms. Record disagreements
and fixes in a reviewed change; regenerate the packet and repeat affected approvals when an
asset changes. Do not change expected answers merely to agree with the implementation.

The verification tool rejects wrong hashes, duplicate handles, absent attestations and any
unapproved case. A syntactically valid form does **not** authenticate identity, expertise or
independence. The accountable release approver must verify those facts through the actual
review process. The protected signing job runs this checker but does not replace human judgment.

No request has been sent to anyone. The next human action is to perform the prepared review,
not to design a review process or create missing engineering artifacts.
