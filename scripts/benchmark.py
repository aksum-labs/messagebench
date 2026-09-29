"""Measure 1,000 actual small-pair comparisons; no synthetic timing claims."""

import json
import platform
import resource
import statistics
import time
from pathlib import Path

from lxml import etree

from aksum_messagebench.engine import compare

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "corpus/gate1-index.json").read_text())
pairs = [(root / "corpus" / c["source"], root / "corpus" / c["target"]) for c in manifest["cases"]]
latencies = []
for i in range(1000):
    before, after = pairs[i % len(pairs)]
    start = time.perf_counter_ns()
    compare(before, after, root / "contracts/pacs008-preserve.json")
    latencies.append((time.perf_counter_ns() - start) / 1e6)
ordered = sorted(latencies)
cpu = next(
    (
        s.split(":", 1)[1].strip()
        for s in Path("/proc/cpuinfo").read_text().splitlines()
        if s.startswith("model name")
    ),
    platform.processor(),
)
mem = next(s for s in Path("/proc/meminfo").read_text().splitlines() if s.startswith("MemTotal:"))
result = {
    "iterations": len(latencies),
    "cpu": cpu,
    "memory_reported_by_os": mem,
    "os": platform.platform(),
    "python": platform.python_version(),
    "lxml": etree.LXML_VERSION,
    "libxml2": etree.LIBXML_VERSION,
    "corpus_version": manifest["version"],
    "distinct_pairs": len(pairs),
    "corpus_input_bytes": sum(a.stat().st_size + b.stat().st_size for a, b in pairs),
    "p50_ms": statistics.median(latencies),
    "p95_ms": ordered[949],
    "throughput_pairs_per_second": 1000 / (sum(latencies) / 1000),
    "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "method": "In-process full compare including file reads, contract validation and schema "
    "compilation each iteration; six small pairs cycled, OS cache warm; no CLI "
    "startup. RSS is process peak, not incremental allocation. Shared host, "
    "single run; not an SLA or large/batch performance claim.",
}
print(json.dumps(result, sort_keys=True, indent=2))
