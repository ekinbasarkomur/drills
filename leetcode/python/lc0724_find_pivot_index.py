"""
724. Find Pivot Index · Easy · https://leetcode.com/problems/find-pivot-index/
Plan: Aşama 0 · Sliding Window ve Prefix Sum

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().pivotIndex([1, 7, 3, 6, 5, 6]), 3, "Solution().pivotIndex([1, 7, 3, 6, 5, 6])")


def test_example_2():
    check(Solution().pivotIndex([1, 2, 3]), -1, "Solution().pivotIndex([1, 2, 3])")


def test_example_3():
    check(Solution().pivotIndex([2, 1, -1]), 0, "Solution().pivotIndex([2, 1, -1])")
