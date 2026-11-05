"""
239. Sliding Window Maximum · Hard · https://leetcode.com/problems/sliding-window-maximum/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7], "Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)")


def test_example_2():
    check(Solution().maxSlidingWindow([1], 1), [1], "Solution().maxSlidingWindow([1], 1)")
