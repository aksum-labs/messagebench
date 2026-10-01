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
print("Recognition targets, artifacts, citation metadata and criteria accounting validated.")
