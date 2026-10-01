# LFDT technical attachment

MessageBench checks whether externally supplied financial-message file pairs preserve the information promised by a versioned engineering contract. It runs offline, executes no adapter, and produces deterministic, redacted reports with explicit coverage limits.

Exact engineering scope: pacs.008.001.08 and pacs.002.001.10 only. Ten contracts declare 38 required assertions over 27 extractable fields. A required unsupported or indeterminate check prevents overall PASS. Exclusions and unexamined fields remain visible.

100 synthetic paired cases; 140 passing tests; 99/102 core semantic branches (97.06%); 40/40 targeted mutants killed; 200 XML documents with matching XSD classifications across lxml and xmlschema; 100,000 parser fuzz iterations and 10,000 contract mutations.

Local measured six-pair cycling benchmark: 1,000 in-process comparisons, 80.624 pairs/s, p50 11.741 ms, p95 15.584 ms, peak RSS 40,360 KiB. See evidence/benchmark.json for hardware and conditions; not a batch benchmark, SLA or independent reproduction.

Security: bounded secure XML parsing; no DTD/entities/network/XInclude; closed non-executable contracts; redacted reports; escaped static HTML; dependency/native rights inventory; read-only PR checks. The repository has no payment initiation, banking connectivity or adapter execution.

No independent human review or institutional adoption has been established. No certification, production-safety, national-standard or regulator/vendor endorsement claim is made. camt.053.001.08 is excluded because joint-contributor redistribution permission was not established. A PASS covers only listed assertions, never the whole document.
