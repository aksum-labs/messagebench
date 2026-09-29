"""Run the offline technical acceptance checks, failing on any observed failed check."""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--actionlint", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    python = sys.executable
    bindir = Path(python).parent
    checks = [
        ("lint", [str(bindir / "ruff"), "check", "src", "tests", "scripts", "fuzz"]),
        ("format", [str(bindir / "ruff"), "format", "--check", "src", "tests", "scripts", "fuzz"]),
        ("types", [str(bindir / "mypy"), "src"]),
        ("tests", [python, "-m", "coverage", "run", "-m", "pytest", "-q"]),
        (
            "coverage-json",
            [python, "-m", "coverage", "json", "-o", str(args.out / "coverage.json")],
        ),
        ("coverage-target", [python, "scripts/check_coverage.py", str(args.out / "coverage.json")]),
        ("corpus", [python, "-m", "aksum_messagebench", "corpus", "verify"]),
        ("differential-xsd", [python, "scripts/differential_xsd.py"]),
        ("security-corpus", [python, "scripts/security_corpus.py"]),
        ("mutations", [python, "scripts/mutations.py"]),
        ("parser-fuzz", [python, "fuzz/smoke.py", "--iterations", "1000"]),
        ("contract-fuzz", [python, "fuzz/contracts.py", "--iterations", "1000"]),
        ("licenses", [python, "scripts/check_licenses.py"]),
        ("secrets", [python, "scripts/check_secrets.py"]),
        ("sast", [str(bindir / "bandit"), "-r", "src", "-ll"]),
        (
            "workflows",
            [
                str(args.actionlint.resolve()),
                *map(str, sorted((ROOT / ".github/workflows").glob("*.yml"))),
            ],
        ),
    ]
    results = []
    env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
    for name, command in checks:
        run = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, timeout=180, check=False
        )
        (args.out / (name + ".stdout")).write_bytes(run.stdout)
        (args.out / (name + ".stderr")).write_bytes(run.stderr)
        results.append({"check": name, "exit_code": run.returncode, "passed": run.returncode == 0})
        print(name + (": PASS" if run.returncode == 0 else ": FAIL"), flush=True)
    summary = {
        "checks": results,
        "all_passed": all(c["passed"] for c in results),
        "scope": "Local offline checks; hosted Actions and genuine human approval are separate.",
    }
    (args.out / "checks.json").write_text(json.dumps(summary, indent=2) + "\n")
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
