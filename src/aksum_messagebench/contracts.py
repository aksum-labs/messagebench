"""Closed declarative contracts; only built-in comparisons, never expressions."""

import hashlib
from dataclasses import dataclass
from pathlib import Path

from jsonschema import Draft202012Validator

from .assets import data_root
from .errors import BenchError
from .input_guard import load_json


@dataclass(frozen=True)
class Contract:
    document: dict
    sha256: str


def load_contract(path: Path) -> Contract:
    try:
        document, raw = load_json(path)
    except BenchError as exc:
        if exc.exit_code == 3:
            raise BenchError("CONTRACT_MISSING", 2) from None
        raise
    schema, _ = load_json(data_root() / "schemas/contracts.schema.json")
    if next(Draft202012Validator(schema).iter_errors(document), None) is not None:
        raise BenchError("CONTRACT_INVALID", 2)
    assertions = document["assertions"]
    ids = [a["id"] for a in assertions]
    fields = [a["field"] for a in assertions]
    excluded = [e["field"] for e in document["exclusions"]]
    if len(set(ids)) != len(ids) or len(set(fields)) != len(fields):
        raise BenchError("CONTRACT_DUPLICATE_ASSERTION", 2)
    if len(set(excluded)) != len(excluded) or set(excluded) & set(fields):
        raise BenchError("CONTRACT_EXCLUSION_CONFLICT", 2)
    if not any(a["required"] for a in assertions):
        raise BenchError("CONTRACT_NO_REQUIRED_ASSERTIONS", 2)
    association = document["association"]
    if (
        association["mode"] == "single"
        and "keys" in association
        or association["mode"] == "keyed"
        and "keys" not in association
    ):
        raise BenchError("CONTRACT_ASSOCIATION_INVALID", 2)
    return Contract(document, hashlib.sha256(raw).hexdigest())
