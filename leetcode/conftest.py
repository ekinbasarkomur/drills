"""Make a crash inside a solution read like the test report around it.

pytest's own traceback for, say, a bad pd.DataFrame() call is a dozen frames deep
in pandas before it reaches the line that is actually wrong. Only the frames in
this repository are ours to fix, so that is all this prints.

Assertion failures are left alone: pytest rewrites those, and check() in
leetcode/python/_pd.py already explains itself.
"""
import pytest


def _ours(entry):
    path = str(entry.path)
    return "site-packages" not in path and "/lib/python3" not in path


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed or call.excinfo is None:
        return
    if call.excinfo.errisinstance(AssertionError):
        return

    frames = [e for e in call.excinfo.traceback if _ours(e)]
    if not frames:
        return

    exc = call.excinfo.value
    lines = [f"{item.name}: your code raised {type(exc).__name__}: {exc}", ""]
    for entry in frames:
        source = entry.statement.lines[0].strip() if entry.statement.lines else ""
        lines.append(f"  {entry.path.name}:{entry.lineno + 1}  {source}")
    report.longrepr = "\n".join(lines)
