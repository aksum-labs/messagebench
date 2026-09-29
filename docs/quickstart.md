# Quickstart

Python 3.12+, POSIX local filesystem. The tested native wheel is Linux x86_64 / CPython 3.12.
A C compiler and make are required for the source-build route below. See native-build.md. Run from the repository root.

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r dependency-lock.txt
.venv/bin/python scripts/build_native.py --archives /tmp/messagebench-native-archives \
  --out /tmp/messagebench-native-wheels --download
.venv/bin/python -m pip install --no-index --no-deps --force-reinstall \
  /tmp/messagebench-native-wheels/lxml-6.1.3-cp312-cp312-linux_x86_64.whl
.venv/bin/python -m pip install --no-deps --no-build-isolation .
.venv/bin/messagebench compare corpus/negative/reference-truncated.source.xml corpus/negative/reference-truncated.target.xml
# Expected exit code: 1; two XSD PASS results and one preservation FAIL.
.venv/bin/messagebench corpus verify corpus/index.json
# Expected exit code: 0; 68 expected classifications match, independent review pending.
```

Environment preparation above uses PyPI; actual commands work offline. The full development
lock includes test/security/build tools. Runtime-only requirements are in `runtime-lock.txt`.
For disconnected installation see [offline-install.md](offline-install.md).

Use `--format json --out result.json` for canonical evidence. The output parent must exist;
the output file must not exist. Keep reports private if inputs are private. No values switch.
Do not supply real messages for public bug reports; reconstruct a synthetic example.
