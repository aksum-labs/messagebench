"""Run source-only Scorecard checks on a tracked-file snapshot, excluding local venvs."""

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    "License,Security-Policy,Dangerous-Workflow,Token-Permissions,"
    "Pinned-Dependencies,Binary-Artifacts,Dependency-Update-Tool"
)
parser = argparse.ArgumentParser()
parser.add_argument("--binary", type=Path, required=True)
args = parser.parse_args()
files = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
with tempfile.TemporaryDirectory(prefix="messagebench-scorecard-") as folder:
    snapshot = Path(folder)
    for name in filter(None, files):
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise SystemExit("Tracked source must be regular files")
        target = snapshot / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
    run = subprocess.run(
        [
            str(args.binary.resolve()),
            "--local=" + str(snapshot),
            "--checks=" + CHECKS,
            "--format=json",
            "--show-details",
        ],
        capture_output=True,
        text=True,
        timeout=120,
        check=True,
    )
    result = json.loads(run.stdout)
    result["repo"]["name"] = "local-tracked-source-snapshot"
    result["metadata"] = ["scope=seven-local-source-checks-only", "not-a-public-repository-score"]
    print(json.dumps(result, indent=2, sort_keys=True))
