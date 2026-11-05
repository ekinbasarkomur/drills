"""
714. Best Time to Buy and Sell Stock with Transaction Fee · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2), 8, "Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)")


def test_example_2():
    check(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3), 6, "Solution().maxProfit([1, 3, 7, 5, 10, 3], 3)")
