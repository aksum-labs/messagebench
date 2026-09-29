# Reproduce major claims

Use the locked Python 3.12 environment in docs/quickstart.md. Commands assume repository root.
Evidence files contain only original synthetic inputs/metadata. Do not substitute real bank
records when reproducing public test evidence.

```sh
# Formatting, type checking, unit/security/integration/property/fuzz-smoke/golden tests:
.venv/bin/ruff check src tests scripts fuzz
.venv/bin/ruff format --check src tests scripts fuzz
.venv/bin/mypy src
PYTHONPATH=src .venv/bin/python -m coverage run -m pytest -q
.venv/bin/python -m coverage report
.venv/bin/python -m coverage json -o evidence/coverage.json

# Exact recorded fixture classifications and baseline (offline):
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify
PYTHONPATH=src .venv/bin/python scripts/baseline.py
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify corpus/extended/index.json --contract contracts/pacs008-extended.json
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify corpus/pacs002/index.json --contract contracts/pacs002-preserve.json

# Targeted mutation campaign and real 1,000-pair benchmark:
PYTHONPATH=src .venv/bin/python scripts/mutations.py
PYTHONPATH=src .venv/bin/python scripts/benchmark.py

# Dependencies/rights/native SBOM:
PYTHONPATH=src .venv/bin/python scripts/inventory.py
.venv/bin/bandit -r src -f json
# Explicit developer online scan, never invoked by runtime:
.venv/bin/pip-audit --strict --disable-pip --no-deps -r dependency-lock.txt -f json

# Package build:
.venv/bin/python -m build --no-isolation
```

The optional Cognis comparison in `evidence/baseline.json` used only public synthetic XML
and the following reviewed source (not included in MessageBench):

```sh
# Explicit connected preparation; inspect the exact source before executing it.
curl -fL https://raw.githubusercontent.com/cognis-digital/iso20022/d7903979b5dbc74967f93eaa5688d5d5db984b06/iso20022/core.py -o /tmp/cognis-core.py
PYTHONPATH=src .venv/bin/python scripts/baseline.py --cognis-source /tmp/cognis-core.py
```

The script checks the source SHA-256 before import. No upstream runtime code is bundled.
The first baseline only parses/XSD-validates; neither XSD engine was expected to compare
messages. These results demonstrate differing scope, not bugs in the baseline tools.

Golden hashes pin canonical report bytes for all six pairs. Changes require explanation and
human review; there is no automatic expected-result updater. The mutation script tests 33
targeted oracle/association changes, not every possible line mutation. Hypothesis tests perform bounded
random XML/contract smoke checks, not a long-running fuzz service. Test counts refer to pytest
items, not individual Hypothesis examples.

Current supplemental checks:

```sh
PYTHONPATH=src .venv/bin/python fuzz/smoke.py --iterations 1000
.venv/bin/python scripts/check_licenses.py
.venv/bin/python scripts/check_secrets.py
.venv/bin/python scripts/check_coverage.py evidence/coverage.json
.venv/bin/pip-audit --strict --disable-pip --no-deps -r dependency-lock.txt -f json
```

Secret scanning requires a Git checkout with tracked files and never verifies credentials
against external services. Its baseline covers reviewed public digests, not credentials.
Python advisory scans cover the fully enumerated requirements; native review is separate.

Prepare artifacts in **new** directories outside the checkout:

```sh
.venv/bin/python scripts/reproducible_build.py ../messagebench-release-new --require-clean
.venv/bin/python scripts/prepare_bundle.py --release ../messagebench-release-new \
  --native /tmp/messagebench-native-wheels --archives /tmp/messagebench-native-archives \
  --out ../messagebench-review-new
```

The native directory must contain the wheel and native-build.json produced by the documented
build recipe. The bundle includes a hashed offline installation lock and corresponding native
sources. Its README gives the installation check. Source copies are clean build directories;
source_dirty in build evidence records whether the original checkout had uncommitted changes.
Do not present an uncommitted checkout as a clean source commit.
