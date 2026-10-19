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
    assert Solution().coinChange([1, 2, 5], 11) == 3


def test_example_2():
    assert Solution().coinChange([2], 3) == -1


def test_example_3():
    assert Solution().coinChange([1], 0) == 0
