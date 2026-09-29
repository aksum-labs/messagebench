# Offline installation

The runtime never downloads anything. A separate connected staging machine prepares a
wheelhouse for the target Python/OS/CPU. The local review bundle is Linux x86_64/Python 3.12;
other platforms require their own compatible wheels and tests.

```sh
# Connected preparation, not part of message processing:
python -m pip download --only-binary=:all: --dest wheelhouse -r runtime-lock.txt
python -m build --no-isolation
cp dist/*.whl wheelhouse/
(cd wheelhouse && sha256sum *.whl > SHA256SUMS)
# Transfer the wheelhouse, checksums and source review packet through your approved channel.

# Disconnected machine:
(cd wheelhouse && sha256sum -c SHA256SUMS)
python3.12 -m venv offline-env
offline-env/bin/python -m pip install --no-index --find-links wheelhouse aksum-messagebench==0.1.0a1
offline-env/bin/messagebench corpus verify
```

Hashes detect changes against trusted hashes; they do not authenticate an untrusted bundle.
This local proof is unsigned and not approved for public release. Runtime dependencies are
exactly pinned. Development tools can be staged similarly using dependency-lock.txt.
