"""Five targeted oracle mutations against pre-recorded, unchanged expectations."""

import json
from pathlib import Path
from unittest.mock import patch

from aksum_messagebench import engine
from aksum_messagebench.comparators import compare_fact

root = Path(__file__).resolve().parents[1]
cases = json.loads((root / "corpus/index.json").read_text())["cases"]
mutants = []
for case in cases:
    if not case["expected"]["failed_assertions"]:
        continue
    assertion_id = case["expected"]["failed_assertions"][0]

    def bypass(before, after, assertion, selected=assertion_id):
        return (
            ("PASS", "MUTANT_BYPASS")
            if assertion["id"] == selected
            else compare_fact(before, after, assertion)
        )

    with patch.object(engine, "compare_fact", bypass):
        report = engine.compare(
            root / "corpus" / case["source"],
            root / "corpus" / case["target"],
            root / "contracts/pacs008-preserve.json",
        )
    mutants.append(
        {
            "operator": "bypass-required-assertion",
            "assertion": assertion_id,
            "case": case["id"],
            "killed": report["overall"] != case["expected"]["overall"],
        }
    )
case = next(c for c in cases if c["id"] == "message-id-regenerated")


def deny_regeneration(before, after, assertion):
    if assertion["comparator"] == "allowed-regeneration":
        assertion = {**assertion, "comparator": "exact-identifier"}
    return compare_fact(before, after, assertion)


with patch.object(engine, "compare_fact", deny_regeneration):
    report = engine.compare(
        root / "corpus" / case["source"],
        root / "corpus" / case["target"],
        root / "contracts/pacs008-preserve.json",
    )
mutants.append(
    {
        "operator": "deny-permitted-regeneration",
        "assertion": "PERMIT-MESSAGE-ID-REGENERATION",
        "case": case["id"],
        "killed": report["overall"] != case["expected"]["overall"],
    }
)
print(
    json.dumps(
        {
            "mutants": mutants,
            "killed": sum(m["killed"] for m in mutants),
            "total": len(mutants),
            "scope": "Targeted oracle-bypass and false-positive operators only; not a "
            "whole-program mutation score. Expectations were not changed.",
        },
        indent=2,
    )
)
