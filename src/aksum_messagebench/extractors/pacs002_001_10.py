"""Exact pacs.002.001.10 status-report preservation facts, without status decisioning."""

from .pacs008_001_08 import Fact, qualified_path

NAMESPACE = "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10"
VERSION = "0.1.0"
Q = "{" + NAMESPACE + "}"
CONTAINER = Q + "FIToFIPmtStsRpt/"
TRANSACTIONS = CONTAINER + Q + "TxInfAndSts"
FIELDS = {
    "message.id": ("GrpHdr/MsgId", "text", "single"),
    "transactions.original_end_to_end_id": (
        "TxInfAndSts/OrgnlEndToEndId",
        "identifier",
        "per-transaction",
    ),
    "transactions.original_transaction_id": (
        "TxInfAndSts/OrgnlTxId",
        "identifier",
        "per-transaction",
    ),
    "transactions.status": ("TxInfAndSts/TxSts", "text", "per-transaction"),
    "transactions.reason_codes": ("TxInfAndSts/StsRsnInf/Rsn/Cd", "list", "per-transaction"),
    "transactions.reason_text": ("TxInfAndSts/StsRsnInf/AddtlInf", "list", "per-transaction"),
}


def extract(root) -> dict[str, Fact]:
    facts = {}
    for field, (path, kind, _) in FIELDS.items():
        nodes = root.findall(CONTAINER + "/".join(Q + part for part in path.split("/")))
        facts[field] = Fact(
            kind,
            tuple(node.text or "" for node in nodes),
            tuple(qualified_path(node) for node in nodes),
        )
    return facts


def transaction_count(root) -> int:
    return len(root.findall(TRANSACTIONS))
