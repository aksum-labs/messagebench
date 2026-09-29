"""Exact, declared transaction association; never match by amount or party name."""

from .comparators import compare_fact
from .extractors.pacs008_001_08 import FIELDS, Fact, Q, qualified_path


def transactions(root) -> list:
    return root.findall(Q + "FIToFICstmrCdtTrf/" + Q + "CdtTrfTxInf")


def transaction_fact(node, field: str) -> Fact:
    path, kind, _ = FIELDS[field]
    relative = path.split("/")[1:]
    nodes = node.findall("/".join(Q + part for part in relative))
    values: list[str | tuple[str, str | None]] = []
    paths = []
    for value in nodes:
        location = qualified_path(value)
        paths.append(location)
        if kind == "money":
            values.append((value.text or "", value.get("Ccy")))
            paths.append(location + "/@Ccy")
        else:
            values.append(value.text or "")
    return Fact(kind, tuple(values), tuple(paths))


def index_transactions(root, keys: list[str]) -> tuple[dict, str | None]:
    index: dict = {}
    if not keys or len(keys) != len(set(keys)):
        return index, "ASSOCIATION_KEYS_INVALID"
    if any(
        key not in FIELDS or FIELDS[key][1:] != ("identifier", "per-transaction") for key in keys
    ):
        return index, "ASSOCIATION_KEY_UNSUPPORTED"
    for node in transactions(root):
        facts = [transaction_fact(node, key) for key in keys]
        if any(len(fact.values) != 1 or not fact.values[0] for fact in facts):
            return {}, "ASSOCIATION_KEY_MISSING"
        key = tuple(fact.values[0] for fact in facts)
        if key in index:
            return {}, "ASSOCIATION_KEY_AMBIGUOUS"
        index[key] = node
    if not index:
        return {}, "ASSOCIATION_NO_ITEMS"
    return index, None


def compare_keyed(source, target, assertion: dict, keys: list[str]) -> tuple[str, str]:
    before, left_error = index_transactions(source, keys)
    after, right_error = index_transactions(target, keys)
    if left_error or right_error:
        return "INDETERMINATE", left_error or right_error or "ASSOCIATION_INVALID"
    if before.keys() != after.keys():
        return "INDETERMINATE", "ASSOCIATION_KEY_SET_CHANGED"
    results = [
        compare_fact(
            transaction_fact(before[key], assertion["field"]),
            transaction_fact(after[key], assertion["field"]),
            assertion,
        )
        for key in sorted(before)
    ]
    # A partial result cannot imply that every associated item was examined.
    for status in ("UNSUPPORTED", "INDETERMINATE", "FAIL"):
        for result in results:
            if result[0] == status:
                return result
    return "PASS", "KEYED_ITEMS_PRESERVED"
