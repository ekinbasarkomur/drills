// 1048. Longest String Chain · Medium · https://leetcode.com/problems/longest-string-chain/
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
    int longestStrChain(vector<string>& words) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<string> words = vector<string>{"a", "b", "ba", "bca", "bda", "bdca"};
    CHECK_EQ(Solution().longestStrChain(words), 4);
}

TEST(example_2) {
    vector<string> words = vector<string>{"xbc", "pcxbcf", "xb", "cxbc", "pcxbc"};
    CHECK_EQ(Solution().longestStrChain(words), 5);
}

TEST(example_3) {
    vector<string> words = vector<string>{"abcd", "dbqca"};
    CHECK_EQ(Solution().longestStrChain(words), 1);
}
