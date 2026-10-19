// 2484. Count Palindromic Subsequences · Hard · https://leetcode.com/problems/count-palindromic-subsequences/
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
    int countPalindromes(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("103301");
    CHECK_EQ(Solution().countPalindromes(s), 2);
}

TEST(example_2) {
    string s = string("0000000");
    CHECK_EQ(Solution().countPalindromes(s), 21);
}

TEST(example_3) {
    string s = string("9999900000");
    CHECK_EQ(Solution().countPalindromes(s), 2);
}
