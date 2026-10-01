# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Retain a dated Python-advisory result even when the advisory service/check fails.

Connected maintainer tooling only. Native-component source review is separate.
"""

import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    output = args.out / "python-advisories.json"
    command = [
        sys.executable,
        "-m",
        "pip_audit",
        "--strict",
        "--disable-pip",
        "--no-deps",
        "-r",
        str(ROOT / "dependency-lock.txt"),
        "--format",
        "json",
        "--output",
        str(output),
    ]
    try:
        run = subprocess.run(command, capture_output=True, text=True, timeout=300, check=False)
        code = run.returncode
        status = "PASS" if code == 0 else "CHECK_FAILED"
    except subprocess.TimeoutExpired:
        code, status = 1, "ADVISORY_SERVICE_TIMEOUT"
    summary = {
        "checked_at": datetime.datetime.now(datetime.UTC).isoformat(),
        "scope": "Pinned Python distributions only; does not audit bundled native XML sources",
        "status": status,
        "exit_code": code,
        "advisory_result_retained": output.is_file(),
        "notification": (
            "Normal repository Actions failure notifications; "
            "accountable maintainers must subscribe."
        ),
        "native_source_review": [
            "evidence/native-source-pins.json",
            "evidence/native-advisory-review.json",
        ],
    }
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
