"""Scan tracked repository files without credential verification or network calls."""

import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
repository = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], cwd=root, capture_output=True, text=True, check=False
)
if repository.returncode or Path(repository.stdout.strip()).resolve() != root:
    raise SystemExit("Secret scan requires this project as a Git repository with tracked files.")
baseline = json.loads((root / ".secrets.baseline").read_text())
allowed = {
    (name, item["type"], item["hashed_secret"])
    for name, entries in baseline["results"].items()
    for item in entries
    if item.get("is_secret") is False
}
run = subprocess.run(
    [
        sys.executable,
        "-m",
        "detect_secrets",
        "scan",
        "--no-verify",
        "--exclude-files",
        r"^\.secrets\.baseline$",
    ],
    cwd=root,
    capture_output=True,
    check=True,
    text=True,
    timeout=120,
)
result = json.loads(run.stdout)
new = [
    (name, item["line_number"], item["type"])
    for name, entries in result["results"].items()
    for item in entries
    if (name, item["type"], item["hashed_secret"]) not in allowed
]
if new:
    # Never print detected values or source lines.
    print(json.dumps({"unreviewed_findings": new}))
    raise SystemExit(1)
print(
    "No unreviewed secret findings; network verification disabled. Reviewed public hashes retained."
)
