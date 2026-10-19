"""
346. Moving Average from Data Stream · Easy · https://leetcode.com/problems/moving-average-from-data-stream/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MovingAverage:

    def __init__(self, size: int):
        raise NotImplementedError
    def next(self, val: int) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    obj = MovingAverage(3)
    obj.next(1)
    obj.next(10)
    obj.next(3)
    obj.next(5)
