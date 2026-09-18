// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/
//
// Problem: length of the longest run of consecutive integers that can be formed
//          from nums. Order in the array does not matter.
// Approach:
// Time O(?), space O(?)   -- the problem demands O(n)

#include <numeric>
#include <random>
#include <vector>

#include "test.hpp"

int longestConsecutive(const std::vector<int> &nums) {
    (void)nums;
    return 0; // TODO
}

// ---------------------------------------------------------------- tests

using vi = std::vector<int>;

TEST(example_1) { CHECK(longestConsecutive({2, 20, 4, 10, 3, 4, 5}) == 4); }

TEST(example_2) { CHECK(longestConsecutive({0, 3, 2, 5, 4, 6, 1, 1}) == 7); }

TEST(empty_array) { CHECK(longestConsecutive({}) == 0); }

TEST(single_element) { CHECK(longestConsecutive({7}) == 1); }

TEST(all_duplicates_of_one_value) {
    CHECK(longestConsecutive({5, 5, 5, 5}) == 1);
}

TEST(no_two_numbers_are_consecutive) {
    CHECK(longestConsecutive({10, 30, 50, 70}) == 1);
}

TEST(already_sorted) { CHECK(longestConsecutive({1, 2, 3, 4, 5}) == 5); }

TEST(given_in_descending_order) {
    CHECK(longestConsecutive({5, 4, 3, 2, 1}) == 5);
}

TEST(two_runs_and_the_longer_one_comes_second) {
    CHECK(longestConsecutive({1, 2, 3, 100, 101, 102, 103}) == 4);
}

TEST(negative_numbers) { CHECK(longestConsecutive({-3, -2, -1, 0, 1}) == 5); }

TEST(run_straddling_zero_with_a_gap) {
    CHECK(longestConsecutive({-5, -4, 100, -3, 7, -1, 0}) == 3);
}

TEST(value_range_extremes) {
    // watch out for overflow: num + 1 on INT_MAX would wrap
    CHECK(longestConsecutive({1000000000, 999999999, -1000000000}) == 2);
}

TEST(duplicates_inside_a_run_do_not_inflate_it) {
    CHECK(longestConsecutive({1, 2, 2, 3, 3, 3, 4}) == 4);
}

TEST(large_input_stays_linear) {
    // 100_000 elements in one unbroken run, handed over shuffled.
    // An O(n^2) solution will hang here rather than fail.
    const int n = 100000;
    vi nums(n);
    std::iota(nums.begin(), nums.end(), 0);
    std::shuffle(nums.begin(), nums.end(), std::mt19937(0));

    CHECK(longestConsecutive(nums) == n);
}
