// 1223. Dice Roll Simulation · Hard · https://leetcode.com/problems/dice-roll-simulation/
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
    int dieSimulator(int n, vector<int>& rollMax) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 2;
    vector<int> rollMax = vector<int>{1, 1, 2, 2, 2, 3};
    CHECK_EQ(Solution().dieSimulator(n, rollMax), 34);
}

TEST(example_2) {
    int n = 2;
    vector<int> rollMax = vector<int>{1, 1, 1, 1, 1, 1};
    CHECK_EQ(Solution().dieSimulator(n, rollMax), 30);
}

TEST(example_3) {
    int n = 3;
    vector<int> rollMax = vector<int>{1, 1, 1, 2, 2, 3};
    CHECK_EQ(Solution().dieSimulator(n, rollMax), 181);
}
