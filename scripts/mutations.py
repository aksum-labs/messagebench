"""Targeted bypass, false-positive and association mutations; not whole-program scoring."""

import json
from pathlib import Path
from unittest.mock import patch

from aksum_messagebench import association, engine
from aksum_messagebench.comparators import compare_fact

ROOT = Path(__file__).resolve().parents[1]
mutants = []
for corpus, contract in [
    ("corpus/gate1-index.json", "contracts/pacs008-preserve.json"),
    ("corpus/extended/index.json", "contracts/pacs008-extended.json"),
    ("corpus/pacs002/index.json", "contracts/pacs002-preserve.json"),
]:
    manifest = ROOT / corpus
    cases = json.loads(manifest.read_text())["cases"]
    seen = set()
    for case in cases:
        for assertion_id in case["expected"]["failed_assertions"]:
            if assertion_id in seen:
                continue
            seen.add(assertion_id)

            def bypass(before, after, assertion, selected=assertion_id):
                return (
                    ("PASS", "MUTANT_BYPASS")
                    if assertion["id"] == selected
                    else compare_fact(before, after, assertion)
                )

            with (
                patch.object(engine, "compare_fact", bypass),
                patch.object(association, "compare_fact", bypass),
            ):
                report = engine.compare(
                    manifest.parent / case["source"],
                    manifest.parent / case["target"],
                    ROOT / contract,
                )
            mutants.append(
                {
                    "operator": "bypass-required-assertion",
                    "contract": contract,
                    "assertion": assertion_id,
                    "case": case["id"],
                    "killed": report["exit_code"] != case["expected"]["exit_code"],
                }
            )
    regen = next(
        (c for c in cases if c["id"] in {"message-id-regenerated", "regenerated-message-id"}), None
    )
    if regen:

        def deny_regeneration(before, after, assertion):
            if assertion["comparator"] == "allowed-regeneration":
                assertion = {**assertion, "comparator": "exact-identifier"}
            return compare_fact(before, after, assertion)

        with patch.object(engine, "compare_fact", deny_regeneration):
            report = engine.compare(
                manifest.parent / regen["source"],
                manifest.parent / regen["target"],
                ROOT / contract,
            )
        mutants.append(
            {
                "operator": "deny-permitted-regeneration",
                "contract": contract,
                "assertion": "PERMIT-MESSAGE-ID-REGENERATION",
                "case": regen["id"],
                "killed": report["exit_code"] != regen["expected"]["exit_code"],
            }
        )

cases = json.loads((ROOT / "corpus/extended/index.json").read_text())["cases"]
for case_id in ("batch-reordered", "batch-duplicate-key", "transaction-id-changed"):
    case = next(c for c in cases if c["id"] == case_id)

    def positional(root, keys, extractor):
        return {
            (str(i),): node for i, node in enumerate(association.transactions(root, extractor))
        }, None

    with patch.object(association, "index_transactions", positional):
        report = engine.compare(
            ROOT / "corpus/extended" / case["source"],
            ROOT / "corpus/extended" / case["target"],
            ROOT / "contracts/pacs008-extended.json",
        )
    mutants.append(
        {
            "operator": "guess-positional-association",
            "contract": "contracts/pacs008-extended.json",
            "assertion": "ASSOCIATION-PRECONDITION",
            "case": case_id,
            "killed": report["exit_code"] != case["expected"]["exit_code"],
        }
    )
print(
    json.dumps(
        {
            "mutants": mutants,
            "killed": sum(m["killed"] for m in mutants),
            "total": len(mutants),
            "scope": "Targeted preservation-bypass, false-positive and association operators only; "
            "not a whole-program mutation score. "
            "Original expected classifications remain unchanged.",
        },
        indent=2,
    )
)
