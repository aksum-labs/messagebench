"""Bounded regular-file reads using directory descriptors on POSIX.

No URL interpretation, symlink traversal, parent traversal or FIFO blocking.
Unsupported operating systems fail closed instead of silently weakening checks.
"""

import json
import os
import stat
from pathlib import Path
from typing import Any

from .errors import BenchError

MAX_BYTES = 5 * 1024 * 1024


def read_local(path: Path | str, *, root: Path | None = None, limit: int = MAX_BYTES) -> bytes:
    raw = str(path)
    if not raw or ":" in raw or "\x00" in raw or ".." in Path(raw).parts:
        raise BenchError("UNSAFE_PATH", 4)
    if root is not None:
        if Path(raw).is_absolute():
            raise BenchError("UNSAFE_PATH", 4)
        path = root.absolute() / raw
    path = Path(path).absolute()
    if os.name != "posix":
        raise BenchError("PLATFORM_UNSUPPORTED", 3)
    descriptor = None
    directory = None
    try:
        directory = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
        for part in path.parts[1:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            os.close(directory)
            directory = child
        descriptor = os.open(
            path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory
        )
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise BenchError("NOT_REGULAR_FILE", 4)
        if info.st_size > limit:
            raise BenchError("INPUT_SIZE_LIMIT", 4)
        chunks = []
        remaining = limit + 1
        while remaining:
            chunk = os.read(descriptor, min(remaining, 65536))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        data = b"".join(chunks)
        if len(data) > limit:
            raise BenchError("INPUT_SIZE_LIMIT", 4)
        after = os.fstat(descriptor)
        if (info.st_size, info.st_mtime_ns, info.st_ctime_ns) != (
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        ):
            raise BenchError("INPUT_CHANGED_DURING_READ", 3)
        return data
    except FileNotFoundError:
        raise BenchError("INPUT_MISSING", 3) from None
    except OSError:
        raise BenchError("FILE_ACCESS_REJECTED", 4) from None
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if directory is not None:
            os.close(directory)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise BenchError("JSON_DUPLICATE_KEY", 2)
        result[key] = value
    return result


def _no_constant(value: str) -> None:
    raise BenchError("JSON_NONFINITE_NUMBER", 2)


def load_json(
    path: Path | str, *, root: Path | None = None, limit: int = 1024 * 1024
) -> tuple[dict, bytes]:
    data = read_local(path, root=root, limit=limit)
    try:
        result = json.loads(data, object_pairs_hook=_unique_object, parse_constant=_no_constant)
    except (ValueError, UnicodeError, RecursionError):
        raise BenchError("JSON_INVALID", 2) from None
    if not isinstance(result, dict):
        raise BenchError("JSON_OBJECT_REQUIRED", 2)
    stack = [(result, 0)]
    while stack:
        value, depth = stack.pop()
        if depth > 32:
            raise BenchError("JSON_DEPTH_LIMIT", 4)
        if isinstance(value, dict):
            stack.extend((v, depth + 1) for v in value.values())
        elif isinstance(value, list):
            stack.extend((v, depth + 1) for v in value)
    return result, data
