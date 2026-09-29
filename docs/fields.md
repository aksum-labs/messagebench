# Exact extractable field inventory

Extractability does not mean a contract examines a field. Read the actual assertions and coverage report.

## urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08

| Field | Relative QName path (namespace above) | Type | Scope |
|---|---|---|---|
| `message.id` | `GrpHdr/MsgId` | text | single |
| `transactions.debtor_account` | `CdtTrfTxInf/DbtrAcct/Id/Othr/Id` | identifier | per-transaction |
| `transactions.end_to_end_id` | `CdtTrfTxInf/PmtId/EndToEndId` | identifier | per-transaction |
| `transactions.remittance` | `CdtTrfTxInf/RmtInf/Ustrd` | list | per-transaction |
| `transactions.settlement_amount` | `CdtTrfTxInf/IntrBkSttlmAmt` | money | per-transaction |
| `transactions.transaction_id` | `CdtTrfTxInf/PmtId/TxId` | identifier | per-transaction |
| `transactions.instruction_id` | `CdtTrfTxInf/PmtId/InstrId` | identifier | per-transaction |
| `transactions.debtor_account_iban` | `CdtTrfTxInf/DbtrAcct/Id/IBAN` | identifier | per-transaction |
| `transactions.debtor_account_scheme_code` | `CdtTrfTxInf/DbtrAcct/Id/Othr/SchmeNm/Cd` | identifier | per-transaction |
| `transactions.debtor_account_scheme_proprietary` | `CdtTrfTxInf/DbtrAcct/Id/Othr/SchmeNm/Prtry` | identifier | per-transaction |
| `transactions.debtor_account_issuer` | `CdtTrfTxInf/DbtrAcct/Id/Othr/Issr` | identifier | per-transaction |
| `transactions.debtor_agent_bic` | `CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI` | identifier | per-transaction |
| `transactions.debtor_agent_other_id` | `CdtTrfTxInf/DbtrAgt/FinInstnId/Othr/Id` | identifier | per-transaction |
| `transactions.creditor_account` | `CdtTrfTxInf/CdtrAcct/Id/Othr/Id` | identifier | per-transaction |
| `transactions.creditor_account_iban` | `CdtTrfTxInf/CdtrAcct/Id/IBAN` | identifier | per-transaction |
| `transactions.creditor_account_issuer` | `CdtTrfTxInf/CdtrAcct/Id/Othr/Issr` | identifier | per-transaction |
| `transactions.creditor_agent_bic` | `CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI` | identifier | per-transaction |
| `transactions.debtor_name` | `CdtTrfTxInf/Dbtr/Nm` | text | per-transaction |
| `transactions.creditor_name` | `CdtTrfTxInf/Cdtr/Nm` | text | per-transaction |
| `transactions.instructed_amount` | `CdtTrfTxInf/InstdAmt` | money | per-transaction |

## urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10

| Field | Relative QName path (namespace above) | Type | Scope |
|---|---|---|---|
| `message.id` | `GrpHdr/MsgId` | text | single |
| `transactions.original_end_to_end_id` | `TxInfAndSts/OrgnlEndToEndId` | identifier | per-transaction |
| `transactions.original_transaction_id` | `TxInfAndSts/OrgnlTxId` | identifier | per-transaction |
| `transactions.status` | `TxInfAndSts/TxSts` | text | per-transaction |
| `transactions.reason_codes` | `TxInfAndSts/StsRsnInf/Rsn/Cd` | list | per-transaction |
| `transactions.reason_text` | `TxInfAndSts/StsRsnInf/AddtlInf` | list | per-transaction |

Nested association among individual reason-code/text blocks is not promised by independent multiset assertions.
No calendar conversion, fee analytics, balance computation or status decisioning is implemented.
