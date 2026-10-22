// 994. Rotting Oranges · Medium · https://leetcode.com/problems/rotting-oranges/
// Plan: Aşama 0 · Graphs
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> grid = vector<vector<int>>{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}};
    CHECK_EQ(Solution().orangesRotting(grid), 4);
}

TEST(example_2) {
    vector<vector<int>> grid = vector<vector<int>>{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}};
    CHECK_EQ(Solution().orangesRotting(grid), -1);
}

TEST(example_3) {
    vector<vector<int>> grid = vector<vector<int>>{{0, 2}};
    CHECK_EQ(Solution().orangesRotting(grid), 0);
}
