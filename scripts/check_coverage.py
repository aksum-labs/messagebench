# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Enforce measured branch coverage of authored extraction and comparison code."""

import json
import sys
from pathlib import Path

report = json.loads(Path(sys.argv[1]).read_text())
selected = [
    data["summary"]
    for name, data in report["files"].items()
    if "/extractors/" in name
    or name.endswith(("/comparators.py", "/association.py", "/time_semantics.py"))
]
branches = sum(item["num_branches"] for item in selected)
covered = sum(item["covered_branches"] for item in selected)
if not branches or covered / branches < 0.90:
    raise SystemExit("Comparator/extractor branch coverage below 90% or evidence absent")
print(f"Comparator/extractor branches: {covered}/{branches} ({covered / branches:.2%})")
