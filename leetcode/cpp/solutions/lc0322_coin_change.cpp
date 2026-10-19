// 322. Coin Change · Medium · https://leetcode.com/problems/coin-change/
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
    int coinChange(vector<int>& coins, int amount) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> coins = vector<int>{1, 2, 5};
    int amount = 11;
    CHECK_EQ(Solution().coinChange(coins, amount), 3);
}

TEST(example_2) {
    vector<int> coins = vector<int>{2};
    int amount = 3;
    CHECK_EQ(Solution().coinChange(coins, amount), -1);
}

TEST(example_3) {
    vector<int> coins = vector<int>{1};
    int amount = 0;
    CHECK_EQ(Solution().coinChange(coins, amount), 0);
}
