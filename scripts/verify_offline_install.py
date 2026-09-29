"""Verify a separately installed wheel outside the checkout with Python sockets denied."""

import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path

PROBE = r"""
import json, socket
from pathlib import Path

def denied(*args, **kwargs):
    raise AssertionError("Network access attempted during offline verification")
socket.socket = denied
socket.create_connection = denied
socket.getaddrinfo = denied
import aksum_messagebench
from aksum_messagebench.corpus import verify
from aksum_messagebench.engine import compare
from lxml import etree
package = Path(aksum_messagebench.__file__).resolve().parent
data = package / "data"
manifest = data / "corpus/index.json"
# The installed wheel, not PYTHONPATH or editable source, supplies all assets.
assert data.is_dir() and "site-packages" in str(package)
result = verify(manifest)
assert result["exit_code"] == 0
assert len(result["cases"]) == 100
contract = data / "contracts/pacs008-preserve.json"
negative = compare(data / "corpus/negative/reference-truncated.source.xml",
                   data / "corpus/negative/reference-truncated.target.xml", contract)
positive = compare(data / "corpus/positive/identity.source.xml",
                   data / "corpus/positive/identity.target.xml", contract)
assert negative["exit_code"] == 1 and positive["exit_code"] == 0
assert all(c["status"] == "PASS" for c in negative["schema_checks"].values())
assert any(c["id"] == "PRESERVE-END-TO-END-ID" and c["status"] == "FAIL"
           for c in negative["assertions"])
print(json.dumps({"status": "PASS", "version": aksum_messagebench.__version__,
 "installed_package": str(package), "corpus_cases": len(result["cases"]),
 "schema_valid_semantic_loss_detected": True, "identity_passed": True,
 "python_socket_calls_denied": True, "independent_reproduction": False,
 "lxml": etree.LXML_VERSION, "libxml2": etree.LIBXML_VERSION}, indent=2))
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--python", type=Path, required=True)
    args = parser.parse_args()
    env = {k: v for k, v in os.environ.items() if k not in {"PYTHONPATH", "PYTHONHOME"}}
    with tempfile.TemporaryDirectory(prefix="messagebench-installed-check-") as directory:
        run = subprocess.run(
            [str(args.python.absolute()), "-I", "-c", PROBE],
            cwd=directory,
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
    if run.returncode:
        print(run.stderr)
        raise SystemExit(run.returncode)
    result = json.loads(run.stdout)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
