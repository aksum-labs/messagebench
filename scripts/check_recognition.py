"""Validate recognition accounting and citation metadata without network or external claims."""

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATES = {
    "ACHIEVED",
    "SUBMITTED",
    "READY-FOR-OWNER-APPROVAL",
    "BLOCKED-BY-EXTERNAL-PARTY",
    "BLOCKED-BY-REQUIRED-HUMAN-HISTORY",
    "REJECTED-AS-PAID",
    "REJECTED-AS-NOT-APPLICABLE",
}
data = json.loads((ROOT / "external/recognition-matrix.json").read_text())
seen = set()
for target in data["targets"]:
    if target["target"] in seen or target["status"] not in STATES:
        raise SystemExit("Invalid recognition target or disposition")
    seen.add(target["target"])
    for name in target["artifact_required"]:
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise SystemExit("Missing/unsafe recognition artifact")
    if target["accepted"] and not target["public_listing_url"]:
        raise SystemExit("Accepted recognition needs actual listing evidence")
    if target["submitted"] and target["status"] not in {
        "SUBMITTED",
        "ACHIEVED",
        "BLOCKED-BY-EXTERNAL-PARTY",
    }:
        raise SystemExit("Submission state inconsistent")
    if target["badge_url"] and not target["accepted"]:
        raise SystemExit("No unearned badge")
for name in ["CITATION.cff", "paper/citation.cff"]:
    document = yaml.safe_load((ROOT / name).read_text())
    if document["cff-version"] != "1.2.0" or not document["title"] or not document["authors"]:
        raise SystemExit("Invalid citation metadata")
criteria = json.loads((ROOT / "evidence/openssf-current-criteria.json").read_text())
if (
    len(criteria["criteria"]) != criteria["criteria_count"]
    or len({item["criterion"] for item in criteria["criteria"]}) != criteria["criteria_count"]
):
    raise SystemExit("Criteria accounting mismatch")
accounting = json.loads((ROOT / "external/mandate-accounting.json").read_text())
requirements = accounting["requirements"]
if (
    len(requirements) != accounting["requirement_count"]
    or len({item["id"] for item in requirements}) != len(requirements)
    or {item["section"] for item in requirements} != set(range(21))
):
    raise SystemExit("Mandate accounting mismatch")
for item in requirements:
    if item["status"] not in STATES or not item["disposition"].strip():
        raise SystemExit("Mandate item lacks a precise disposition")
    for name in item["evidence"]:
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise SystemExit("Missing/unsafe mandate evidence")
print("Recognition targets, artifacts, citations, criteria and mandate accounting validated.")

current = json.loads((ROOT / "evidence/engineering-current-accounting.json").read_text())
original = json.loads((ROOT / "docs/mandate-items.json").read_text())["items"]
if len(current["items"]) != len(original) or {x["id"] for x in current["items"]} != {
    x["id"] for x in original
}:
    raise SystemExit("Current original-mandate accounting mismatch")
for item in current["items"]:
    if item["status"] not in {"PASS", "BLOCKED-BY-HUMAN", "IMPOSSIBLE-WITH-EVIDENCE"}:
        raise SystemExit("Invalid original-mandate current disposition")
    for name in item["evidence"]:
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT) or not path.exists():
            raise SystemExit("Missing/unsafe original-mandate evidence")
print("All original engineering requirements also accounted for in the current crosswalk.")
