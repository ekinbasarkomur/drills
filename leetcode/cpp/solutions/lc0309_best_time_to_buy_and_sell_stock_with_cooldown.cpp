// 309. Best Time to Buy and Sell Stock with Cooldown · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
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
    int maxProfit(vector<int>& prices) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> prices = vector<int>{1, 2, 3, 0, 2};
    CHECK_EQ(Solution().maxProfit(prices), 3);
}

TEST(example_2) {
    vector<int> prices = vector<int>{1};
    CHECK_EQ(Solution().maxProfit(prices), 0);
}
