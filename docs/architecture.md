# Architecture

`input_guard` reads bounded regular files without symlinks or URL resolution.
`xml_reader` applies resource and parser policy while building trees. `schema_catalog`
compiles the two exact hash-pinned pacs.008.001.08 and pacs.002.001.10 XSDs. `contracts` validates JSON against
an owned, closed Draft 2020-12 schema. `extractors/pacs008_001_08` selects exact expanded
QNames and emits internal facts with original QName occurrence paths.

`comparators` operates on typed facts. `engine` requires valid inputs and explicit single
transaction association, collects safe input results, evaluates declared assertions and
applies exit precedence. `coverage` partitions input occurrences. Paths for coverage are
hashed incrementally during a linear traversal; this avoids repeated sibling scans and
large repeated long-path strings. `reports` serializes deterministic redacted evidence.
`corpus` verifies stored bytes and recorded expectations. `cli` only reads files.

Internal APIs are experimental. No stable v1 API, plugin interface, executable contract,
adapter process, network client, service or database. Build/development scripts are outside
the installed runtime package and may invoke reviewed baseline/build tools explicitly.
The optional Cognis baseline script refuses any source other than its pinned reviewed hash.

Supported runtime CLI: `inspect`, `compare`, `corpus verify`. Report output is selected on
`compare`; standalone suite/report/regression commands are deferred behind independent review.
