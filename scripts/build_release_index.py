# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Combine already-authored cases without deriving or changing expected results."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "corpus"
cases = []
for prefix, manifest, contract in [
    ("gate1", "gate1-index.json", "pacs008-preserve.json"),
    ("extended", "extended/index.json", "pacs008-extended.json"),
    ("pacs002", "pacs002/index.json", "pacs002-preserve.json"),
    ("semantic", "semantic/index.json", None),
]:
    path = ROOT / manifest
    for original in json.loads(path.read_text())["cases"]:
        case = {
            **original,
            "id": prefix + "-" + original["id"],
            "control": prefix + "-" + original["control"],
            "contract": original.get("contract", contract),
        }
        for side in ("source", "target"):
            case[side] = (path.parent.relative_to(ROOT) / original[side]).as_posix()
        cases.append(case)
result = {
    "schema_version": "1.0",
    "version": "0.2.0-rc.1",
    "review_status": "pending-independent-human-review",
    "cases": cases,
}
(ROOT / "index.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"Combined {len(cases)} unchanged case expectations")
