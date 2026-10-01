# Reproducibility appendix

Record `git rev-parse HEAD`; retain the engineering measurement commit separately from the current documentation/publication commit. Install the exact hashed lock and documented native profile as in docs/reproduce.md. Use Python 3.12 on Linux for the verified profile.

```bash
python -m pip install --require-hashes -r dependency-lock-hashed.txt
python scripts/build_native.py --archives /tmp/mb-native-src --out /tmp/mb-native-wheel --download
python -m pip install --no-index --no-deps --force-reinstall --require-hashes --find-links /tmp/mb-native-wheel -r /tmp/mb-native-wheel/install-requirements.txt
python -m pip install --no-deps --no-build-isolation -e .
coverage run -m pytest -q
coverage json -o /tmp/mb-coverage.json
python scripts/check_coverage.py /tmp/mb-coverage.json
messagebench corpus verify corpus/index.json
messagebench corpus verify corpus/extended/index.json --contract contracts/pacs008-extended.json
messagebench corpus verify corpus/pacs002/index.json --contract contracts/pacs002-preserve.json
python scripts/differential_xsd.py
python scripts/security_corpus.py
python scripts/mutations.py
python fuzz/smoke.py --iterations 100000
python fuzz/contracts.py --iterations 10000
python scripts/benchmark.py > /tmp/messagebench-benchmark-rerun.json
```

Evidence scripts can regenerate tracked evidence. Run them in a disposable checkout and inspect differences. A new timing result will differ and must not be presented as reproducing an identical latency. Differential processor agreement is bounded to the synthetic corpus; a missing processor is not agreement. Use scripts/baseline.py with the documented inspected Cognis source for that optional baseline; no copied upstream code is bundled here.

The historical benchmark cycled six small pairs and included per-pair schema compilation. The benchmark file records its hardware/conditions. Current public CI runs identify separate source commits. A fresh offline install is run outside the checkout with network sockets disabled, as documented in docs/offline-install.md and scripts/verify_offline_install.py.

Two identical unsigned builds in one environment are not independent reproduction. Signatures must be verified against exact workflow/ref and OIDC issuer; no signature is evidence of human review. See docs/release-verification.md and SECURITY-EVIDENCE.md for earned status.
