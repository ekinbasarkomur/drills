// 347. Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/
//
// Problem: return the k most frequent values in nums. The answer is unique and
//          may be returned in any order.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <vector>

#include "test.hpp"

std::vector<int> topKFrequent(const std::vector<int> &nums, int k) {
    (void)nums;
    (void)k;
    return {};  // TODO
}

// ---------------------------------------------------------------- tests
// "You may return the output in any order" -> sort before comparing.

using vi = std::vector<int>;

static vi sorted(vi v) {
    std::sort(v.begin(), v.end());
    return v;
}

static vi topK(const vi &nums, int k) { return sorted(topKFrequent(nums, k)); }

TEST(example_1) { CHECK_EQ(topK({1, 2, 2, 3, 3, 3}, 2), (vi{2, 3})); }

TEST(example_2) { CHECK_EQ(topK({7, 7}, 1), (vi{7})); }

TEST(single_element) { CHECK_EQ(topK({1}, 1), (vi{1})); }

TEST(k_equals_number_of_distinct_values) {
    CHECK_EQ(topK({1, 1, 2, 2, 3}, 3), (vi{1, 2, 3}));
}

TEST(negative_values) {
    CHECK_EQ(topK({-1, -1, -1, -2, -2, 5}, 2), (vi{-2, -1}));
}

TEST(extremes_of_the_value_range) {
    CHECK_EQ(topK({1000, 1000, -1000, -1000, -1000, 7}, 1), (vi{-1000}));
}

TEST(least_frequent_values_are_excluded) {
    CHECK_EQ(topK({4, 4, 4, 4, 9, 9, 9, 1, 1, 6}, 2), (vi{4, 9}));
}

TEST(every_value_appears_once_except_one) {
    CHECK_EQ(topK({5, 6, 7, 8, 8}, 1), (vi{8}));
}
