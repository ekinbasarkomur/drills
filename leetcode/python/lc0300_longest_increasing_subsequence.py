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
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example_2():
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_example_3():
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
