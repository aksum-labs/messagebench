# Development continuation, 29 September 2026

The owner authorized expansion before independent review (see expansion-decision.md).
Current working version is 0.1.0a2; no new public release has been made.

Implemented since the original proof:

- File-handoff suite, stored comparison report conversion and regression commands.
- Closed comparison report schema, status consistency and disjoint coverage validation.
- Exact unique declared-key transaction association; reordering passes, ambiguity blocks pass.
- 20 extractable pacs.008 fields and an explicit extended contract. Scheme, issuer, agent,
  instructed amount and settlement amount remain separate concepts.
- 40 additional original synthetic cases, with expectations authored before execution.
  All 46 cases across both manifests classify as expected. Independent review remains pending.
- 104 passing tests; 78/82 comparator/extractor/association branches covered (95.12%).
- 1,000 deterministic parser mutations completed without unexpected exceptions.
- Initial SHA-pinned, read-only PR checks, dependency updates and issue templates prepared.
  Hosted CI has not run. Secret/license scanning and complete release/Scorecard workflows
  are still outstanding; this is not a completed CI/security gate.

The native dependency review is open. The installed lxml wheel reports libxml2 2.14.6
and libxslt 1.1.43. Version strings alone do not account for vendor backports. A local
build against newer native libraries is being investigated; it has not replaced the
installed wheel. See evidence/native-advisory-review.json. No clean-native-audit claim.

Outstanding work includes pacs.002/camt.053, additional security/corpus classes,
full mutation and release evidence, native dependency resolution, final documentation,
rights inventory refresh, all report formats for suites, complete CI configuration,
and fresh packaged/offline/reproducible-build checks. The original review bundle is
historical 0.1.0a1 evidence, not a package of the current working tree.

Reproduce current checks:

```sh
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify corpus/index.json
PYTHONPATH=src .venv/bin/python -m aksum_messagebench corpus verify \
  corpus/extended/index.json --contract contracts/pacs008-extended.json
PYTHONPATH=src .venv/bin/coverage run -m pytest -q
.venv/bin/coverage json -o evidence/coverage.json
.venv/bin/python scripts/check_coverage.py evidence/coverage.json
PYTHONPATH=src .venv/bin/python fuzz/smoke.py --iterations 1000
.venv/bin/ruff check src tests scripts fuzz
.venv/bin/mypy src
```

Release assessment remains **NOT READY — FIX REQUIRED** while these tasks are in progress.
