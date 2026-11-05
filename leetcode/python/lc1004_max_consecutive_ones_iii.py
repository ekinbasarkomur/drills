"""
1004. Max Consecutive Ones III · Medium · https://leetcode.com/problems/max-consecutive-ones-iii/
Plan: Aşama 1 · Prefix Sum ve Sliding Window

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6, "Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)")


def test_example_2():
    check(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10, "Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)")
