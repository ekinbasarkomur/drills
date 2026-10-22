"""
153. Find Minimum in Rotated Sorted Array · Medium · https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Plan: Aşama 0 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findMin(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1


def test_example_2():
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0


def test_example_3():
    assert Solution().findMin([11, 13, 15, 17]) == 11
