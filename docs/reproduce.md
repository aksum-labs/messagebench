# Reproduce major claims

Use the locked Python 3.12 environment in docs/quickstart.md. Commands assume repository root.
Evidence files contain only original synthetic inputs/metadata. Do not substitute real bank
records when reproducing public test evidence.

```sh
# Formatting, type checking, unit/security/integration/property/fuzz-smoke/golden tests:
.venv/bin/ruff check src tests scripts
.venv/bin/ruff format --check src tests scripts
.venv/bin/mypy src
PYTHONPATH=src .venv/bin/python -m coverage run -m pytest -q
.venv/bin/python -m coverage report
.venv/bin/python -m coverage json -o evidence/coverage.json

# Exact recorded fixture classifications and baseline (offline):
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify
PYTHONPATH=src .venv/bin/python scripts/baseline.py

# Targeted mutation campaign and real 1,000-pair benchmark:
PYTHONPATH=src .venv/bin/python scripts/mutations.py
PYTHONPATH=src .venv/bin/python scripts/benchmark.py

# Dependencies/rights/native SBOM:
PYTHONPATH=src .venv/bin/python scripts/inventory.py
.venv/bin/bandit -r src -f json
# Explicit developer online scan, never invoked by runtime:
.venv/bin/pip-audit -r dependency-lock.txt -f json

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
human review; there is no automatic expected-result updater. The mutation script tests five
explicit oracle changes, not every possible line mutation. Hypothesis tests perform bounded
random XML/contract smoke checks, not a long-running fuzz service. Test counts refer to pytest
items, not individual Hypothesis examples.
