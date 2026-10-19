// 32. Longest Valid Parentheses · Hard · https://leetcode.com/problems/longest-valid-parentheses/
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
    int longestValidParentheses(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("(()");
    CHECK_EQ(Solution().longestValidParentheses(s), 2);
}

TEST(example_2) {
    string s = string(")()())");
    CHECK_EQ(Solution().longestValidParentheses(s), 4);
}

TEST(example_3) {
    string s = string("");
    CHECK_EQ(Solution().longestValidParentheses(s), 0);
}
