# Quickstart

Python 3.12+, POSIX local filesystem. The tested native wheel is Linux x86_64 / CPython 3.12.
A C compiler and make are required for the source-build route below. See native-build.md. Run from the repository root.

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r dependency-lock-hashed.txt
.venv/bin/python scripts/build_native.py --archives /tmp/messagebench-native-archives \
  --out /tmp/messagebench-native-wheels --download
.venv/bin/python -m pip install --no-index --no-deps --force-reinstall \
  --require-hashes --find-links /tmp/messagebench-native-wheels \
  -r /tmp/messagebench-native-wheels/install-requirements.txt
.venv/bin/python -m pip install --no-deps --no-build-isolation .
.venv/bin/messagebench compare corpus/negative/reference-truncated.source.xml corpus/negative/reference-truncated.target.xml
# Expected exit code: 1; two XSD PASS results and one preservation FAIL.
.venv/bin/messagebench corpus verify corpus/index.json
# Expected exit code: 0; 100 expected classifications match, independent human review required.
```

Environment preparation above uses PyPI; actual commands work offline. The full development
lock includes test/security/build tools. Runtime-only requirements are in `runtime-lock.txt`.
For disconnected installation see [offline-install.md](offline-install.md).

Use `--format json --out result.json` for canonical evidence. The output parent must exist;
the output file must not exist. Keep reports private if inputs are private. No values switch.
Do not supply real messages for public bug reports; reconstruct a synthetic example.
