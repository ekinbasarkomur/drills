"""
560. Subarray Sum Equals K · Medium · https://leetcode.com/problems/subarray-sum-equals-k/
Plan: Aşama 1 · Prefix Sum ve Sliding Window

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().subarraySum([1, 1, 1], 2), 2, "Solution().subarraySum([1, 1, 1], 2)")


def test_example_2():
    check(Solution().subarraySum([1, 2, 3], 3), 2, "Solution().subarraySum([1, 2, 3], 3)")
