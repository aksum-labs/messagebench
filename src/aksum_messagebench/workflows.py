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
    return document, raw


def suite(manifest: Path, outputs: Path, contract: Path) -> dict:
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
                manifest.parent / case["source"], outputs / (case["id"] + ".xml"), contract
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
    result, _ = load_json(path)
    schema, _ = load_json(data_root() / "schemas/report.schema.json")
    if not Draft202012Validator(schema).is_valid(result):
        raise BenchError("REPORT_INVALID", 2)
    ids = [check["id"] for check in result["assertions"]]
    if len(ids) != len(set(ids)):
        raise BenchError("REPORT_DUPLICATE_ASSERTION", 2)
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
                for k in ("field", "comparator", "required", "normalization")
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
