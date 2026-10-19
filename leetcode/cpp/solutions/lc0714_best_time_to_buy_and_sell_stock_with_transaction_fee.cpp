// 714. Best Time to Buy and Sell Stock with Transaction Fee · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> prices = vector<int>{1, 3, 2, 8, 4, 9};
    int fee = 2;
    CHECK_EQ(Solution().maxProfit(prices, fee), 8);
}

TEST(example_2) {
    vector<int> prices = vector<int>{1, 3, 7, 5, 10, 3};
    int fee = 3;
    CHECK_EQ(Solution().maxProfit(prices, fee), 6);
}
