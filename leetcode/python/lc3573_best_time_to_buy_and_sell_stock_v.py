"""
3573. Best Time to Buy and Sell Stock V · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maximumProfit([1, 7, 9, 8, 2], 2), 14, "Solution().maximumProfit([1, 7, 9, 8, 2], 2)")


def test_example_2():
    check(Solution().maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3), 36, "Solution().maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3)")
