# OpenSSF readiness

No Best Practices badge has been obtained and no Scorecard result is claimed.

Prepared locally: Apache-2.0 original source license; explicit third-party rights; contribution,
governance and security policies; install/build/release instructions; deterministic tests and
reports; property and bounded fuzz tests; SAST; pinned dependency inventory and advisory scan;
native dependency SBOM; threat model; read-only SHA-pinned Actions; dependency update workflow;
secret scanning without network verification; source and unsigned artifact checksums.

Pending organization-owned evidence: public version history and stable release links, real
maintainer/contact ownership, private vulnerability reporting and response operation, required
human reviews, branch protection, protected release environment, successful hosted CI, actual
Scorecard execution and badge application. Files alone do not configure GitHub settings.

The scheduled Scorecard workflow runs without publication and preserves its output artifact.
No score is predicted. Passing criteria must be checked against the current badge application
when the repository is public. Silver/Gold need stronger independent review, governance and
sustained process evidence; this sprint does not establish them.

Review the secret baseline when public hashes change; never suppress a credential merely to
make a check pass. Review native dependencies separately from Python package advisories.
Signing/provenance identity must be provided by an actual approved release environment;
local checksums and source-commit metadata are not signatures.
