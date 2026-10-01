# Offline installation

Use the prepared review bundle on compatible Linux x86_64 / CPython 3.12. Verify its
SHA256SUMS against a trusted copy, then create a fresh environment outside the checkout:

```sh
sha256sum -c SHA256SUMS
python3.12 -m venv review-env
review-env/bin/python -m pip install --no-index --find-links wheelhouse \
  --require-hashes -r install-requirements.txt
review-env/bin/messagebench corpus verify
```

Expected: all 100 recorded classifications match, including intentional failures. The lock
includes the specifically built native wheel; downloading the ordinary upstream lxml wheel
alone is insufficient for this tested native profile. Runtime rejects older native libraries.

Connected developer preparation is documented in native-build.md and reproduce.md. It is
separate from offline runtime. The bundle contains corresponding native sources, notices,
SBOM and rebuild instructions. It is platform-specific, unsigned and for local review.

## Prepare a new bundle using cleared local wheels

Developer preparation can reuse an existing cleared wheelhouse without a package index. All dependency pins and hash checks still apply:

```sh
python scripts/prepare_bundle.py --release /path/to/clean-release \
  --native /path/to/native-build --archives /path/to/native-sources \
  --wheel-cache /path/to/cleared-wheelhouse --out /path/to/new-bundle
```

The cache is an input, not a trusted source of new versions: pip uses `--no-index`, the reviewed hash requirements and exact pins. The original native/source rights checks are unchanged. A fresh installation of the refreshed local bundle passed from outside the source checkout with Python socket calls denied; measured evidence is in `evidence/local-recognition-offline-install.json`. This is local verification, not independent reproduction or a signature.
