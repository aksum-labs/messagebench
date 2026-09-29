# Gate 1 independent review packet

Status: **pending**. Author: Codex. Independent human reviewers: none recorded.
The source specification (Part VI §7) calls for two humans to review expected outcomes;
the implementation mandate §3 makes independent review a pre-expansion gate.
An AI self-review, a second parser or passing tests does not establish that review.

Review these six pairs against [the engineering contract](../contracts/pacs008-preserve.json).
All data was authored synthetically for this repository. Names and identifiers are fictional;
the tool has no capability to transmit a message.

| Case | Expected | Reason |
|---|---|---|
| [Identity](../corpus/positive/identity.target.xml) | PASS | Unchanged declared information. |
| [Leading-zero loss](../corpus/negative/leading-zero-loss.target.xml) | FAIL PRESERVE-DEBTOR-ACCOUNT | `0000123400` becomes `123400`; identifiers are strings. |
| [Reference truncation](../corpus/negative/reference-truncated.target.xml) | FAIL PRESERVE-END-TO-END-ID | `INV-2026-000123` becomes `INV-2026-000`. |
| [Repeated remittance removal](../corpus/negative/remittance-removed.target.xml) | FAIL PRESERVE-REMITTANCE | One of two unstructured remittance items is removed. |
| [Regenerated message ID](../corpus/positive/message-id-regenerated.target.xml) | PASS | Contract permits a new nonempty message ID; no equality assertion is made for that ID. |
| [Currency change](../corpus/negative/currency-changed.target.xml) | FAIL PRESERVE-SETTLEMENT-AMOUNT | Numeric value unchanged, ETB becomes USD. |

Each target has its corresponding `*.source.xml` next to it. The unchanged source is also
[here](../corpus/positive/identity.source.xml). Review XML directly, not just report output.
The expectations and rationale were recorded before comparator implementation; their initial
manifest hash is in `evidence/expectations-preimplementation.sha256`. This temporal separation
is useful evidence but is **not** independent authorship.

Review tasks:

1. Check schema provenance and the exact namespace; do not assume an Ethiopian scheme profile.
2. Inspect all twelve files and the five contract assertions; confirm each expected result.
3. Confirm `single` association is valid only for exactly one transaction on each side.
4. Confirm remittance multiplicity matters but order is explicitly disregarded in this contract.
5. Confirm regeneration checks presence, not identity, and the coverage/limitations explain this.
6. Identify omitted information: agent context, account scheme/issuer, names, fees, dates,
   instructed amount, structured remittance and other XML fields are not preservation-checked.
7. Record corrections before changing implementation or expectations; never approve a report
   simply because it agrees with code.

Reproduce from this checkout using `PYTHONPATH=src python -m aksum_messagebench corpus verify`
with the pinned dependencies installed. Exit 0 means the six recorded classifications match;
it does not mean the four deliberately defective transformations passed.

Record review evidence with reviewer identity/role, date, the exact reviewed corpus/contract/XSD
hashes, all six case decisions, any conflicts and their resolution. Put signed-off evidence in
`evidence/reviews/` only when it exists. Do not populate fictional names, credentials or dates.
No institutional affiliation or endorsement is required or implied.
