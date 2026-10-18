// <NUMBER>. <TITLE>            https://leetcode.com/problems/<slug>/
//
// Problem: one or two lines, in your own words.
// Approach: the trick in one line. Time O(?), space O(?).

#include <vector>

#include "test.hpp"

std::vector<int> solve(const std::vector<int> &nums, int target) {
    (void)nums;
    (void)target;
    return {};
}

// ---------------------------------------------------------------- tests

TEST(example_1) {
    CHECK_EQ(solve({2, 7, 11, 15}, 9), (std::vector<int>{0, 1}));
}

TEST(example_2) {
    CHECK_EQ(solve({3, 2, 4}, 6), (std::vector<int>{1, 2}));
}
