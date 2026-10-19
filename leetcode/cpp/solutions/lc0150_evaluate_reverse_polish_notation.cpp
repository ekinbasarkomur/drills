// 150. Evaluate Reverse Polish Notation · Medium · https://leetcode.com/problems/evaluate-reverse-polish-notation/
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
    int evalRPN(vector<string>& tokens) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<string> tokens = vector<string>{"2", "1", "+", "3", "*"};
    CHECK_EQ(Solution().evalRPN(tokens), 9);
}

TEST(example_2) {
    vector<string> tokens = vector<string>{"4", "13", "5", "/", "+"};
    CHECK_EQ(Solution().evalRPN(tokens), 6);
}

TEST(example_3) {
    vector<string> tokens = vector<string>{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    CHECK_EQ(Solution().evalRPN(tokens), 22);
}
