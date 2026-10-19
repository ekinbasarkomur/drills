"""
480. Sliding Window Median · Hard · https://leetcode.com/problems/sliding-window-median/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert close(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [1.0, -1.0, -1.0, 3.0, 5.0, 6.0])


def test_example_2():
    assert close(Solution().medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3), [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0])
