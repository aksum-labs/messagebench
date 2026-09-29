"""Coverage measures examined leaf/attribute occurrences, not business correctness."""

import hashlib

from lxml import etree

from .extractors.pacs008_001_08 import inventory


def account_coverage(root, facts: dict, assertions: list[dict], exclusions: list[dict]) -> dict:
    units = inventory(root)
    examined: set[str] = set()
    for result in assertions:
        if result["status"] in {"PASS", "FAIL"}:
            examined.update(facts[result["field"]].paths if result["field"] in facts else ())
    excluded = set()
    for entry in exclusions:
        if entry["field"] in facts:
            excluded.update(facts[entry["field"]].paths)
    examined = {hashlib.sha256(path.encode("utf-8")).hexdigest() for path in examined}
    excluded = {hashlib.sha256(path.encode("utf-8")).hexdigest() for path in excluded}
    unsupported = {
        path for path, namespace in units.items() if namespace != etree.QName(root).namespace
    }
    buckets = {
        "examined": examined & units.keys(),
        "explicitly_excluded": (excluded & units.keys()) - examined,
        "unsupported": unsupported - examined - excluded,
        "unexamined": units.keys() - examined - excluded - unsupported,
    }
    return {
        "unit": "leaf-or-empty-element-and-attribute-occurrence",
        "total": len(units),
        "categories": {
            name: {
                "count": len(paths),
                "path_sha256": sorted(paths),
            }
            for name, paths in buckets.items()
        },
        "unresolved_exclusions": sorted(e["field"] for e in exclusions if e["field"] not in facts),
        "note": "Unknown paths are hashed to avoid echoing payload-bearing extension names. "
        "Hashes are metadata, not anonymization. Containers, comments, whitespace and "
        "namespace declarations are not coverage units. Examined does not mean equal.",
    }
