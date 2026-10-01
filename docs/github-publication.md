# GitHub publication and release controls

Repository: https://github.com/aksum-labs/messagebench. Owner authorized public source publication on 1 October 2026. Actual configuration read-back and hosted workflow results are in evidence/github-settings.json and evidence/hosted-recognition.json. Historical 29 September local completion reports describe the pre-publication state; current recognition status is EXTERNAL_RECOGNITION_COMPLETION_REPORT.md.

Company commit metadata and the organization-owned publisher App protect public author/push attribution. No personal account token is used for code pushes, public workflow dispatch or releases. A private owner-controlled maintainer team is CODEOWNER. Platform audit records are not erased or claimed anonymous.

Candidate snapshots may be built and signed by snapshot.yml without claiming independent review. It verifies a checksum manifest against the exact repository/workflow/main ref and OIDC issuer. The protected release.yml workflow retains the genuine review check and explicit enablement variables. It does not automatically publish a release.

Before formal RC release: authenticate two independent technical/rights review decisions for the current packet; appoint actual accountable maintainers; confirm protected branch/tag/environment controls; enable RELEASE_PREPARATION_ENABLED and RELEASE_SIGNING_ENABLED only after review; run and verify the protected workflow; inspect artifacts/notes; create a draft prerelease, attach all assets and publish only with genuine approval. Do not call the candidate v0.5/v1.0.

SHA-pinned Actions, read-only defaults, isolated OIDC jobs, CodeQL/Bandit, dependency review, secret scanning and SBOM/provenance are configured with least privilege. Public Scorecard badge appears only after the official published result exists. Prepared Best Practices/foundation forms are not earned awards or affiliations.
