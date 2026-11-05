"""
198. House Robber · Medium · https://leetcode.com/problems/house-robber/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def rob(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().rob([1, 2, 3, 1]), 4, "Solution().rob([1, 2, 3, 1])")


def test_example_2():
    check(Solution().rob([2, 7, 9, 3, 1]), 12, "Solution().rob([2, 7, 9, 3, 1])")
