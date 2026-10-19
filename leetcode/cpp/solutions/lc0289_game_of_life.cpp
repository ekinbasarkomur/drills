// 289. Game of Life · Medium · https://leetcode.com/problems/game-of-life/
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
    void gameOfLife(vector<vector<int>>& board) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> board = vector<vector<int>>{{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
    Solution().gameOfLife(board);
    CHECK_EQ(board, (vector<vector<int>>{{0, 0, 0}, {1, 0, 1}, {0, 1, 1}, {0, 1, 0}}));
}

TEST(example_2) {
    vector<vector<int>> board = vector<vector<int>>{{1, 1}, {1, 0}};
    Solution().gameOfLife(board);
    CHECK_EQ(board, (vector<vector<int>>{{1, 1}, {1, 1}}));
}
