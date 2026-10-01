# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""One targeted killing witness for every required declaration; no whole-program score."""

import json
from pathlib import Path
from unittest.mock import patch

from aksum_messagebench import association, engine
from aksum_messagebench.comparators import compare_fact

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "corpus/index.json").read_text())
mutants = []
rules = []


def outcome(report):
    return {
        "overall": report["overall"],
        "exit_code": report["exit_code"],
        "failed_assertions": sorted(a["id"] for a in report["assertions"] if a["status"] == "FAIL"),
        "source_xsd": report["schema_checks"]["source"]["status"],
        "target_xsd": report["schema_checks"]["target"]["status"],
    }


def run_case(case, contract):
    return engine.compare(
        ROOT / "corpus" / case["source"], ROOT / "corpus" / case["target"], contract
    )


def positional(root, keys, extractor):
    return {
        (str(i),): node for i, node in enumerate(association.transactions(root, extractor))
    }, None


for filename in sorted({c["contract"] for c in manifest["cases"]}):
    contract = ROOT / "contracts" / filename
    doc = json.loads(contract.read_text())
    cases = [c for c in manifest["cases"] if c["contract"] == filename]
    for assertion in doc["assertions"]:
        if not assertion["required"]:
            continue
        witness = next(
            (c for c in cases if assertion["id"] in c["expected"]["failed_assertions"]), None
        )
        if witness:

            def bypass(before, after, rule, selected=assertion["id"]):
                return (
                    ("PASS", "MUTANT_BYPASS")
                    if rule["id"] == selected
                    else compare_fact(before, after, rule)
                )

            with (
                patch.object(engine, "compare_fact", bypass),
                patch.object(association, "compare_fact", bypass),
            ):
                actual = outcome(run_case(witness, contract))
            operator = "bypass-required-assertion"
        elif assertion["comparator"] == "allowed-regeneration":
            witness = next(
                c for c in cases if "regenerat" in c["id"] and c["expected"]["exit_code"] == 0
            )

            def deny_regeneration(before, after, rule):
                if rule["comparator"] == "allowed-regeneration":
                    rule = {**rule, "comparator": "exact-identifier"}
                return compare_fact(before, after, rule)

            with patch.object(engine, "compare_fact", deny_regeneration):
                actual = outcome(run_case(witness, contract))
            operator = "deny-permitted-regeneration"
        elif assertion["field"] in doc["association"].get("keys", []):
            witness = next(c for c in cases if c["id"].endswith("transaction-id-changed"))
            with patch.object(association, "index_transactions", positional):
                actual = outcome(run_case(witness, contract))
            operator = "bypass-key-association-precondition"
        else:
            raise AssertionError(
                "Required declaration lacks a mutation witness: " + filename + "/" + assertion["id"]
            )
        killed = actual != witness["expected"]
        assert killed, (filename, assertion["id"])
        mutants.append(
            {
                "contract": filename,
                "assertion": assertion["id"],
                "operator": operator,
                "case": witness["id"],
                "killed": killed,
            }
        )
        rules.append(
            {
                "contract": filename,
                "assertion": assertion["id"],
                "field": assertion["field"],
                "targeted_witness": witness["id"],
                "operator": operator,
                "killed": killed,
            }
        )
for suffix in ("batch-reordered", "batch-duplicate-key"):
    case = next(c for c in manifest["cases"] if c["id"] == "extended-" + suffix)
    with patch.object(association, "index_transactions", positional):
        actual = outcome(run_case(case, ROOT / "contracts" / case["contract"]))
    killed = actual != case["expected"]
    assert killed
    mutants.append(
        {
            "contract": case["contract"],
            "assertion": "ASSOCIATION-PRECONDITION",
            "operator": "guess-positional-association",
            "case": case["id"],
            "killed": killed,
        }
    )
(ROOT / "evidence/rule-coverage.json").write_text(
    json.dumps(
        {"required_declarations": len(rules), "all_have_killing_witness": True, "rules": rules},
        indent=2,
    )
    + "\n"
)
print(
    json.dumps(
        {
            "mutants": mutants,
            "killed": sum(m["killed"] for m in mutants),
            "total": len(mutants),
            "scope": (
                "Targeted assertion, false-positive and association mutations; "
                "not whole-program scoring. Original expected classifications retained."
            ),
        },
        indent=2,
    )
)
