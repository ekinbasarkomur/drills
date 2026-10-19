// 224. Basic Calculator · Hard · https://leetcode.com/problems/basic-calculator/
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
    int calculate(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("1 + 1");
    CHECK_EQ(Solution().calculate(s), 2);
}

TEST(example_2) {
    string s = string(" 2-1 + 2 ");
    CHECK_EQ(Solution().calculate(s), 3);
}

TEST(example_3) {
    string s = string("(1+(4+5+2)-3)+(6+8)");
    CHECK_EQ(Solution().calculate(s), 23);
}
