// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/
//
// Problem: output[i] is the product of every element of nums except nums[i].
// Approach:
// Time O(?), space O(?)

#include <vector>

#include "test.hpp"

std::vector<int> productExceptSelf(const std::vector<int> &nums) {
    (void)nums;
    return {};  // TODO
}

// ---------------------------------------------------------------- tests

using vi = std::vector<int>;

TEST(example_1) { CHECK_EQ(productExceptSelf({1, 2, 4, 6}), (vi{48, 24, 12, 8})); }

TEST(example_2) {
    CHECK_EQ(productExceptSelf({-1, 0, 1, 2, 3}), (vi{0, -6, 0, 0, 0}));
}

TEST(shortest_possible_input) { CHECK_EQ(productExceptSelf({2, 3}), (vi{3, 2})); }

TEST(all_ones) { CHECK_EQ(productExceptSelf({1, 1, 1, 1}), (vi{1, 1, 1, 1})); }

// The two cases a naive "divide by nums[i]" solution gets wrong.

TEST(one_zero_in_the_middle) {
    CHECK_EQ(productExceptSelf({1, 2, 0, 4}), (vi{0, 0, 8, 0}));
}

TEST(two_zeros_make_everything_zero) {
    CHECK_EQ(productExceptSelf({0, 4, 0, 5}), (vi{0, 0, 0, 0}));
}

TEST(zero_at_each_end) {
    CHECK_EQ(productExceptSelf({0, 3, 5}), (vi{15, 0, 0}));
    CHECK_EQ(productExceptSelf({3, 5, 0}), (vi{0, 0, 15}));
}

TEST(negative_numbers_flip_the_sign) {
    CHECK_EQ(productExceptSelf({-1, -2, -3}), (vi{6, 3, 2}));
    CHECK_EQ(productExceptSelf({-2, 3, -4}), (vi{-12, 8, -6}));
}

TEST(value_range_extremes) { CHECK_EQ(productExceptSelf({-30, 30}), (vi{30, -30})); }

TEST(large_input_stays_linear) {
    // 100_000 elements: anything O(n^2) will hang here rather than fail.
    const int n = 100000;
    vi nums(n, 1);
    nums[7] = 0;

    vi out = productExceptSelf(nums);

    CHECK(out.size() == static_cast<size_t>(n));
    if (out.size() != static_cast<size_t>(n)) return;
    CHECK(out[7] == 1);
    bool rest_all_zero = true;
    for (int i = 0; i < n; ++i)
        if (i != 7 && out[i] != 0) rest_all_zero = false;
    CHECK(rest_all_zero);
}
