"""
837. New 21 Game · Medium · https://leetcode.com/problems/new-21-game/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().new21Game(10, 1, 10), 1.0), "close(Solution().new21Game(10, 1, 10), 1.0)")


def test_example_2():
    check_true(close(Solution().new21Game(6, 1, 10), 0.6), "close(Solution().new21Game(6, 1, 10), 0.6)")


def test_example_3():
    check_true(close(Solution().new21Game(21, 17, 10), 0.73278), "close(Solution().new21Game(21, 17, 10), 0.73278)")
