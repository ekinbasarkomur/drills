// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Plan: Aşama 0 · Two Pointers
//
// Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
//          values that add up to target, smaller index first. Exactly one
//          answer exists and you may not use the same element twice.
// Follow-up: constant extra space -- so no hash map this time.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
std::vector<int> twoSum(const std::vector<int> &numbers, int target) {

    int left = 0;
    int right = size(numbers) - 1;

    while (left < right) {
        if (target == numbers[left] + numbers[right]) {
            return {left + 1, right + 1};
        }

        else if (target > numbers[left] + numbers[right]) {
            left++;
        } else {
            right--;
        }
    }

    return {0, 0};
}
// ---------------------------------------------------------------- tests

using vi = std::vector<int>;

TEST(example_1) { CHECK_EQ(twoSum({1, 2, 3, 4}, 3), (vi{1, 2})); }

TEST(example_2) { CHECK_EQ(twoSum({2, 7, 11, 15}, 9), (vi{1, 2})); }

TEST(example_3) { CHECK_EQ(twoSum({2, 3, 4}, 6), (vi{1, 3})); }

TEST(shortest_possible_input) { CHECK_EQ(twoSum({-1, 0}, -1), (vi{1, 2})); }

TEST(the_two_ends_are_the_answer) {
    CHECK_EQ(twoSum({1, 5, 6, 7, 20}, 21), (vi{1, 5}));
}

TEST(the_answer_sits_in_the_middle) {
    CHECK_EQ(twoSum({1, 4, 5, 6, 20}, 11), (vi{3, 4}));
}

TEST(equal_values_next_to_each_other) {
    CHECK_EQ(twoSum({3, 3}, 6), (vi{1, 2}));
}

TEST(repeated_values_around_the_answer) {
    CHECK_EQ(twoSum({2, 2, 3, 7}, 10), (vi{3, 4}));
}

TEST(all_negative) { CHECK_EQ(twoSum({-9, -7, -3, -1}, -4), (vi{3, 4})); }

TEST(crossing_zero) { CHECK_EQ(twoSum({-5, -2, 0, 3, 8}, 6), (vi{2, 5})); }

TEST(target_is_zero) { CHECK_EQ(twoSum({-4, -1, 0, 1, 5}, 0), (vi{2, 4})); }

TEST(value_range_extremes) {
    CHECK_EQ(twoSum({-1000, 0, 1000}, 0), (vi{1, 3}));
}

TEST(largest_allowed_input) {
    // 1000 elements: the answer is the very first and the very last, so a scan
    // that starts from both ends finds it immediately while a nested loop
    // grinds through the whole array.
    vi numbers(1000);
    std::iota(numbers.begin(), numbers.end(), 0);
    // 998 + 999 is the only pair reaching 1997, and it sits at the far end
    CHECK_EQ(twoSum(numbers, 1997), (vi{999, 1000}));
}
