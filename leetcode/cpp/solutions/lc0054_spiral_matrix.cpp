// 54. Spiral Matrix · Medium · https://leetcode.com/problems/spiral-matrix/
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
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> matrix = vector<vector<int>>{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    CHECK_EQ(Solution().spiralOrder(matrix), (vector<int>{1, 2, 3, 6, 9, 8, 7, 4, 5}));
}

TEST(example_2) {
    vector<vector<int>> matrix = vector<vector<int>>{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    CHECK_EQ(Solution().spiralOrder(matrix), (vector<int>{1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7}));
}
