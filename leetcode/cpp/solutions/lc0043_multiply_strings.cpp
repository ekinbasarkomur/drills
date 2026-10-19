// 43. Multiply Strings · Medium · https://leetcode.com/problems/multiply-strings/
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
    string multiply(string num1, string num2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string num1 = string("2");
    string num2 = string("3");
    CHECK_EQ(Solution().multiply(num1, num2), (string("6")));
}

TEST(example_2) {
    string num1 = string("123");
    string num2 = string("456");
    CHECK_EQ(Solution().multiply(num1, num2), (string("56088")));
}
