"""
907. Sum of Subarray Minimums · Medium · https://leetcode.com/problems/sum-of-subarray-minimums/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().sumSubarrayMins([3, 1, 2, 4]) == 17


def test_example_2():
    assert Solution().sumSubarrayMins([50]) == 444
