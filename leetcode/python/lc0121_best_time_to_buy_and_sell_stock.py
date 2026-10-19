"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Plan: Aşama 0 · Sliding Window

Problem: buy on one day and sell on a LATER day. Return the best profit,
         or 0 if every later price is lower.
Note: You never need to look ahead: the best sale on day i is against the
      cheapest price seen so far, so one pass is enough.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def max_profit(prices: List[int]) -> int:
    return Solution().maxProfit(prices)


def test_example_1():
    assert max_profit([10, 1, 5, 6, 7, 1]) == 6


def test_example_2():
    # prices only fall, so no transaction is made
    assert max_profit([10, 8, 7, 5, 2]) == 0


def test_single_day():
    # nothing to sell into
    assert max_profit([1]) == 0


def test_two_days_rising():
    assert max_profit([1, 2]) == 1


def test_two_days_falling():
    assert max_profit([2, 1]) == 0


def test_flat_prices():
    assert max_profit([5, 5, 5]) == 0


def test_all_zeros():
    assert max_profit([0, 0, 0]) == 0


def test_buy_low_sell_high_at_the_ends():
    assert max_profit([0, 100]) == 100


def test_the_low_comes_after_the_high():
    # cannot sell before buying
    assert max_profit([100, 0]) == 0


def test_best_pair_is_not_the_global_min_and_max():
    # the lowest price (0) comes after the highest (6)
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4


def test_largest_allowed_input():
    # 100 days, the constraint's ceiling: the price slides from 50 down to 0,
    # then climbs to 98. Buy at the bottom, sell on the last day.
    prices = [50 - i for i in range(50)] + [i * 2 for i in range(50)]
    assert max_profit(prices) == 98


if __name__ == "__main__":
    print(max_profit([10, 1, 5, 6, 7, 1]))
