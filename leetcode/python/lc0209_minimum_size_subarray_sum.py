"""
209. Minimum Size Subarray Sum · Medium · https://leetcode.com/problems/minimum-size-subarray-sum/
Plan: Aşama 0 · Sliding Window ve Prefix Sum

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2


def test_example_2():
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1


def test_example_3():
    assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
