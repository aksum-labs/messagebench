import hashlib
import json

from aksum_messagebench.engine import compare
from aksum_messagebench.reports import canonical_json


def test_canonical_hashes(root, contract):
    hashes = json.loads((root / "tests/golden/report-hashes.json").read_text())
    manifest = json.loads((root / "corpus/gate1-index.json").read_text())
    for case in manifest["cases"]:
        report = compare(
            root / "corpus" / case["source"], root / "corpus" / case["target"], contract
        )
        assert hashlib.sha256(canonical_json(report)).hexdigest() == hashes[case["id"]]
