# Verify local review artifacts

Artifacts are **unsigned local review builds**, not approved releases. Verify SHA256SUMS and
inspect build-evidence.json/provenance.json in the artifact directory. A checksum only conveys
integrity relative to trusted evidence; it does not authenticate Aksum Labs or a build identity.
No Sigstore login, identity, signature, transparency publication or GitHub release was fabricated.

Two builds must be made from separate clean source copies with the same locked toolchain and
SOURCE_DATE_EPOCH; compare wheel and sdist bytes. Reproducibility claims are restricted to
those unsigned artifacts and that environment, not different OS/Python/native dependencies.
The reproduction script is scripts/reproducible_build.py. It produces review artifacts outside
the checkout, never overwrites a prior output directory, and records the source commit if present.

Runtime wheel installation is tested separately with `--no-index` against the local wheelhouse.
Run `messagebench corpus verify` from a directory outside the source checkout to prove resources
are packaged. An offline bundle is platform-specific and contains native dependency wheels.

Bandit B405 flags the standard-library ElementTree import in reports.py. Inspection shows
only Element/SubElement/tostring use to construct escaped JUnit output; no untrusted XML is
parsed there. The actual parser is the guarded lxml module. The low-severity finding is kept
in the raw scan rather than silently hidden. Python dependency advisory scan found no known
advisories; native dependency advisory analysis is still pending.

Any public release still needs all acceptance gates and actual human approval. Publication,
GitHub settings and identity-backed signing require real organizational setup after review.
