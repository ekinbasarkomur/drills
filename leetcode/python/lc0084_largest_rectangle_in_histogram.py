"""
84. Largest Rectangle in Histogram · Hard · https://leetcode.com/problems/largest-rectangle-in-histogram/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]), 10, "Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])")


def test_example_2():
    check(Solution().largestRectangleArea([2, 4]), 4, "Solution().largestRectangleArea([2, 4])")
