"""
1425. Constrained Subsequence Sum · Hard · https://leetcode.com/problems/constrained-subsequence-sum/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2), 37, "Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2)")


def test_example_2():
    check(Solution().constrainedSubsetSum([-1, -2, -3], 1), -1, "Solution().constrainedSubsetSum([-1, -2, -3], 1)")


def test_example_3():
    check(Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2), 23, "Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2)")
