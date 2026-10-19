// 8. String to Integer (atoi) · Medium · https://leetcode.com/problems/string-to-integer-atoi/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int myAtoi(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("42");
    CHECK_EQ(Solution().myAtoi(s), 42);
}

TEST(example_2) {
    string s = string("   -042");
    CHECK_EQ(Solution().myAtoi(s), -42);
}

TEST(example_3) {
    string s = string("1337c0d3");
    CHECK_EQ(Solution().myAtoi(s), 1337);
}

TEST(example_4) {
    string s = string("0-1");
    CHECK_EQ(Solution().myAtoi(s), 0);
}

TEST(example_5) {
    string s = string("words and 987");
    CHECK_EQ(Solution().myAtoi(s), 0);
}
