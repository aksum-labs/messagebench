# Limitations

This is a local 0.1.0a2 alpha candidate. Independent review and public release remain pending.
The owner authorized development continuation before review; no reviewer identity is invented.

Only pacs.008.001.08 and pacs.002.001.10 are supported. The 68 cases are synthetic, with
pre-recorded expectations, not independently reviewed. camt.053 is excluded pending an
asset-specific redistribution basis. No scheme versions used by Ethiopian institutions are inferred.

Comparison is limited to declared fields and exact extractor versions. Unexamined information,
fees, structured remittance, calendar/timezone reasoning, institutional usage rules and arbitrary
nested associations are not validated. pacs.002 reason codes/text are independent multisets;
their pairing inside reason blocks is not promised. Cross-family/version translation is absent.
The keyed-items scalar comparator is unsupported; explicit unique transaction-key association
is supported. Missing/ambiguous keys prevent a required check from passing.

Reports are bounded to 5 MiB when reloaded. Large suites may exceed this report-reader limit.
Input quotas are not a process sandbox. CPU/RSS hard limits and continuous fuzzing are absent.
Hashes do not anonymize private data. Stored report validation verifies structure/consistency,
not authenticity; reports are unsigned claims unless independently authenticated.

Tested profile: Linux x86_64, CPython 3.12.3, lxml 6.1.3 with libxml2 2.15.4, libxslt 1.1.45
and libiconv 1.19. The bundled wheel is not a manylinux/cross-platform guarantee. Native Windows
fails closed under the POSIX file policy. Other platforms are unverified. Selected native
advisory triage is not complete historical vulnerability assurance.

Core branch coverage exceeds 90%; whole-package branch coverage does not. Targeted mutations
are not a comprehensive mutation score. Same-environment double builds are not independent
reproduction. No native-wheel reproducibility or identity-backed signature is claimed.

Original code/fixtures are Apache-2.0; ISO schema and third-party dependency rights remain
separate. Public mirror provenance is documented because official direct downloads returned
403. LGPL native source/notices/rebuild materials accompany the offline bundle.

No payment connectivity, live institution probing, custody, adapter execution, account system,
telemetry, certification, national rules, institutional endorsement or production-safety claim.
Pass means only the listed assertions passed for these inputs and versions.
