// 1. Two Sum                   https://leetcode.com/problems/two-sum/
//
// Problem: return the two indices whose values add up to target, smaller first.
// Approach:
// Time O(?), space O(?)

#include <vector>

#include "test.hpp"

std::vector<int> twoSum(const std::vector<int> &nums, int target) {
    (void)nums;
    (void)target;
    return {};  // TODO
}

// ---------------------------------------------------------------- tests

using vi = std::vector<int>;

TEST(example_1) { CHECK_EQ(twoSum({3, 4, 5, 6}, 7), (vi{0, 1})); }

TEST(example_2) { CHECK_EQ(twoSum({4, 5, 6}, 10), (vi{0, 2})); }

TEST(example_3) { CHECK_EQ(twoSum({5, 5}, 10), (vi{0, 1})); }

TEST(answer_is_the_last_two) { CHECK_EQ(twoSum({1, 9, 3, 4}, 7), (vi{2, 3})); }

TEST(negative_numbers) { CHECK_EQ(twoSum({-3, 4, 7, -1}, -4), (vi{0, 3})); }

TEST(target_is_zero) { CHECK_EQ(twoSum({-8, 2, 8}, 0), (vi{0, 2})); }

TEST(extreme_values) {
    CHECK_EQ(twoSum({10000000, -10000000, 3}, 0), (vi{0, 1}));
}
