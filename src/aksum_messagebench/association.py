"""Exact, declared transaction association; never match by amount or party name."""

from .comparators import compare_fact
from .extractors import pacs008_001_08 as default_extractor
from .extractors.pacs008_001_08 import Fact, qualified_path


def transactions(root, extractor=default_extractor) -> list:
    return root.findall(extractor.TRANSACTIONS)


def transaction_fact(node, field: str, extractor=default_extractor) -> Fact:
    path, kind, _ = extractor.FIELDS[field]
    relative = path.split("/")[1:]
    nodes = node.findall("/".join(extractor.Q + part for part in relative))
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


def index_transactions(
    root, keys: list[str], extractor=default_extractor
) -> tuple[dict, str | None]:
    fields = extractor.FIELDS
    index: dict = {}
    if not keys or len(keys) != len(set(keys)):
        return index, "ASSOCIATION_KEYS_INVALID"
    if any(
        key not in fields or fields[key][1:] != ("identifier", "per-transaction") for key in keys
    ):
        return index, "ASSOCIATION_KEY_UNSUPPORTED"
    for node in transactions(root, extractor):
        facts = [transaction_fact(node, key, extractor) for key in keys]
        if any(len(fact.values) != 1 or not fact.values[0] for fact in facts):
            return {}, "ASSOCIATION_KEY_MISSING"
        key = tuple(fact.values[0] for fact in facts)
        if key in index:
            return {}, "ASSOCIATION_KEY_AMBIGUOUS"
        index[key] = node
    if not index:
        return {}, "ASSOCIATION_NO_ITEMS"
    return index, None


def compare_keyed(
    source, target, assertion: dict, keys: list[str], extractor=default_extractor
) -> tuple[str, str]:
    before, left_error = index_transactions(source, keys, extractor)
    after, right_error = index_transactions(target, keys, extractor)
    if left_error or right_error:
        return "INDETERMINATE", left_error or right_error or "ASSOCIATION_INVALID"
    if before.keys() != after.keys():
        return "INDETERMINATE", "ASSOCIATION_KEY_SET_CHANGED"
    item_assertion = assertion
    if assertion["comparator"] == "keyed-items":
        item_assertion = {**assertion, "comparator": assertion["item_comparator"]}
    results = [
        compare_fact(
            transaction_fact(before[key], assertion["field"], extractor),
            transaction_fact(after[key], assertion["field"], extractor),
            item_assertion,
        )
        for key in sorted(before)
    ]
    # A partial result cannot imply that every associated item was examined.
    for status in ("UNSUPPORTED", "INDETERMINATE", "FAIL"):
        for result in results:
            if result[0] == status:
                return result
    return "PASS", "KEYED_ITEMS_PRESERVED"
