// 85. Maximal Rectangle · Hard · https://leetcode.com/problems/maximal-rectangle/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<char>> matrix = vector<vector<char>>{{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}};
    CHECK_EQ(Solution().maximalRectangle(matrix), 6);
}

TEST(example_2) {
    vector<vector<char>> matrix = vector<vector<char>>{{'0'}};
    CHECK_EQ(Solution().maximalRectangle(matrix), 0);
}

TEST(example_3) {
    vector<vector<char>> matrix = vector<vector<char>>{{'1'}};
    CHECK_EQ(Solution().maximalRectangle(matrix), 1);
}
