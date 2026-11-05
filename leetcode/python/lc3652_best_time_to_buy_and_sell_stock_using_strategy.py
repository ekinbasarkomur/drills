"""
3652. Best Time to Buy and Sell Stock using Strategy · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maxProfit([4, 2, 8], [-1, 0, 1], 2), 10, "Solution().maxProfit([4, 2, 8], [-1, 0, 1], 2)")


def test_example_2():
    check(Solution().maxProfit([5, 4, 3], [1, 1, 0], 2), 9, "Solution().maxProfit([5, 4, 3], [1, 1, 0], 2)")
