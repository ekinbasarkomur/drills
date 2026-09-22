// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//
// Problem: buy on one day and sell on a LATER day. Return the best profit,
//          or 0 if every later price is lower.
// Note: You never need to look ahead: the best sale on day i is against the
//       cheapest price seen so far, so one pass is enough.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {

        int lowest_price = prices[0];
        int max_profit = 0;

        for (int price : prices) {
            if (price < lowest_price) {
                lowest_price = price;
                continue;
            }

            int profit = price - lowest_price;

            if (profit > max_profit) {
                max_profit = profit;
            }
        }

        return max_profit;
    }
};

// ---------------------------------------------------------------- tests
// maxProfit takes a non-const reference, so it cannot be handed a temporary.

static int maxProfit(vector<int> prices) {
    return Solution().maxProfit(prices);
}

TEST(example_1) { CHECK((maxProfit({10, 1, 5, 6, 7, 1}) == 6)); }

TEST(example_2) {
    // prices only fall, so no transaction is made
    CHECK((maxProfit({10, 8, 7, 5, 2}) == 0));
}

TEST(single_day) {
    // nothing to sell into
    CHECK((maxProfit({1}) == 0));
}

TEST(two_days_rising) { CHECK((maxProfit({1, 2}) == 1)); }

TEST(two_days_falling) { CHECK((maxProfit({2, 1}) == 0)); }

TEST(flat_prices) { CHECK((maxProfit({5, 5, 5}) == 0)); }

TEST(all_zeros) { CHECK((maxProfit({0, 0, 0}) == 0)); }

TEST(buy_low_sell_high_at_the_ends) { CHECK((maxProfit({0, 100}) == 100)); }

TEST(the_low_comes_after_the_high) {
    // cannot sell before buying
    CHECK((maxProfit({100, 0}) == 0));
}

TEST(best_pair_is_not_the_global_min_and_max) {
    // the lowest price (0) comes after the highest (6)
    CHECK((maxProfit({3, 2, 6, 5, 0, 3}) == 4));
}

TEST(largest_allowed_input) {
    // 100 days, the constraint's ceiling: the price slides from 50 down to 0,
    // then climbs to 98. Buy at the bottom, sell on the last day.
    vector<int> prices;
    for (int i = 0; i < 50; ++i)
        prices.push_back(50 - i);
    for (int i = 0; i < 50; ++i)
        prices.push_back(i * 2);
    CHECK((maxProfit(prices) == 98));
}
