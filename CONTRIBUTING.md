# Contributing

Do not add message families or enlarge the release corpus until Gate 1 independent review
is recorded. Start with docs/fixture-review.md and docs/prior-art.md. Preserve the narrow
non-operational scope and contribute generally useful library fixes upstream.

Install dependency-lock.txt in a Python 3.12+ venv; run the commands in docs/reproduce.md.
New comparisons need explicit semantics, positive and failing mutations, privacy tests and
scope accounting. Record expected results before adjusting implementation; explain changes
to any existing golden or expectation. No “update snapshots until green” workflow.

Only original synthetic fixtures or assets with documented public redistribution rights.
Apache-2.0 contributions; include provenance and applicable third-party terms. Never attach
live bank files. Pull requests need an independent human review and passing checks before
merge once a public repository exists. AI assistance must be disclosed; AI review does not
satisfy the independent human fixture-review gate.
