// 188. Best Time to Buy and Sell Stock IV · Hard · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
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
    int maxProfit(int k, vector<int>& prices) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int k = 2;
    vector<int> prices = vector<int>{2, 4, 1};
    CHECK_EQ(Solution().maxProfit(k, prices), 2);
}

TEST(example_2) {
    int k = 2;
    vector<int> prices = vector<int>{3, 2, 6, 5, 0, 3};
    CHECK_EQ(Solution().maxProfit(k, prices), 7);
}
