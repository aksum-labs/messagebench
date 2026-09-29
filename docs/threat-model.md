# Threat model: Gate 1 proof

Protected assets: local files; availability of the caller; confidentiality of input values;
integrity and scope of preservation reports. Attackers can supply XML/JSON/file paths. Trusted
computing base: reviewed package/code, Python, locked libraries, OS, and the code-pinned XSD.
Contracts can weaken their declared promises: a PASS is always conditional on contract review.

| Threat | Implemented control | Residual limitation |
|---|---|---|
| DTD/entity/remote resolution | Parser target rejects DOCTYPE, deny-all resolver, no network/entity expansion. UTF-16 regression tested. | Native parser defects remain possible; dependency maintenance required. |
| XInclude/PI/schema hints | Explicitly rejected, never expanded or used for resolution. | May reject otherwise harmless files; deliberate conservative prototype policy. |
| Resource exhaustion | Input/text/depth/element/assertion caps. Bounds applied while tree is built. | No OS sandbox or hard CPU/RSS ceiling; quarantine unknown inputs. |
| Symlink/FIFO/traversal | Directory-descriptor traversal, O_NOFOLLOW, O_NONBLOCK, regular-file check, no `..`/URLs. Output exclusive, mode 0600. | POSIX only; no defense against privileged filesystem/OS compromise. File mutation checks are best effort, not a filesystem snapshot. |
| Schema substitution | Constant SHA-256 allowlist, local catalog path confinement, no schema imports. | A maintainer/code compromise can replace trust anchors. |
| Executable contracts | Closed schema and comparator allowlist, no evaluation; duplicate IDs/keys rejected. | A syntactically valid weak contract can intentionally exclude meaningful information. |
| Leakage | No values/raw XML in reports; constant diagnostics; unknown coverage paths hashed. | Hashes and declared paths remain sensitive metadata. Contract text/IDs are author-controlled. |
| HTML injection | Escape all strings, no scripts/remote content, CSP. | Handling exported reports is the caller's responsibility. |
| False assurance | Exact version, draft status, explicit scope, required unsupported checks prevent pass. | Independent human semantic review is still missing. |
| Dependency/build compromise | Exact environment lock, inventory, local scans and SBOM. | No GitHub branch protection, signed public releases, or trusted external reproduction yet. |
| Public PR execution | No GitHub publication/workflows yet at this gate. | CI is deferred, not claimed secure by absence of evidence. |
| Adapter execution | Runtime has no adapter/plugin execution or network API. | Developer baseline scripts run only locally reviewed third-party code; never process private inputs in those scripts. |

A test found that lxml target cleanup initially masked safety errors. Preserving the original
rejection in `BoundedTree.close` fixed classification; regression tests cover the failure.
No claim of a professional security audit or production safety is made.
