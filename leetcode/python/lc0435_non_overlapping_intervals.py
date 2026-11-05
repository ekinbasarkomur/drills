"""
435. Non-overlapping Intervals · Medium · https://leetcode.com/problems/non-overlapping-intervals/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1, "Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])")


def test_example_2():
    check(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]), 2, "Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])")


def test_example_3():
    check(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]), 0, "Solution().eraseOverlapIntervals([[1, 2], [2, 3]])")
