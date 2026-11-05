"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit · Medium · https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().longestSubarray([8, 2, 4, 7], 4), 2, "Solution().longestSubarray([8, 2, 4, 7], 4)")


def test_example_2():
    check(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5), 4, "Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5)")


def test_example_3():
    check(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0), 3, "Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0)")
