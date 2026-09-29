"""Build twice from clean copies; attest only measured byte equivalence, not identity."""

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".hypothesis",
    ".mypy_cache",
    ".ruff_cache",
    ".coverage",
    "dist",
    "build",
    "htmlcov",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--require-clean", action="store_true")
    args = parser.parse_args()
    if args.output.resolve().is_relative_to(ROOT):
        raise SystemExit("Build output must be outside the source checkout")
    commit_run = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False
    )
    status_run = subprocess.run(
        ["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, check=False
    )
    source_commit = commit_run.stdout.strip() if commit_run.returncode == 0 else None
    source_dirty = bool(status_run.stdout) if status_run.returncode == 0 else None
    if args.require_clean and (not source_commit or source_dirty is not False):
        raise SystemExit("A clean committed source checkout is required")
    args.output.mkdir(parents=True, exist_ok=False)
    environment = {**os.environ, "SOURCE_DATE_EPOCH": "1790640000", "PYTHONHASHSEED": "0"}
    runs = []
    with tempfile.TemporaryDirectory(prefix="messagebench-build-") as folder:
        for run in (1, 2):
            target = Path(folder) / str(run)
            shutil.copytree(ROOT, target, ignore=lambda path, names: set(names) & EXCLUDE)
            subprocess.run(
                [sys.executable, "-m", "build", "--no-isolation"],
                cwd=target,
                env=environment,
                check=True,
                timeout=120,
                capture_output=True,
            )
            artifacts = sorted((target / "dist").iterdir())
            hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in artifacts}
            runs.append(hashes)
            if run == 1:
                for artifact in artifacts:
                    shutil.copy2(artifact, args.output / artifact.name)
    result = {
        "source_commit": source_commit,
        "source_dirty": source_dirty,
        "unsigned_artifacts_identical": runs[0] == runs[1],
        "runs": runs,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "source_date_epoch": environment["SOURCE_DATE_EPOCH"],
        "method": "Two separate source copies, same locked build environment, no isolation "
        "downloads; wheel and sdist hashes compared. Not independent reproduction.",
    }
    (args.output / "build-evidence.json").write_text(json.dumps(result, indent=2) + "\n")
    (args.output / "SHA256SUMS").write_text(
        "".join(h + "  " + name + "\n" for name, h in runs[0].items())
    )
    if not result["unsigned_artifacts_identical"]:
        raise SystemExit("Unsigned artifacts differ; do not claim reproducibility.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
