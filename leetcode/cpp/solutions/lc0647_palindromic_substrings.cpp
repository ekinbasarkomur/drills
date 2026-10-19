// 647. Palindromic Substrings · Medium · https://leetcode.com/problems/palindromic-substrings/
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
    int countSubstrings(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("abc");
    CHECK_EQ(Solution().countSubstrings(s), 3);
}

TEST(example_2) {
    string s = string("aaa");
    CHECK_EQ(Solution().countSubstrings(s), 6);
}
