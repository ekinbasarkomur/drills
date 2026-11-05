"""
1186. Maximum Subarray Sum with One Deletion · Medium · https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maximumSum([1, -2, 0, 3]), 4, "Solution().maximumSum([1, -2, 0, 3])")


def test_example_2():
    check(Solution().maximumSum([1, -2, -2, 3]), 3, "Solution().maximumSum([1, -2, -2, 3])")


def test_example_3():
    check(Solution().maximumSum([-1, -1, -1, -1]), -1, "Solution().maximumSum([-1, -1, -1, -1])")
