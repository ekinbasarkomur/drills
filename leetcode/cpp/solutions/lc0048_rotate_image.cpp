// 48. Rotate Image · Medium · https://leetcode.com/problems/rotate-image/
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
    void rotate(vector<vector<int>>& matrix) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> matrix = vector<vector<int>>{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution().rotate(matrix);
    CHECK_EQ(matrix, (vector<vector<int>>{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}));
}

TEST(example_2) {
    vector<vector<int>> matrix = vector<vector<int>>{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
    Solution().rotate(matrix);
    CHECK_EQ(matrix, (vector<vector<int>>{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}));
}
