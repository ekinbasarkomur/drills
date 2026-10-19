"""What LeetCode provides around a Python solution, plus the helpers the tests use.

Every problem file does `from _lc import *`, so List, Optional, ListNode, TreeNode, heapq,
collections ... are in scope exactly as on LeetCode, and the tests can build inputs from
plain values:

    build([1, 2, 3]) / to_list(head)            linked lists
    build_tree([1, None, 2]) / to_level_order   binary trees
    deep_sorted(v)                              answers "in any order"
    close(a, b)                                 doubles (or lists of them), 1e-5
"""
import bisect  # noqa: F401
import collections  # noqa: F401
import functools  # noqa: F401
import heapq  # noqa: F401
import itertools  # noqa: F401
import math  # noqa: F401
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
