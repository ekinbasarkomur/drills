"""
4. Median of Two Sorted Arrays · Hard · https://leetcode.com/problems/median-of-two-sorted-arrays/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().findMedianSortedArrays([1, 3], [2]), 2.0), "close(Solution().findMedianSortedArrays([1, 3], [2]), 2.0)")


def test_example_2():
    check_true(close(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5), "close(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)")
