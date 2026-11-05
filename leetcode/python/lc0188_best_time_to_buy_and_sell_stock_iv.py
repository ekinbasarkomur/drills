"""
188. Best Time to Buy and Sell Stock IV · Hard · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxProfit(2, [2, 4, 1]), 2, "Solution().maxProfit(2, [2, 4, 1])")


def test_example_2():
    check(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]), 7, "Solution().maxProfit(2, [3, 2, 6, 5, 0, 3])")
