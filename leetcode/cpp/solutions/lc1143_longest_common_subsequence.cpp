// 1143. Longest Common Subsequence · Medium · https://leetcode.com/problems/longest-common-subsequence/
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
    int longestCommonSubsequence(string text1, string text2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string text1 = string("abcde");
    string text2 = string("ace");
    CHECK_EQ(Solution().longestCommonSubsequence(text1, text2), 3);
}

TEST(example_2) {
    string text1 = string("abc");
    string text2 = string("abc");
    CHECK_EQ(Solution().longestCommonSubsequence(text1, text2), 3);
}

TEST(example_3) {
    string text1 = string("abc");
    string text2 = string("def");
    CHECK_EQ(Solution().longestCommonSubsequence(text1, text2), 0);
}
