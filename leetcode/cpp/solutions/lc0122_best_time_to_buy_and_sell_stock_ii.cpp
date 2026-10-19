// 122. Best Time to Buy and Sell Stock II · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
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
    vector<int> prices = vector<int>{7, 1, 5, 3, 6, 4};
    CHECK_EQ(Solution().maxProfit(prices), 7);
}

TEST(example_2) {
    vector<int> prices = vector<int>{1, 2, 3, 4, 5};
    CHECK_EQ(Solution().maxProfit(prices), 4);
}

TEST(example_3) {
    vector<int> prices = vector<int>{7, 6, 4, 3, 1};
    CHECK_EQ(Solution().maxProfit(prices), 0);
}
