"""Deterministic grammar mutations of a valid closed contract; offline developer check."""

import argparse
import copy
import json
import random
import tempfile
from pathlib import Path

from aksum_messagebench.assets import data_root
from aksum_messagebench.contracts import load_contract
from aksum_messagebench.errors import BenchError

parser = argparse.ArgumentParser()
parser.add_argument("--iterations", type=int, default=1000)
args = parser.parse_args()
if not 1 <= args.iterations <= 100000:
    raise SystemExit("iterations must be 1..100000")
seed = json.loads((data_root() / "contracts/pacs008-preserve.json").read_text())
rng = random.Random(20260929)
values = [None, [], {}, True, 0, "", "python:exec", {"xpath": "//node"}, ["none"]]
rejected = 0
with tempfile.TemporaryDirectory(prefix="messagebench-contract-fuzz-") as folder:
    path = Path(folder) / "contract.json"
    for _ in range(args.iterations):
        doc = copy.deepcopy(seed)
        # All operators deliberately violate the closed schema or semantic constraints.
        operator = rng.randrange(5)
        if operator == 0:
            doc["execute"] = rng.choice(values)
        elif operator == 1:
            doc["assertions"][0]["comparator"] = rng.choice(values)
        elif operator == 2:
            doc["assertions"].append(copy.deepcopy(doc["assertions"][0]))
        elif operator == 3:
            doc["assertions"] = []
        else:
            doc["association"] = {"mode": "single", "keys": ["transactions.transaction_id"]}
        path.write_text(json.dumps(doc))
        try:
            load_contract(path)
        except BenchError as exc:
            assert exc.exit_code in (2, 4)
            rejected += 1
        else:
            raise AssertionError("Invalid contract accepted")
assert rejected == args.iterations
print(
    json.dumps(
        {
            "iterations": args.iterations,
            "seed": 20260929,
            "expected_rejections": rejected,
            "unexpected_acceptance": 0,
            "unexpected_exceptions": 0,
        }
    )
)
