// 221. Maximal Square · Medium · https://leetcode.com/problems/maximal-square/
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
    int maximalSquare(vector<vector<char>>& matrix) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<char>> matrix = vector<vector<char>>{{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}};
    CHECK_EQ(Solution().maximalSquare(matrix), 4);
}

TEST(example_2) {
    vector<vector<char>> matrix = vector<vector<char>>{{'0', '1'}, {'1', '0'}};
    CHECK_EQ(Solution().maximalSquare(matrix), 1);
}

TEST(example_3) {
    vector<vector<char>> matrix = vector<vector<char>>{{'0'}};
    CHECK_EQ(Solution().maximalSquare(matrix), 0);
}
