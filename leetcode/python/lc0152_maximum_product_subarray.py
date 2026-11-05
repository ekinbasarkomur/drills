"""
152. Maximum Product Subarray · Medium · https://leetcode.com/problems/maximum-product-subarray/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxProduct([2, 3, -2, 4]), 6, "Solution().maxProduct([2, 3, -2, 4])")


def test_example_2():
    check(Solution().maxProduct([-2, 0, -1]), 0, "Solution().maxProduct([-2, 0, -1])")
