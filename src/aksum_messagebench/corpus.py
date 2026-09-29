"""Verify immutable fixture bytes and pre-recorded expectations, not reviewer identity."""

import hashlib
from pathlib import Path

from jsonschema import Draft202012Validator

from . import SCOPE_NOTICE
from .assets import data_root
from .engine import compare
from .errors import BenchError, aggregate_exit
from .input_guard import load_json, read_local
from .reports import canonical_json


def verify(manifest: Path, contract: Path | None = None) -> dict:
    document, raw = load_json(manifest)
    schema, _ = load_json(data_root() / "schemas/corpus.schema.json")
    if next(Draft202012Validator(schema).iter_errors(document), None) is not None:
        raise BenchError("CORPUS_MANIFEST_INVALID", 2)
    ids = [c["id"] for c in document["cases"]]
    if len(set(ids)) != len(ids):
        raise BenchError("CORPUS_DUPLICATE_ID", 2)
    if any(case["control"] not in ids for case in document["cases"]):
        raise BenchError("CORPUS_CONTROL_MISSING", 2)
    results = []
    codes = []
    for case in document["cases"]:
        for side in ("source", "target"):
            raw_input = read_local(case[side], root=manifest.parent)
            if hashlib.sha256(raw_input).hexdigest() != case[side + "_sha256"]:
                raise BenchError("CORPUS_HASH_MISMATCH", 2)
        report = compare(
            manifest.parent / case["source"],
            manifest.parent / case["target"],
            contract or data_root() / "contracts" / case.get("contract", "pacs008-preserve.json"),
        )
        actual = {
            "overall": report["overall"],
            "exit_code": report["exit_code"],
            "failed_assertions": sorted(
                a["id"] for a in report["assertions"] if a["status"] == "FAIL"
            ),
            "source_xsd": report["schema_checks"]["source"]["status"],
            "target_xsd": report["schema_checks"]["target"]["status"],
        }
        matched = actual == case["expected"]
        codes.append(0 if matched else 1)
        results.append(
            {
                "id": case["id"],
                "expectation_matched": matched,
                "actual": actual,
                "report_sha256": hashlib.sha256(canonical_json(report)).hexdigest(),
            }
        )
    return {
        "schema_version": "1.0",
        "kind": "corpus-verification",
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "cases": results,
        "exit_code": aggregate_exit(codes),
        "overall": "PASS" if all(c == 0 for c in codes) else "FAIL",
        "review_status": document["review_status"],
        "independent_review_verified": False,
        "limitations": [
            SCOPE_NOTICE,
            "Corpus PASS means recorded classifications match, including expected failures.",
            "Verification of recorded expectations is not independent review.",
        ],
    }
