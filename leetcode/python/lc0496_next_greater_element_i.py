"""
496. Next Greater Element I · Easy · https://leetcode.com/problems/next-greater-element-i/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1], "Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])")


def test_example_2():
    check(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1], "Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])")
