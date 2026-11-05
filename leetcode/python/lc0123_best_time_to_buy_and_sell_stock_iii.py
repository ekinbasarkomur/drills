"""
123. Best Time to Buy and Sell Stock III · Hard · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
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
    check(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6, "Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])")


def test_example_2():
    check(Solution().maxProfit([1, 2, 3, 4, 5]), 4, "Solution().maxProfit([1, 2, 3, 4, 5])")


def test_example_3():
    check(Solution().maxProfit([7, 6, 4, 3, 1]), 0, "Solution().maxProfit([7, 6, 4, 3, 1])")
