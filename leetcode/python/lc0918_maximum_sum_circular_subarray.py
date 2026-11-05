"""
918. Maximum Sum Circular Subarray · Medium · https://leetcode.com/problems/maximum-sum-circular-subarray/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxSubarraySumCircular([1, -2, 3, -2]), 3, "Solution().maxSubarraySumCircular([1, -2, 3, -2])")


def test_example_2():
    check(Solution().maxSubarraySumCircular([5, -3, 5]), 10, "Solution().maxSubarraySumCircular([5, -3, 5])")


def test_example_3():
    check(Solution().maxSubarraySumCircular([-3, -2, -3]), -2, "Solution().maxSubarraySumCircular([-3, -2, -3])")
