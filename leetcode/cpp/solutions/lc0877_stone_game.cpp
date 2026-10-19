// 877. Stone Game · Medium · https://leetcode.com/problems/stone-game/
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
    bool stoneGame(vector<int>& piles) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> piles = vector<int>{5, 3, 4, 5};
    CHECK_EQ(Solution().stoneGame(piles), true);
}

TEST(example_2) {
    vector<int> piles = vector<int>{3, 7, 2, 3};
    CHECK_EQ(Solution().stoneGame(piles), true);
}
