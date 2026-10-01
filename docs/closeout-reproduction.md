# Reproduce release close-out additions

Use CPython 3.12 Linux x86-64 with the reviewed native wheel installed, then the pinned developer lock. Runtime remains offline; developer advisory/tool preparation is an explicit connected step.

```bash
ruff check src tests scripts fuzz
ruff format --check src tests scripts fuzz
mypy src
coverage run -m pytest -q
coverage json -o coverage-ci.json
python scripts/check_coverage.py coverage-ci.json
python scripts/fetch_dev_tools.py --out /tmp/messagebench-tools actionlint cue
/tmp/messagebench-tools/actionlint/actionlint .github/workflows/*.yml
/tmp/messagebench-tools/cue/cue vet schemas/security-insights-v2.2.0.cue security-insights.yml -d '#SecurityInsights'
python scripts/scheduled_audit.py --out /tmp/messagebench-python-advisories
python scripts/check_licenses.py
python scripts/check_recognition.py
python scripts/review_packet.py prepare
python scripts/review_packet.py verify
```

The final command intentionally rejects missing genuine reviews. Preparing a packet never supplies approvals.

```bash
python -m pip install --require-hashes --no-deps -r fuzz/coverage-guided-lock.txt
mkdir -p /tmp/messagebench-guided/corpus /tmp/messagebench-guided/crashes
cp fuzz/coverage-guided/seeds/* /tmp/messagebench-guided/corpus/
MESSAGEBENCH_FUZZ_COUNTS=/tmp/messagebench-guided/counts.json \
  python fuzz/coverage_guided.py -runs=10000 -max_len=16384 -timeout=10 -rss_limit_mb=1024 \
  -artifact_prefix=/tmp/messagebench-guided/crashes/ /tmp/messagebench-guided/corpus
```

The fuzzer checkpoints boundary invocation counts, because libFuzzer exits without invoking normal Python atexit handlers. Counters are not native sanitizer coverage or whole-runtime branch coverage. Keep production files out of seeds and artifacts.

A fresh standard-index installation of the stock pinned lxml wheel can fail `NATIVE_XML_PROFILE_UNSUPPORTED`; that is deliberate evidence of an unsupported profile, not a preservation assertion failure. Use the complete supported offline bundle and `scripts/verify_offline_install.py --python /path/to/fresh/venv/bin/python`. The manifest covers nested bundle files and must be verified inside the full extracted bundle. Main-snapshot and reviewed-tag signature identities are distinct.


## ClusterFuzzLite native-stack campaign

The existing scheduled-security workflow builds `.clusterfuzzlite/Dockerfile` with digest-pinned CPython 3.12 and the official Python builder, compiles the reviewed native XML stack, freezes the real fuzz boundary, and runs 10,000 bounded iterations. It uses no issue/comment APIs and no publishing credentials. The local run completed in 482 seconds, reaching all four boundaries; `evidence/clusterfuzzlite-local.json` records observed counters and log hashes. These counters are not whole-program branch coverage. The builder's address/fuzzer compile flags and runtime preload do not establish complete native sanitizer coverage or independent review.

```bash
docker build -f .clusterfuzzlite/Dockerfile -t messagebench-cfl .
mkdir -p /tmp/messagebench-cfl/out /tmp/messagebench-cfl/work
docker run --rm -e FUZZING_LANGUAGE=python -e SANITIZER=address \
  -v /tmp/messagebench-cfl/out:/out -v /tmp/messagebench-cfl/work:/work messagebench-cfl compile
mkdir -p /tmp/messagebench-cfl/out/corpus /tmp/messagebench-cfl/out/crashes
cp fuzz/coverage-guided/seeds/* /tmp/messagebench-cfl/out/corpus/
docker run --rm -e MESSAGEBENCH_FUZZ_COUNTS=/out/boundary-counts.json \
  -v /tmp/messagebench-cfl/out:/out messagebench-cfl /out/coverage_guided \
  -runs=10000 -max_len=16384 -timeout=10 -rss_limit_mb=1024 \
  -artifact_prefix=/out/crashes/ /out/corpus
```
