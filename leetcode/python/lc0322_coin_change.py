"""
322. Coin Change · Medium · https://leetcode.com/problems/coin-change/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().coinChange([1, 2, 5], 11), 3, "Solution().coinChange([1, 2, 5], 11)")


def test_example_2():
    check(Solution().coinChange([2], 3), -1, "Solution().coinChange([2], 3)")


def test_example_3():
    check(Solution().coinChange([1], 0), 0, "Solution().coinChange([1], 0)")
