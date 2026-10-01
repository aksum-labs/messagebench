#!/bin/bash
# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
set -euxo pipefail
cd "$SRC/messagebench"
# Native dependencies must be built for this builder's OS; never reuse runner wheels.
# Python guidance is the primary assurance. Do not infer complete native ASan coverage.
python3 scripts/build_native.py --archives "$WORK/native-sources" --out "$WORK/native-wheels" --download
python3 -m pip install --no-index --no-deps --force-reinstall --require-hashes --find-links "$WORK/native-wheels" -r "$WORK/native-wheels/install-requirements.txt"
python3 -m pip install --no-deps --no-build-isolation .
compile_python_fuzzer fuzz/coverage_guided.py --collect-all aksum_messagebench --collect-all jsonschema --collect-all jsonschema_specifications --collect-all referencing --collect-all lxml --collect-all atheris
python3 - "$OUT" <<'PY'
import sys, zipfile
from pathlib import Path
out = Path(sys.argv[1])
with zipfile.ZipFile(out / 'coverage_guided_seed_corpus.zip', 'w') as z:
    for seed in sorted(Path('fuzz/coverage-guided/seeds').iterdir()):
        z.write(seed, seed.name)
(out / 'coverage_guided.options').write_text('[libfuzzer]\nmax_len = 16384\ntimeout = 10\nrss_limit_mb = 1024\n')
PY
