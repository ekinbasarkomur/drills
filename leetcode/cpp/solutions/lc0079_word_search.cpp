// 79. Word Search · Medium · https://leetcode.com/problems/word-search/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<char>> board = vector<vector<char>>{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    string word = string("ABCCED");
    CHECK_EQ(Solution().exist(board, word), true);
}

TEST(example_2) {
    vector<vector<char>> board = vector<vector<char>>{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    string word = string("SEE");
    CHECK_EQ(Solution().exist(board, word), true);
}

TEST(example_3) {
    vector<vector<char>> board = vector<vector<char>>{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    string word = string("ABCB");
    CHECK_EQ(Solution().exist(board, word), false);
}
