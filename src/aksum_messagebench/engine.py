"""Orchestrate two independent file inputs; never invoke an adapter."""

import hashlib
from pathlib import Path

from . import SCOPE_NOTICE, __version__
from .comparators import compare_fact
from .contracts import load_contract
from .coverage import account_coverage
from .errors import BenchError, aggregate_exit
from .extractors import pacs008_001_08 as extractor
from .input_guard import read_local
from .schema_catalog import NAMESPACE, SCHEMA_HASH, Catalog
from .xml_reader import parse_xml


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
        if root.tag != "{" + NAMESPACE + "}Document":
            raise BenchError("ROOT_QNAME_UNSUPPORTED", 3)
        check["namespace"] = NAMESPACE
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
    report = {
        "schema_version": "1.0",
        "tool_version": __version__,
        "contract_id": document["id"],
        "contract_version": document["version"],
        "contract_sha256": contract.sha256,
        "catalog_sha256": catalog.sha256,
        "schema_sha256": SCHEMA_HASH,
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
            "Single-transaction pacs.008.001.08 subset. "
            "No business-rule compliance or certification. Independent review pending.",
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
            facts[side] = extractor.extract(root)
    inputs_valid = all(root is not None for root in roots.values())
    namespace_allowed = (
        NAMESPACE in document["source_namespaces"] and NAMESPACE in document["target_namespaces"]
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
