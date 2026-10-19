// 874. Walking Robot Simulation · Medium · https://leetcode.com/problems/walking-robot-simulation/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> commands = vector<int>{4, -1, 3};
    vector<vector<int>> obstacles = vector<vector<int>>{};
    CHECK_EQ(Solution().robotSim(commands, obstacles), 25);
}

TEST(example_2) {
    vector<int> commands = vector<int>{4, -1, 4, -2, 4};
    vector<vector<int>> obstacles = vector<vector<int>>{{2, 4}};
    CHECK_EQ(Solution().robotSim(commands, obstacles), 65);
}

TEST(example_3) {
    vector<int> commands = vector<int>{-1, 9};
    vector<vector<int>> obstacles = vector<vector<int>>{{5, 0}, {2, 0}};
    CHECK_EQ(Solution().robotSim(commands, obstacles), 36);
}
