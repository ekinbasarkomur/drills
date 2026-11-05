"""
1094. Car Pooling · Medium · https://leetcode.com/problems/car-pooling/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4), False, "Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4)")


def test_example_2():
    check(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5), True, "Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5)")
