"""
862. Shortest Subarray with Sum at Least K · Hard · https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().shortestSubarray([1], 1), 1, "Solution().shortestSubarray([1], 1)")


def test_example_2():
    check(Solution().shortestSubarray([1, 2], 4), -1, "Solution().shortestSubarray([1, 2], 4)")


def test_example_3():
    check(Solution().shortestSubarray([2, -1, 2], 3), 3, "Solution().shortestSubarray([2, -1, 2], 3)")
