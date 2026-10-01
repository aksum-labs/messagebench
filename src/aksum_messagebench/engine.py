# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Orchestrate two independent file inputs; never invoke an adapter."""

import hashlib
from pathlib import Path

from lxml import etree

from . import SCOPE_NOTICE, __version__
from .association import compare_keyed
from .comparators import compare_fact
from .contracts import load_contract
from .coverage import account_coverage
from .errors import BenchError, aggregate_exit
from .extractors import pacs002_001_10, pacs008_001_08
from .input_guard import read_local
from .schema_catalog import SCHEMA_HASHES, Catalog
from .xml_reader import parse_xml

EXTRACTORS = {pacs008_001_08.NAMESPACE: pacs008_001_08, pacs002_001_10.NAMESPACE: pacs002_001_10}


def inspect_bytes(data: bytes, catalog: Catalog) -> tuple[dict, object | None]:
    check = {
        "sha256": hashlib.sha256(data).hexdigest(),
        "status": "INDETERMINATE",
        "code": "NOT_EXAMINED",
        "exit_code": 3,
        "namespace": None,
    }
    try:
        root = parse_xml(data)
        namespace = etree.QName(root).namespace
        if namespace not in catalog.schemas or root.tag != "{" + namespace + "}Document":
            raise BenchError("ROOT_QNAME_UNSUPPORTED", 3)
        check["namespace"] = namespace
        if not catalog.validate(root):
            raise BenchError("XSD_INVALID", 1)
        check.update(status="PASS", code="XSD_VALID", exit_code=0)
        return check, root
    except BenchError as exc:
        check.update(
            status="FAIL" if exc.exit_code in {1, 4} else "UNSUPPORTED",
            code=exc.code,
            exit_code=exc.exit_code,
        )
        return check, None


def inspect_file(path: Path, catalog: Catalog) -> tuple[dict, object | None]:
    try:
        return inspect_bytes(read_local(path), catalog)
    except BenchError as exc:
        return {
            "sha256": None,
            "status": "INDETERMINATE",
            "code": exc.code,
            "exit_code": exc.exit_code,
            "namespace": None,
        }, None


def compare(
    source: Path, target: Path, contract_path: Path, catalog_path: Path | None = None
) -> dict:
    contract = load_contract(contract_path)
    catalog = Catalog(catalog_path)
    document = contract.document
    extractor = EXTRACTORS.get(document["source_namespaces"][0], pacs008_001_08)
    report = {
        "schema_version": "1.0",
        "tool_version": __version__,
        "contract_id": document["id"],
        "contract_version": document["version"],
        "contract_sha256": contract.sha256,
        "catalog_sha256": catalog.sha256,
        "schema_sha256": SCHEMA_HASHES.get(extractor.NAMESPACE),
        "extractor_version": extractor.VERSION,
        "source_sha256": None,
        "target_sha256": None,
        "schema_checks": {},
        "assertions": [],
        "coverage": {},
        "overall": "INDETERMINATE",
        "exit_code": 3,
        "limitations": [
            SCOPE_NOTICE,
            "Declared version-specific subset; single or uniquely keyed transaction association. "
            "No business-rule compliance or certification. Independent human review not performed.",
        ],
    }
    codes = []
    roots = {}
    facts = {}
    for side, path in (("source", source), ("target", target)):
        check, root = inspect_file(path, catalog)
        report["schema_checks"][side] = check
        report[side + "_sha256"] = check["sha256"]
        codes.append(check["exit_code"])
        roots[side] = root
        if root is not None:
            facts[side] = EXTRACTORS[check["namespace"]].extract(root)
    extractor = EXTRACTORS.get(report["schema_checks"]["source"]["namespace"], extractor)
    report["extractor_version"] = extractor.VERSION
    report["schema_sha256"] = SCHEMA_HASHES[extractor.NAMESPACE]
    inputs_valid = all(root is not None for root in roots.values())
    namespace_allowed = (
        report["schema_checks"]["source"]["namespace"] in document["source_namespaces"]
        and report["schema_checks"]["target"]["namespace"] in document["target_namespaces"]
        and report["schema_checks"]["source"]["namespace"] == extractor.NAMESPACE
        and report["schema_checks"]["target"]["namespace"] == extractor.NAMESPACE
    )
    association_valid = (
        inputs_valid
        and document["association"]["mode"] == "single"
        and all(extractor.transaction_count(r) == 1 for r in roots.values())
    )
    for assertion in document["assertions"]:
        field = assertion["field"]
        status, code = "INDETERMINATE", "INPUT_NOT_VALID"
        source_paths = (
            list(facts["source"][field].paths) if field in facts.get("source", {}) else []
        )
        target_paths = (
            list(facts["target"][field].paths) if field in facts.get("target", {}) else []
        )
        if inputs_valid:
            if not namespace_allowed:
                status, code = "UNSUPPORTED", "CONTRACT_NAMESPACE_UNSUPPORTED"
            elif field not in extractor.FIELDS:
                status, code = "UNSUPPORTED", "FIELD_UNSUPPORTED"
            elif assertion["cardinality"] != extractor.FIELDS[field][2]:
                status, code = "UNSUPPORTED", "CARDINALITY_UNSUPPORTED"
            elif (
                assertion["cardinality"] == "per-transaction"
                and document["association"]["mode"] == "keyed"
            ):
                status, code = compare_keyed(
                    roots["source"],
                    roots["target"],
                    assertion,
                    document["association"]["keys"],
                    extractor,
                )
            elif assertion["cardinality"] == "per-transaction" and not association_valid:
                status, code = "INDETERMINATE", "ASSOCIATION_AMBIGUOUS_OR_UNSUPPORTED"
            else:
                status, code = compare_fact(
                    facts["source"][field], facts["target"][field], assertion
                )
            if assertion["required"]:
                codes.append(
                    3
                    if status in {"UNSUPPORTED", "INDETERMINATE"}
                    else 1
                    if status == "FAIL"
                    else 0
                )
        report["assertions"].append(
            {
                "id": assertion["id"],
                "field": field,
                "comparator": assertion["comparator"],
                **(
                    {"item_comparator": assertion["item_comparator"]}
                    if "item_comparator" in assertion
                    else {}
                ),
                "required": assertion["required"],
                "status": status,
                "code": code,
                "normalization": assertion.get("normalization", "none"),
                "source_paths": source_paths,
                "target_paths": target_paths,
            }
        )
    for side in ("source", "target"):
        report["coverage"][side] = (
            account_coverage(roots[side], facts[side], report["assertions"], document["exclusions"])
            if roots[side] is not None
            else {"unavailable": True}
        )
    report["assertions"].sort(key=lambda item: item["id"])
    exit_code = aggregate_exit(codes)
    report["exit_code"] = exit_code
    report["overall"] = "PASS" if exit_code == 0 else "FAIL" if exit_code == 1 else "INDETERMINATE"
    return report
