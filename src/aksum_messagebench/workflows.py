"""File handoff and evidence comparison. No adapter code is ever executed."""

import hashlib
from pathlib import Path

from jsonschema import Draft202012Validator

from . import SCOPE_NOTICE
from .assets import data_root
from .engine import compare
from .errors import BenchError, aggregate_exit
from .input_guard import load_json, read_local
from .reports import canonical_json


def load_manifest(path: Path) -> tuple[dict, bytes]:
    document, raw = load_json(path)
    schema, _ = load_json(data_root() / "schemas/corpus.schema.json")
    if not Draft202012Validator(schema).is_valid(document):
        raise BenchError("CORPUS_MANIFEST_INVALID", 2)
    ids = [case["id"] for case in document["cases"]]
    if len(ids) != len(set(ids)):
        raise BenchError("CORPUS_DUPLICATE_ID", 2)
    if any(case["control"] not in ids for case in document["cases"]):
        raise BenchError("CORPUS_CONTROL_MISSING", 2)
    return document, raw


def suite(manifest: Path, outputs: Path, contract: Path | None = None) -> dict:
    """Compare each corpus source against outputs/<case-id>.xml, ignoring oracle targets."""
    document, raw = load_manifest(manifest)
    results = []
    codes = []
    for case in sorted(document["cases"], key=lambda item: item["id"]):
        try:
            source = read_local(case["source"], root=manifest.parent)
            if hashlib.sha256(source).hexdigest() != case["source_sha256"]:
                raise BenchError("CORPUS_HASH_MISMATCH", 2)
            result = compare(
                manifest.parent / case["source"],
                outputs / (case["id"] + ".xml"),
                contract
                or data_root() / "contracts" / case.get("contract", "pacs008-preserve.json"),
            )
            if result["source_sha256"] != case["source_sha256"]:
                raise BenchError("CORPUS_SOURCE_CHANGED", 3)
        except BenchError as exc:
            result = {"overall": "INDETERMINATE", "exit_code": exc.exit_code, "code": exc.code}
        codes.append(result["exit_code"])
        results.append({"id": case["id"], "result": result})
    code = aggregate_exit(codes)
    return {
        "schema_version": "1.0",
        "kind": "adapter-suite",
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "cases": results,
        "exit_code": code,
        "overall": "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE",
        "limitations": [SCOPE_NOTICE, "Adapter execution is outside MessageBench."],
    }


def load_result(path: Path) -> dict:
    result, _ = load_json(path, limit=5 * 1024 * 1024)
    return validate_result(result)


def validate_result(result: dict) -> dict:
    if result.get("kind") == "adapter-suite":
        return validate_suite(result)
    schema, _ = load_json(data_root() / "schemas/report.schema.json")
    if not Draft202012Validator(schema).is_valid(result):
        raise BenchError("REPORT_INVALID", 2)
    ids = [check["id"] for check in result["assertions"]]
    if len(ids) != len(set(ids)):
        raise BenchError("REPORT_DUPLICATE_ASSERTION", 2)
    for check in result["schema_checks"].values():
        if (check["status"] == "PASS") != (check["exit_code"] == 0):
            raise BenchError("REPORT_SCHEMA_STATUS_INCONSISTENT", 2)
        if check["exit_code"] == 0 and check["code"] != "XSD_VALID":
            raise BenchError("REPORT_SCHEMA_STATUS_INCONSISTENT", 2)
    codes = [check["exit_code"] for check in result["schema_checks"].values()]
    inputs_valid = all(check["status"] == "PASS" for check in result["schema_checks"].values())
    if inputs_valid:
        codes.extend(
            3
            if check["status"] in {"UNSUPPORTED", "INDETERMINATE"}
            else 1
            if check["status"] == "FAIL"
            else 0
            for check in result["assertions"]
            if check["required"]
        )
    code = aggregate_exit(codes)
    overall = "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE"
    if result["exit_code"] != code or result["overall"] != overall:
        raise BenchError("REPORT_STATUS_INCONSISTENT", 2)
    if not any(check["required"] for check in result["assertions"]):
        raise BenchError("REPORT_REQUIRED_ASSERTION_MISSING", 2)
    for coverage in result["coverage"].values():
        if "categories" in coverage:
            paths = []
            for category in coverage["categories"].values():
                if category["count"] != len(category["path_sha256"]):
                    raise BenchError("REPORT_COVERAGE_INCONSISTENT", 2)
                paths.extend(category["path_sha256"])
            if len(paths) != len(set(paths)) or len(paths) != coverage["total"]:
                raise BenchError("REPORT_COVERAGE_INCONSISTENT", 2)
    return result


def regression(previous: dict, current: dict) -> dict:
    """Compare equivalent assertion scopes; a changed contract never silently passes."""
    validate_result(previous)
    validate_result(current)
    if previous.get("kind") == "adapter-suite" and current.get("kind") == "adapter-suite":
        return regression_suite(previous, current)
    if "kind" in previous or "kind" in current:
        raise BenchError("REPORT_KINDS_DIFFER", 2)
    scope_keys = ("contract_sha256", "schema_sha256", "extractor_version", "source_sha256")
    same_scope = all(previous[key] == current[key] for key in scope_keys)
    before = {check["id"]: check for check in previous["assertions"]}
    after = {check["id"]: check for check in current["assertions"]}
    changes = []
    for key in sorted(before.keys() | after.keys()):
        left, right = before.get(key), after.get(key)
        left_status = left["status"] if left else "MISSING"
        right_status = right["status"] if right else "MISSING"
        if (
            left is None
            or right is None
            or any(
                left.get(k) != right.get(k)
                for k in ("field", "comparator", "item_comparator", "required", "normalization")
            )
        ):
            same_scope = False
        if left_status != right_status:
            changes.append({"id": key, "previous": left_status, "current": right_status})
    codes = [previous["exit_code"], current["exit_code"]]
    # This command certifies only current evidence; a resolved previous failure is not retained.
    code = aggregate_exit([current["exit_code"], 0 if same_scope else 3])
    if max(codes) == 5:
        code = 5
    return {
        "schema_version": "1.0",
        "kind": "regression",
        "same_scope": same_scope,
        "previous_sha256": hashlib.sha256(canonical_json(previous)).hexdigest(),
        "current_sha256": hashlib.sha256(canonical_json(current)).hexdigest(),
        "changes": changes,
        "exit_code": code,
        "overall": "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE",
        "limitations": [SCOPE_NOTICE, "Stored reports are untrusted claims, not signatures."],
    }


def validate_suite(result: dict) -> dict:
    schema, _ = load_json(data_root() / "schemas/suite-report.schema.json")
    if not Draft202012Validator(schema).is_valid(result):
        raise BenchError("REPORT_INVALID", 2)
    ids = [case["id"] for case in result["cases"]]
    if len(ids) != len(set(ids)):
        raise BenchError("REPORT_DUPLICATE_CASE", 2)
    for case in result["cases"]:
        if "assertions" in case["result"]:
            validate_result(case["result"])
    code = aggregate_exit([case["result"]["exit_code"] for case in result["cases"]])
    overall = "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE"
    if code != result["exit_code"] or overall != result["overall"]:
        raise BenchError("REPORT_STATUS_INCONSISTENT", 2)
    return result


def regression_suite(previous: dict, current: dict) -> dict:
    before = {case["id"]: case["result"] for case in previous["cases"]}
    after = {case["id"]: case["result"] for case in current["cases"]}
    same_scope = (
        previous["manifest_sha256"] == current["manifest_sha256"] and before.keys() == after.keys()
    )
    results = []
    codes = [current["exit_code"], 0 if same_scope else 3]
    for key in sorted(before.keys() & after.keys()):
        if "assertions" in before[key] and "assertions" in after[key]:
            delta = regression(before[key], after[key])
            same_scope = same_scope and delta["same_scope"]
            codes.append(delta["exit_code"])
            results.append({"id": key, "result": delta})
        else:
            codes.append(3)
            same_scope = False
    code = aggregate_exit(codes)
    return {
        "schema_version": "1.0",
        "kind": "suite-regression",
        "same_scope": same_scope,
        "cases": results,
        "exit_code": code,
        "overall": "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE",
        "limitations": [SCOPE_NOTICE, "Stored reports are untrusted claims, not signatures."],
    }
