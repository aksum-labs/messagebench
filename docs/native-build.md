# Native XML dependency build

The PyPI lxml 6.1.3 wheel inspected here contained libxml2 2.14.6 and libxslt 1.1.43,
including some vendor backports. Python package advisory scans do not describe every native
component. The local hardened build uses libxml2 2.15.4, libxslt 1.1.45 and libiconv 1.19.
Versions do not prove absence of vulnerabilities; track component advisories and reachability.

The build script pins the source archive hashes and build Python packages. It needs Linux,
CPython 3.12, a C compiler, make, curl (only for requested downloads) and the development
lock installed. Downloads happen only in this developer build step, never at runtime.

```sh
.venv/bin/python -m pip install -r dependency-lock.txt
.venv/bin/python scripts/build_native.py --archives /tmp/messagebench-native-archives \
  --out /tmp/messagebench-native-wheels --download
.venv/bin/python -m pip install --no-index --no-deps --force-reinstall \
  /tmp/messagebench-native-wheels/lxml-6.1.3-cp312-cp312-linux_x86_64.whl
```

With all four verified archives present, omit `--download`. The script makes one explicit
build-helper patch to upstream lxml: a pinned native version uses its known directory URL
without retrieving a remote directory listing. No runtime lxml source is changed. Wheel
build uses `--no-index --no-build-isolation`. Source archives and helper hashes are recorded.
The native wheel itself has not been established reproducible; do not infer that from the
separate MessageBench wheel/sdist reproducibility test.

libxml2/libxslt are MIT-licensed; libiconv is LGPL-2.1-or-later. Distribution of the static
native wheel needs the applicable notices, corresponding source and relinking/rebuild
materials. The final offline release bundle must include these, including this build
script and the original pinned source archives. Until that bundle is verified, this is a
local engineering build, not an approved redistributed native binary. A normal unqualified
`pip install lxml==6.1.3` may select a different wheel with different native components.

The developer PR checks build the native wheel from the pinned archives before processing
synthetic XML. They do not silently accept the stock wheel as equivalent. The dependency
advisory job separately scans Python packages and does not claim to audit bundled C code.

The runtime now rejects libxml2 below 2.15.4 or libxslt below 1.1.45 with exit 3 and
`NATIVE_XML_PROFILE_UNSUPPORTED`, before parsing XML. This conservative minimum profile
avoids silently using the older stock wheel. It is not an assertion that every newer build
is secure or behaviorally identical. Run the corpus after any native upgrade; inspect the
SBOM and release manifest for the actual native versions and wheel digest.

The original libiconv source archive also contains the separate iconv command-line program
under GPL-3.0-or-later, with COPYING retained. The linked library uses LGPL-2.1-or-later;
the GPL command-line program is not linked into the lxml wheel. Full original archives
preserve their per-file notices; they are not relicensed under Apache-2.0.
