// 73. Set Matrix Zeroes · Medium · https://leetcode.com/problems/set-matrix-zeroes/
// Plan: Aşama 0 · Matrix
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> matrix = vector<vector<int>>{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    Solution().setZeroes(matrix);
    CHECK_EQ(matrix, (vector<vector<int>>{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}));
}

TEST(example_2) {
    vector<vector<int>> matrix = vector<vector<int>>{{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
    Solution().setZeroes(matrix);
    CHECK_EQ(matrix, (vector<vector<int>>{{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}}));
}
