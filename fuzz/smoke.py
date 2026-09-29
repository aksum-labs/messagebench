"""Bounded deterministic malformed-input smoke test, not a full fuzzing claim."""

import argparse
import random

from aksum_messagebench.errors import BenchError
from aksum_messagebench.xml_reader import parse_xml

parser = argparse.ArgumentParser()
parser.add_argument("--iterations", type=int, default=1000)
args = parser.parse_args()
if not 1 <= args.iterations <= 100000:
    parser.error("iterations must be in [1, 100000]")
rng = random.Random(20260929)
seeds = [b"<a/>", b"<!DOCTYPE a [<!ENTITY x 'x'>]><a>&x;</a>", b"<a><b>text</b></a>"]
for _ in range(args.iterations):
    value = bytearray(rng.choice(seeds))
    for _ in range(rng.randrange(1, 10)):
        value.insert(rng.randrange(len(value) + 1), rng.randrange(256))
    try:
        parse_xml(bytes(value))
    except BenchError:
        pass
print(f"Completed {args.iterations} deterministic parser mutations; no unexpected exceptions")
