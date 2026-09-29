"""Gate 1 facts for pacs.008.001.08. No local-name matching or heuristic association."""

import hashlib
from dataclasses import dataclass

from lxml import etree

from ..schema_catalog import NAMESPACE

VERSION = "0.1.0"
Q = "{" + NAMESPACE + "}"
FIELDS = {
    "message.id": ("GrpHdr/MsgId", "text", "single"),
    "transactions.debtor_account": (
        "CdtTrfTxInf/DbtrAcct/Id/Othr/Id",
        "identifier",
        "per-transaction",
    ),
    "transactions.end_to_end_id": ("CdtTrfTxInf/PmtId/EndToEndId", "identifier", "per-transaction"),
    "transactions.remittance": ("CdtTrfTxInf/RmtInf/Ustrd", "list", "per-transaction"),
    "transactions.settlement_amount": ("CdtTrfTxInf/IntrBkSttlmAmt", "money", "per-transaction"),
}


@dataclass(frozen=True)
class Fact:
    kind: str
    values: tuple
    paths: tuple[str, ...]

    @property
    def presence(self) -> str:
        if not self.values:
            return "absent"
        return "present-empty" if self.values == ("",) else "present-value"


def qualified_path(element) -> str:
    components = []
    node = element
    while node is not None:
        parent = node.getparent()
        index = 1
        if parent is not None:
            for sibling in parent:
                if sibling is node:
                    break
                if sibling.tag == node.tag:
                    index += 1
        components.append(f"{node.tag}[{index}]")
        node = parent
    return "/" + "/".join(reversed(components))


def extract(root) -> dict[str, Fact]:
    facts = {}
    for key, (path, kind, _) in FIELDS.items():
        nodes = root.findall(Q + "FIToFICstmrCdtTrf/" + "/".join(Q + p for p in path.split("/")))
        paths = []
        values: list[str | tuple[str, str | None]] = []
        for node in nodes:
            paths.append(qualified_path(node))
            if kind == "money":
                values.append((node.text or "", node.get("Ccy")))
                paths.append(qualified_path(node) + "/@Ccy")
            else:
                values.append(node.text or "")
        facts[key] = Fact(kind, tuple(values), tuple(paths))
    return facts


def transaction_count(root) -> int:
    return len(root.findall(Q + "FIToFICstmrCdtTrf/" + Q + "CdtTrfTxInf"))


def inventory(root) -> dict[str, str]:
    """Linear traversal with incremental path hashing, bounded by input quotas."""
    result = {}

    def walk(node, path_hash):
        namespace = etree.QName(node).namespace or ""
        if len(node) == 0:
            result[path_hash.hexdigest()] = namespace
        for attr in node.attrib:
            attribute_hash = path_hash.copy()
            attribute_hash.update(("/@" + attr).encode("utf-8"))
            result[attribute_hash.hexdigest()] = etree.QName(attr).namespace or namespace
        counts: dict[str, int] = {}
        for child in node:
            counts[child.tag] = counts.get(child.tag, 0) + 1
            child_hash = path_hash.copy()
            child_hash.update(
                ("/" + child.tag + "[" + str(counts[child.tag]) + "]").encode("utf-8")
            )
            walk(child, child_hash)

    walk(root, hashlib.sha256(("/" + root.tag + "[1]").encode("utf-8")))
    return result
