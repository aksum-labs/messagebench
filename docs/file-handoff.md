# Adapter file handoff

Run an adapter in your own environment. MessageBench does not start it, load its code or contact it. For each case ID in `corpus/index.json`, supply the transformation of that case's **source** as `adapter-outputs/<case-id>.xml`. Outputs may come from Java, Rust, Python, a vendor tool or manual export.

The default release manifest has 100 case IDs and selects a bundled versioned contract per case.
`--contract` explicitly overrides that selection for every case. The six-case Node demonstration
uses `corpus/gate1-index.json`.

The suite evaluates preservation promises. It does not compare output bytes against the corpus's deliberately defective target or reward reproducing a known defect. Missing outputs produce incomplete evidence (exit 3); unsafe files take precedence (exit 4). It checks every case when safe and retains all observed results. Input source hashes must match the manifest.

```sh
mkdir -p report
messagebench suite corpus/index.json --outputs ./adapter-outputs --out ./report
```

The output directory must exist. Existing result files are never overwritten. A separate directory per run preserves prior evidence. The suite result contains a redacted comparison result per case. Report conversion accepts comparison and suite reports, including HTML and JUnit. Stored report input is bounded to 5 MiB.

```sh
messagebench compare corpus/negative/reference-truncated.source.xml \
  corpus/negative/reference-truncated.target.xml \
  --format json --out report/comparison.json
messagebench report report/comparison.json --format html --out report/index.html
messagebench regression previous/result.json current/result.json
```

Regression checks source hash, contract hash, schema hash, extractor version and assertion scope. A changed scope is incomplete evidence, not a successful regression test. Improved current evidence can pass after an earlier preservation failure. Reports are validated for structure, required assertions, status aggregation and disjoint coverage counts; these checks do not authenticate a report or prove its author actually ran the tool. Regenerate evidence from the hashed inputs when trust matters.
