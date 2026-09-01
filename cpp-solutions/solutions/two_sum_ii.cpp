// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
//
// Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
//          values that add up to target, smaller index first. Exactly one
//          answer exists and you may not use the same element twice.
// Follow-up: constant extra space -- so no hash map this time.
// Approach:
// Time O(?), space O(?)

#include <numeric>
#include <vector>

#include "test.hpp"

std::vector<int> twoSum(const std::vector<int> &numbers, int target) {
    (void)numbers;
    (void)target;
    return {};  // TODO
}

// ---------------------------------------------------------------- tests

using vi = std::vector<int>;

TEST(example_1) { CHECK_EQ(twoSum({1, 2, 3, 4}, 3), (vi{1, 2})); }

TEST(example_2) { CHECK_EQ(twoSum({2, 7, 11, 15}, 9), (vi{1, 2})); }

TEST(example_3) { CHECK_EQ(twoSum({2, 3, 4}, 6), (vi{1, 3})); }

TEST(shortest_possible_input) { CHECK_EQ(twoSum({-1, 0}, -1), (vi{1, 2})); }

TEST(the_two_ends_are_the_answer) {
    CHECK_EQ(twoSum({1, 2, 3, 4, 5, 6, 7}, 8), (vi{1, 7}));
}

TEST(the_answer_sits_in_the_middle) {
    CHECK_EQ(twoSum({1, 2, 3, 4, 5, 6, 7}, 7), (vi{3, 4}));
}

TEST(equal_values_next_to_each_other) { CHECK_EQ(twoSum({3, 3}, 6), (vi{1, 2})); }

TEST(repeated_values_around_the_answer) {
    CHECK_EQ(twoSum({1, 1, 1, 5, 9}, 6), (vi{3, 4}));
}

TEST(all_negative) { CHECK_EQ(twoSum({-9, -7, -3, -1}, -10), (vi{2, 3})); }

TEST(crossing_zero) { CHECK_EQ(twoSum({-5, -2, 0, 3, 8}, 3), (vi{2, 5})); }

TEST(target_is_zero) { CHECK_EQ(twoSum({-4, -1, 0, 1, 4}, 0), (vi{2, 4})); }

TEST(value_range_extremes) { CHECK_EQ(twoSum({-1000, 0, 1000}, 0), (vi{1, 3})); }

TEST(largest_allowed_input) {
    // 1000 elements: the answer is the very first and the very last, so a scan
    // that starts from both ends finds it immediately while a nested loop
    // grinds through the whole array.
    const int n = 1000;
    vi numbers(n);
    std::iota(numbers.begin(), numbers.end(), 0);
    CHECK_EQ(twoSum(numbers, n - 1), (vi{1, n}));
}
