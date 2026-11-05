"""What LeetCode provides around a Python solution, plus the helpers the tests use.

Every problem file does `from _lc import *`, so List, Optional, ListNode, TreeNode, heapq,
collections ... are in scope exactly as on LeetCode, and the tests can build inputs from
plain values:

    build([1, 2, 3]) / to_list(head)            linked lists
    build_tree([1, None, 2]) / to_level_order   binary trees
    deep_sorted(v)                              answers "in any order"
    close(a, b)                                 doubles (or lists of them), 1e-5

The tests assert through two helpers instead of a bare `assert`, so a run shows what
it tried as well as what broke:

    check(got, want, "call()")                  got == want   (or `is`, with op="is")
    check_true(got, "call()")                   got is truthy

Both print the call and the value they got every time, and on a mismatch raise an
AssertionError naming the test, the value that came back and the one that was wanted.
Printing needs pytest's capture off; `make <id>` and `make py-<id>` already pass -s.
"""
import bisect  # noqa: F401
import collections  # noqa: F401
import functools  # noqa: F401
import heapq  # noqa: F401
import itertools  # noqa: F401
import math  # noqa: F401
import os
import random  # noqa: F401
import re  # noqa: F401
import string  # noqa: F401
import threading  # noqa: F401
from bisect import bisect_left, bisect_right  # noqa: F401
from collections import Counter, OrderedDict, defaultdict, deque  # noqa: F401
from functools import cache, lru_cache, reduce  # noqa: F401
from heapq import heapify, heappop, heappush, heappushpop, heapreplace  # noqa: F401
from itertools import accumulate, combinations, permutations, product  # noqa: F401
from math import ceil, floor, gcd, inf, isqrt, sqrt  # noqa: F401
from typing import *  # noqa: F401,F403

from list_node import ListNode, build, to_list  # noqa: F401
from tree_node import TreeNode, build_tree, to_level_order  # noqa: F401


def deep_sorted(v):
    if isinstance(v, list):
        return sorted((deep_sorted(x) for x in v), key=repr)
    return v


def close(a, b, tol=1e-5):
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(close(x, y, tol) for x, y in zip(a, b))
    return a is not None and b is not None and abs(a - b) < tol


# ------------------------------------------------------------------ assertions

_shown = None  # the test whose heading is already on screen


def _case():
    """The name of the test being run, for the heading above its output."""
    current = os.environ.get("PYTEST_CURRENT_TEST", "")
    return current.split("::")[-1].split(" ")[0] or "check"


def _heading():
    """Print `--- test_name ---` once per test, however many checks it makes."""
    global _shown
    current = os.environ.get("PYTEST_CURRENT_TEST", "")
    case = _case()
    if current != _shown:
        _shown = current
        print(f"\n--- {case} " + "-" * max(3, 68 - len(case)))
    return case


def _short(text, limit=160):
    """The call as one line. A problem whose input is a 256-element list would
    otherwise bury the result it produced."""
    if not text:
        return "the call"
    one = " ".join(text.split())
    return one if len(one) <= limit else one[: limit - 3] + "..."


def check(got, want, call=None, op="=="):
    __tracebackhide__ = True  # point the failure at the test, not at this file
    case = _heading()
    print(f"  {_short(call)}  ->  {got!r}")
    if (got is want) if op == "is" else (got == want):
        return
    raise AssertionError(
        f"{case}: {_short(call)} returned the wrong value\n\n"
        f"  got:    {got!r}\n"
        f"  wanted: {want!r}" + ("   (compared with `is`)" if op == "is" else "")
    )


def check_true(got, call=None):
    __tracebackhide__ = True
    case = _heading()
    print(f"  {_short(call)}  ->  {got!r}")
    if got:
        return
    raise AssertionError(
        f"{case}: {_short(call)} is not true\n\n"
        f"  got:    {got!r}\n"
        f"  wanted: a true value"
    )
