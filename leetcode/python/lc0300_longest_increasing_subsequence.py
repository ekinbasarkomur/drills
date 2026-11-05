"""
300. Longest Increasing Subsequence · Medium · https://leetcode.com/problems/longest-increasing-subsequence/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4, "Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])")


def test_example_2():
    check(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]), 4, "Solution().lengthOfLIS([0, 1, 0, 3, 2, 3])")


def test_example_3():
    check(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1, "Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7])")
