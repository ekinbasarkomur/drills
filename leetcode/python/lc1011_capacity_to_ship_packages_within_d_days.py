"""
1011. Capacity To Ship Packages Within D Days · Medium · https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15


def test_example_2():
    assert Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6


def test_example_3():
    assert Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3
