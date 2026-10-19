// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Plan: Aşama 0 · Stack
//
// Problem: every bracket closed by its own kind, in the right order,
//          and nothing left open at the end.
// Note: The most recently opened bracket is the first that has to close --
//       that is exactly what a stack gives you.
// Approach: push every opener; on a closer, the top of the stack must be the
//           matching opener, which is then popped. Valid if nothing is left.
// Time O(n), space O(n)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
                continue;
            }

            if (st.empty()) {
                return false;
            }
            if (c == ')' && st.top() != '(') {
                return false;
            }
            if (c == '}' && st.top() != '{') {
                return false;
            }
            if (c == ']' && st.top() != '[') {
                return false;
            }
            st.pop();
        }

        return st.empty();
    }
};
// ---------------------------------------------------------------- tests

static bool isValid(string s) { return Solution().isValid(s); }

TEST(example_1) { CHECK(isValid("[]")); }

TEST(example_2) { CHECK(isValid("([{}])")); }

TEST(example_3) {
    // right counts, wrong order
    CHECK(!isValid("[(])"));
}

TEST(empty_string) {
    // nothing left open
    CHECK(isValid(""));
}

TEST(one_opening_bracket) { CHECK(!isValid("(")); }

TEST(one_closing_bracket) { CHECK(!isValid(")")); }

TEST(all_three_kinds_side_by_side) { CHECK(isValid("()[]{}")); }

TEST(mismatched_pair) { CHECK(!isValid("(]")); }

TEST(a_wrong_closer_is_not_skipped) {
    // the ']' must fail immediately; ignoring it lets ')' close the '('
    CHECK(!isValid("(])"));
}

TEST(only_openers) { CHECK(!isValid("((((")); }

TEST(only_closers) { CHECK(!isValid("))))")); }

TEST(deeply_nested) { CHECK(isValid("{[()]}")); }

TEST(one_opener_left_over) { CHECK(!isValid("(()")); }

TEST(one_closer_too_many) { CHECK(!isValid("())")); }

TEST(largest_allowed_input) {
    // 1000 brackets: 500 openers then 500 closers, the constraint's ceiling.
    string s = string(500, '(') + string(500, ')');
    CHECK(isValid(s));
}
