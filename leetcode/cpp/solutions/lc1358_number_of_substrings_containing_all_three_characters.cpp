// 1358. Number of Substrings Containing All Three Characters · Medium · https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int numberOfSubstrings(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("abcabc");
    CHECK_EQ(Solution().numberOfSubstrings(s), 10);
}

TEST(example_2) {
    string s = string("aaacb");
    CHECK_EQ(Solution().numberOfSubstrings(s), 3);
}

TEST(example_3) {
    string s = string("abc");
    CHECK_EQ(Solution().numberOfSubstrings(s), 1);
}
