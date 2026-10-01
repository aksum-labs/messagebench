# Public OpenSSF Scorecard — actual result

The official public action succeeded in [run 36831305491](https://github.com/aksum-labs/messagebench/actions/runs/36831305491), at commit `2bb62cb1e0dcbbb91d265bb824eda274cbd9b217`. Published score: **6.4/10**, 1 October 2026. The complete 18-check result is evidence/scorecard-public.json; negative one means unavailable/not scored, never a pass. The live badge can change after later scans.

| Check | Score |
|---|---:|
| Code-Review | 0 |
| Maintained | 0 |
| Dependency-Update-Tool | 10 |
| CI-Tests | -1 |
| Security-Policy | 10 |
| Binary-Artifacts | 10 |
| Packaging | -1 |
| Dangerous-Workflow | 10 |
| SAST | 10 |
| Token-Permissions | 10 |
| Pinned-Dependencies | 10 |
| License | 10 |
| CII-Best-Practices | 0 |
| Vulnerabilities | 10 |
| Signed-Releases | -1 |
| Branch-Protection | 0 |
| Fuzzing | 0 |
| Contributors | 0 |

CI-Tests detector availability does not negate actual successful hosted tests. Custom parser/contract campaigns exist and passed, but Scorecard's recognized fuzzing integrations do not detect them. Do not manufacture a recognized integration solely for a score.

The official action is pinned to v2.4.4 immutable commit, publish_results is true, OIDC is job-scoped and SARIF was uploaded. No unsafe top-level environment/defaults or untrusted pull_request_target exists. A full CLI scan was also run; the public API result remains authoritative for the displayed badge.

Actual remediation: enforce main/tag protection and genuine PR review; keep dependency updates, SAST and vulnerability reporting operating; complete a reviewed release. Current App networking is unavailable, so control changes and rescan are not claimed. Maintenance (new repository under 90 days), real contributor/review history and Passing badge need legitimate human operation. No fake commits, reviews, users, downloads or responses will be created.

The authenticated signed main-branch snapshot is an earned provenance artifact, not a formal Signed-Releases result. No score increase, Passing badge or certification is inferred. Native advisory review remains separate from pip-audit.
