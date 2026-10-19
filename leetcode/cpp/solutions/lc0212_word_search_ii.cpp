// 212. Word Search II · Hard · https://leetcode.com/problems/word-search-ii/
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
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<char>> board = vector<vector<char>>{{'o', 'a', 'a', 'n'}, {'e', 't', 'a', 'e'}, {'i', 'h', 'k', 'r'}, {'i', 'f', 'l', 'v'}};
    vector<string> words = vector<string>{"oath", "pea", "eat", "rain"};
    CHECK_EQ(Solution().findWords(board, words), (vector<string>{"eat", "oath"}));
}

TEST(example_2) {
    vector<vector<char>> board = vector<vector<char>>{{'a', 'b'}, {'c', 'd'}};
    vector<string> words = vector<string>{"abcb"};
    CHECK_EQ(Solution().findWords(board, words), (vector<string>{}));
}
