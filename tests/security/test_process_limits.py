import os
import subprocess
import sys


def test_process_limits_and_restoration():
    code = """
import resource, signal, time
from aksum_messagebench.runtime_limits import command_limits
from aksum_messagebench.errors import BenchError
before = resource.getrlimit(resource.RLIMIT_AS)
try:
    with command_limits(cpu=2, wall=0.03, memory=512*1024*1024):
        assert resource.getrlimit(resource.RLIMIT_AS)[0] <= 512*1024*1024
        time.sleep(0.3)
    raise AssertionError('wall deadline ignored')
except BenchError as exc:
    assert exc.exit_code == 4 and exc.code == 'PROCESS_RESOURCE_LIMIT'
assert resource.getrlimit(resource.RLIMIT_AS) == before
assert signal.getitimer(signal.ITIMER_REAL)[0] == 0
"""
    result = subprocess.run(
        [sys.executable, "-c", code], env=os.environ.copy(), capture_output=True, timeout=5
    )
    assert result.returncode == 0, result.stderr.decode()


def test_command_boundary_still_works():
    result = subprocess.run(
        [sys.executable, "-m", "aksum_messagebench", "--version"], capture_output=True, timeout=5
    )
    assert result.returncode == 0
