// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
//
// Problem: every bracket closed by its own kind, in the right order,
//          and nothing left open at the end.
// Note: The most recently opened bracket is the first that has to close --
//       that is exactly what a stack gives you.
// Approach:
// Time O(?), space O(?)

#include <string>

#include "test.hpp"

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        (void)s;
        return false;  // TODO
    }
};

// ---------------------------------------------------------------- tests


static bool isValid(string s) {
    return Solution().isValid(s);
}

TEST(example_1) {
    CHECK(isValid("[]"));
}

TEST(example_2) {
    CHECK(isValid("([{}])"));
}

TEST(example_3) {
    // right counts, wrong order
    CHECK(!isValid("[(])"));
}

TEST(empty_string) {
    // nothing left open
    CHECK(isValid(""));
}

TEST(one_opening_bracket) {
    CHECK(!isValid("("));
}

TEST(one_closing_bracket) {
    CHECK(!isValid(")"));
}

TEST(all_three_kinds_side_by_side) {
    CHECK(isValid("()[]{}"));
}

TEST(mismatched_pair) {
    CHECK(!isValid("(]"));
}

TEST(only_openers) {
    CHECK(!isValid("(((("));
}

TEST(only_closers) {
    CHECK(!isValid("))))"));
}

TEST(deeply_nested) {
    CHECK(isValid("{[()]}"));
}

TEST(one_opener_left_over) {
    CHECK(!isValid("(()"));
}

TEST(one_closer_too_many) {
    CHECK(!isValid("())"));
}

TEST(largest_allowed_input) {
    // 1000 brackets: 500 openers then 500 closers, the constraint's ceiling.
    string s = string(500, '(') + string(500, ')');
    CHECK(isValid(s));
}
