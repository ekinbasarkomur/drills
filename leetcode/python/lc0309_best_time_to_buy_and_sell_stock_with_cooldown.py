"""
309. Best Time to Buy and Sell Stock with Cooldown · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3


def test_example_2():
    assert Solution().maxProfit([1]) == 0
