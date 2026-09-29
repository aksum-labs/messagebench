"""Explicit connected developer preparation of digest-pinned external check tools."""

import argparse
import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--out", type=Path, required=True)
parser.add_argument("names", nargs="+", choices=["scorecard", "actionlint", "cosign"])
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
for pin in json.loads((ROOT / "evidence/developer-tool-pins.json").read_text()):
    if pin["name"] not in args.names:
        continue
    path = args.out / Path(pin["url"]).name
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != pin["sha256"]:
        subprocess.run(
            [
                "curl",
                "--fail",
                "--location",
                "--retry",
                "2",
                "--connect-timeout",
                "10",
                "--max-time",
                "300",
                pin["url"],
                "--output",
                str(path),
            ],
            check=True,
            timeout=930,
        )
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin["sha256"]:
        raise SystemExit("Tool digest mismatch: " + pin["name"])
    if path.name.endswith(".tar.gz"):
        with tarfile.open(path) as archive:
            archive.extractall(args.out / pin["name"], filter="data")
    else:
        path.chmod(0o755)
    print(pin["name"] + " " + pin["version"] + " verified")
