"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Plan: Aşama 0 · Sliding Window

Problem: buy on one day and sell on a LATER day. Return the best profit,
         or 0 if every later price is lower.
Note: You never need to look ahead: the best sale on day i is against the
      cheapest price seen so far, so one pass is enough.
Approach: one pass, keeping the lowest price seen so far. A lower price becomes the new
          buy day; any other price is a possible sale, and its profit against that lowest price
          updates the best.
Time O(n), space O(1)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for price in prices:

            if price < lowest_price:
                lowest_price = price
                continue

            max_profit = max(max_profit, price - lowest_price)

        return max_profit
# ---------------------------------------------------------------- tests


def max_profit(prices: List[int]) -> int:
    return Solution().maxProfit(prices)


def test_example_1():
    check(max_profit([10, 1, 5, 6, 7, 1]), 6, "max_profit([10, 1, 5, 6, 7, 1])")


def test_example_2():
    # prices only fall, so no transaction is made
    check(max_profit([10, 8, 7, 5, 2]), 0, "max_profit([10, 8, 7, 5, 2])")


def test_single_day():
    # nothing to sell into
    check(max_profit([1]), 0, "max_profit([1])")


def test_two_days_rising():
    check(max_profit([1, 2]), 1, "max_profit([1, 2])")


def test_two_days_falling():
    check(max_profit([2, 1]), 0, "max_profit([2, 1])")


def test_flat_prices():
    check(max_profit([5, 5, 5]), 0, "max_profit([5, 5, 5])")


def test_all_zeros():
    check(max_profit([0, 0, 0]), 0, "max_profit([0, 0, 0])")


def test_buy_low_sell_high_at_the_ends():
    check(max_profit([0, 100]), 100, "max_profit([0, 100])")


def test_the_low_comes_after_the_high():
    # cannot sell before buying
    check(max_profit([100, 0]), 0, "max_profit([100, 0])")


def test_best_pair_is_not_the_global_min_and_max():
    # the lowest price (0) comes after the highest (6)
    check(max_profit([3, 2, 6, 5, 0, 3]), 4, "max_profit([3, 2, 6, 5, 0, 3])")


def test_largest_allowed_input():
    # 100 days, the constraint's ceiling: the price slides from 50 down to 0,
    # then climbs to 98. Buy at the bottom, sell on the last day.
    prices = [50 - i for i in range(50)] + [i * 2 for i in range(50)]
    check(max_profit(prices), 98, "max_profit(prices)")


if __name__ == "__main__":
    print(max_profit([10, 1, 5, 6, 7, 1]))
