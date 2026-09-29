"""Locate bundled resources or the source checkout, without runtime downloads."""

from pathlib import Path


def data_root() -> Path:
    package = Path(__file__).parent
    bundled = package / "data"
    return bundled if bundled.is_dir() else package.parents[1]
