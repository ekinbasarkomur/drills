"""
34. Find First and Last Position of Element in Sorted Array · Medium · https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4], "Solution().searchRange([5, 7, 7, 8, 8, 10], 8)")


def test_example_2():
    check(Solution().searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1], "Solution().searchRange([5, 7, 7, 8, 8, 10], 6)")


def test_example_3():
    check(Solution().searchRange([], 0), [-1, -1], "Solution().searchRange([], 0)")
