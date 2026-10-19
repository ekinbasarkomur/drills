// 17. Letter Combinations of a Phone Number · Medium · https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// Plan: Aşama 4 · Backtracking
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string digits = string("23");
    CHECK_EQ(deep_sort(Solution().letterCombinations(digits)), deep_sort(vector<string>{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}));
}

TEST(example_2) {
    string digits = string("2");
    CHECK_EQ(deep_sort(Solution().letterCombinations(digits)), deep_sort(vector<string>{"a", "b", "c"}));
}
