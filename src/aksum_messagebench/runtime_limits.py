# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""POSIX command-process limits; never execute an adapter or alter library callers."""

import math
import resource
import signal
from contextlib import contextmanager

from .errors import BenchError

CPU_SECONDS = 60
WALL_SECONDS = 120
ADDRESS_SPACE = 1024 * 1024 * 1024


def _rejected(signum, frame):
    raise BenchError("PROCESS_RESOURCE_LIMIT", 4)


@contextmanager
def command_limits(cpu=CPU_SECONDS, wall=WALL_SECONDS, memory=ADDRESS_SPACE):
    """Set and restore soft limits. Existing stricter limits are never raised."""
    previous = {}
    handlers = {}
    timer = None
    try:
        used = resource.getrusage(resource.RUSAGE_SELF)
        cpu_budget = math.ceil(used.ru_utime + used.ru_stime) + cpu
        for kind, requested in ((resource.RLIMIT_CPU, cpu_budget), (resource.RLIMIT_AS, memory)):
            old = resource.getrlimit(kind)
            previous[kind] = old
            finite = [v for v in (old[0], old[1], requested) if v != resource.RLIM_INFINITY]
            resource.setrlimit(kind, (min(finite), old[1]))
        for sig in (signal.SIGXCPU, signal.SIGALRM):
            handlers[sig] = signal.signal(sig, _rejected)
        timer = signal.getitimer(signal.ITIMER_REAL)
        signal.setitimer(signal.ITIMER_REAL, min(wall, timer[0]) if timer[0] else wall)
        yield
    finally:
        if timer is not None:
            signal.setitimer(signal.ITIMER_REAL, *timer)
        for sig, previous_handler in handlers.items():
            signal.signal(sig, previous_handler)
        for kind, old in previous.items():
            resource.setrlimit(kind, old)
