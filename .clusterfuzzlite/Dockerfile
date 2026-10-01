# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
# Official builder is Python 3.11; copy a digest-pinned CPython 3.12 userland.
FROM python:3.12-bullseye@sha256:7cc929040c5e8cf6036c5099d62a83708427c131fb7a7c965b5ba51e995eea1c AS python312
FROM gcr.io/oss-fuzz-base/base-builder-python@sha256:58f80c90a90944b68b8e70b98e38997ee9396225311cfb0f3aea78671446ab4e
COPY --from=python312 /usr/local/bin/ /usr/local/bin/
COPY --from=python312 /usr/local/lib/ /usr/local/lib/
COPY --from=python312 /usr/local/include/ /usr/local/include/
COPY --from=python312 /usr/bin/pkg-config /usr/bin/pkg-config
RUN python3 -c 'import sys; assert sys.version_info[:2] == (3,12)'
COPY dependency-lock-hashed.txt fuzz/coverage-guided-lock.txt .clusterfuzzlite/freezer-lock.txt /tmp/locks/
RUN python3 -m pip install --require-hashes -r /tmp/locks/dependency-lock-hashed.txt \
    && python3 -m pip install --require-hashes --no-deps -r /tmp/locks/coverage-guided-lock.txt \
    && python3 -m pip install --require-hashes --no-deps -r /tmp/locks/freezer-lock.txt
COPY --from=python312 /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0 /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
COPY --from=python312 /usr/share/doc/pkg-config/ /usr/share/doc/pkg-config/
COPY . $SRC/messagebench
WORKDIR $SRC/messagebench
COPY .clusterfuzzlite/build.sh $SRC/build.sh
