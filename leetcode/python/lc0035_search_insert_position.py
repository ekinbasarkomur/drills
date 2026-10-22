"""
35. Search Insert Position · Easy · https://leetcode.com/problems/search-insert-position/
Plan: Aşama 0 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2


def test_example_2():
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1


def test_example_3():
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
