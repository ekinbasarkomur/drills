// 3652. Best Time to Buy and Sell Stock using Strategy · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
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
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> prices = vector<int>{4, 2, 8};
    vector<int> strategy = vector<int>{-1, 0, 1};
    int k = 2;
    CHECK_EQ(Solution().maxProfit(prices, strategy, k), 10);
}

TEST(example_2) {
    vector<int> prices = vector<int>{5, 4, 3};
    vector<int> strategy = vector<int>{1, 1, 0};
    int k = 2;
    CHECK_EQ(Solution().maxProfit(prices, strategy, k), 9);
}
