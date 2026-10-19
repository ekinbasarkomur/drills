// 3573. Best Time to Buy and Sell Stock V · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
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
    long long maximumProfit(vector<int>& prices, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> prices = vector<int>{1, 7, 9, 8, 2};
    int k = 2;
    CHECK_EQ(Solution().maximumProfit(prices, k), 14);
}

TEST(example_2) {
    vector<int> prices = vector<int>{12, 16, 19, 19, 8, 1, 19, 13, 9};
    int k = 3;
    CHECK_EQ(Solution().maximumProfit(prices, k), 36);
}
