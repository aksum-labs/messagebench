# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Coverage-guided synthetic parser/contract/comparator/engine boundary target.

Developer-only Atheris target. No production inputs, adapters, downloads or network.
Native ASan instrumentation is not claimed by this Python target.
"""

import atexit
import json
import os
import sys
import tempfile
from pathlib import Path

import atheris

with atheris.instrument_imports():
    from aksum_messagebench.assets import data_root
    from aksum_messagebench.comparators import compare_fact
    from aksum_messagebench.contracts import load_contract
    from aksum_messagebench.engine import compare
    from aksum_messagebench.errors import BenchError
    from aksum_messagebench.extractors.pacs008_001_08 import Fact
    from aksum_messagebench.xml_reader import parse_xml

ROOT = data_root()
TEMP = tempfile.TemporaryDirectory(prefix="messagebench-guided-synthetic-")
WORK = Path(TEMP.name)
SOURCE = ROOT / "corpus/positive/identity.source.xml"
BASE = SOURCE.read_bytes()
BASE_CONTRACT = json.loads((ROOT / "contracts/pacs008-preserve.json").read_text())
COUNTS = {"parser": 0, "contracts": 0, "comparators": 0, "engine": 0}


@atheris.instrument_func
def test_one_input(data):
    if not data or len(data) > 16384:
        return
    mode, raw = data[0] % 4, data[1:]
    key = ("parser", "contracts", "comparators", "engine")[mode]
    COUNTS[key] += 1
    if COUNTS[key] == 1 or sum(COUNTS.values()) % 100 == 0:
        save_counts()
    if mode == 0:
        try:
            parse_xml(raw)
        except BenchError:
            pass
    elif mode == 1:
        path = WORK / "contract.json"
        path.write_bytes(raw)
        try:
            load_contract(path)
        except BenchError:
            pass
    elif mode == 2:
        text = raw.decode("utf-8", errors="replace")
        # Real typed list comparator; reordering, multiplicity and Unicode are all exercised.
        left = Fact("list", tuple(text.split("|")), ())
        right = Fact("list", tuple(reversed(text.split("|"))), ())
        compare_fact(left, right, {"comparator": "multiset", "missing": "compare-presence"})
        compare_fact(left, right, {"comparator": "ordered-list", "missing": "compare-presence"})
    else:
        # Structured text mutations reach schema validation, extraction and preservation.
        target = WORK / "target.xml"
        replacement = raw.decode("utf-8", errors="replace")[:70]
        replacement = replacement.replace("&", "&amp;").replace("<", "&lt;")
        target.write_bytes(BASE.replace(b"INV-2026-000123", replacement.encode("utf-8")))
        compare(SOURCE, target, ROOT / "contracts/pacs008-preserve.json")


def save_counts():
    destination = os.environ.get("MESSAGEBENCH_FUZZ_COUNTS")
    if destination:
        Path(destination).write_text(
            json.dumps(
                {
                    "boundary_invocations": COUNTS,
                    "scope": "Python guidance; synthetic-only; no native ASan claim",
                },
                indent=2,
            )
            + "\n"
        )


atexit.register(save_counts)
if __name__ == "__main__":
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()
