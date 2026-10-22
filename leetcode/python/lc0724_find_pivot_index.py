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
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3


def test_example_2():
    assert Solution().pivotIndex([1, 2, 3]) == -1


def test_example_3():
    assert Solution().pivotIndex([2, 1, -1]) == 0
