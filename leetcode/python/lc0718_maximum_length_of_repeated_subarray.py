"""
718. Maximum Length of Repeated Subarray · Medium · https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3, "Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])")


def test_example_2():
    check(Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]), 5, "Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])")
