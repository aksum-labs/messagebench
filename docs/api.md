# Python API and report interface

Python 3.12+. Install the pinned native profile first. Importing the library does not set
process resource limits; the CLI entrypoint does. API callers must provide an equivalent
process budget when handling untrusted inputs.

```python
from pathlib import Path
from aksum_messagebench.engine import compare, inspect_file
from aksum_messagebench.schema_catalog import Catalog
from aksum_messagebench.corpus import verify
from aksum_messagebench.workflows import suite, load_result, regression
from aksum_messagebench.reports import canonical_json, render

result = compare(Path('source.xml'), Path('target.xml'), Path('contract.json'))
encoded = canonical_json(result)  # UTF-8 bytes, LF, sorted keys, no timestamp
assert result['exit_code'] in range(6)
```

- `compare(source: Path, target: Path, contract_path: Path, catalog_path: Path | None = None) -> dict`
  returns per-side schema checks, assertions, coverage, input/asset hashes and aggregate status.
- `inspect_file(path: Path, catalog: Catalog) -> tuple[dict, object | None]` validates and returns
  the internal XML tree only on success; do not export that tree with private data.
- `verify(manifest: Path, contract: Path | None = None) -> dict` verifies fixture hashes and
  pre-recorded classifications, not human review or the quality of deliberately defective adapters.
- `suite(manifest: Path, outputs: Path, contract: Path | None = None) -> dict` reads separately
  produced `<case-id>.xml` files. It cannot execute the producer.
- `load_result(path: Path) -> dict` checks closed report schema and internal consistency.
- `regression(previous: dict, current: dict) -> dict` compares equivalent scopes; source,
  contract, extractor, schema or comparator-semantic changes produce incomplete evidence.
- `render(report: dict, format: str) -> bytes` supports json, text, html and junit.

Configuration/security failures can raise `BenchError` with payload-free `.code` and `.exit_code`.
The CLI serializes errors, hides underlying exceptions and returns 0 pass, 1 failed assertion/input,
2 configuration, 3 incomplete evidence, 4 security/resource rejection or 5 internal failure.
Precedence is 5 > 4 > 2 > 3 > 1 > 0. No observed safe result is intentionally discarded to obtain PASS.

Contract schema: schemas/contracts.schema.json (Draft 2020-12). Report schemas:
schemas/report.schema.json and schemas/suite-report.schema.json. Per-check values are PASS,
FAIL, NOT_APPLICABLE, UNSUPPORTED and INDETERMINATE. Required unsupported/indeterminate checks
block PASS. Stored reports are not authenticated merely because their schema validates.

`keyed-items` requires per-transaction cardinality, keyed association with explicit unique
identifier fields, and `item_comparator`. Reordering is permitted only through that association;
missing, duplicate or changed key sets produce INDETERMINATE. Nested arbitrary object graphs
are outside this finite field model.

`datetime-equal` compares exact Gregorian XSD dateTime instants for four-digit positive years,
explicit timezone offsets and bounded lexical length. Fractions retain arbitrary decimal
precision within that bound. Missing timezone and unsupported calendar/range yield
INDETERMINATE. No Ethiopian calendar conversion or timezone guess occurs.

Identifiers remain strings, amounts retain lexical input and exact Decimal semantics,
currency is separate, and Unicode is exact unless NFC is explicitly requested. These
interfaces are versioned engineering scope; a v1.0 stable public API commitment requires
external review. Pass means only the listed assertions passed for these inputs and versions.
