// 15. 3Sum                     https://leetcode.com/problems/3sum/
//
// Problem: every triplet of distinct indices summing to zero, with no duplicate
//          triplets in the output. Order does not matter.
// Note: the hard part is not finding the triplets, it is not emitting the same
//       one twice -- [-1,0,1] can be built from several index combinations.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        (void)nums;
        return {};  // TODO
    }
};

// ---------------------------------------------------------------- tests
// "You may return the output and the triplets in any order" -> sort both
// levels before comparing.

using vi  = vector<int>;
using vvi = vector<vector<int>>;

static vvi normalized(vvi triplets) {
    for (auto &t : triplets) sort(t.begin(), t.end());
    sort(triplets.begin(), triplets.end());
    return triplets;
}

static vvi got(vi nums) { return normalized(Solution().threeSum(nums)); }

TEST(example_1) {
    CHECK_EQ(got({-1, 0, 1, 2, -1, -4}), normalized({{-1, -1, 2}, {-1, 0, 1}}));
}

TEST(example_2) { CHECK_EQ(got({0, 1, 1}), vvi{}); }

TEST(example_3) { CHECK_EQ(got({0, 0, 0}), normalized({{0, 0, 0}})); }

TEST(all_positive_cannot_reach_zero) { CHECK_EQ(got({1, 2, 3}), vvi{}); }

TEST(all_negative_cannot_reach_zero) { CHECK_EQ(got({-1, -2, -3}), vvi{}); }

// Duplicate handling: the same triplet must appear exactly once.

TEST(four_zeros_yield_one_triplet) {
    CHECK_EQ(got({0, 0, 0, 0}), normalized({{0, 0, 0}}));
}

TEST(a_repeated_value_inside_a_triplet) {
    CHECK_EQ(got({-2, 0, 1, 1, 2}), normalized({{-2, 0, 2}, {-2, 1, 1}}));
}

TEST(many_repeats_many_triplets) {
    CHECK_EQ(got({-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6}),
             normalized({{-4, -2, 6},
                         {-4, 0, 4},
                         {-4, 1, 3},
                         {-4, 2, 2},
                         {-2, -2, 4},
                         {-2, 0, 2}}));
}

TEST(same_values_different_order_in_the_input) {
    CHECK_EQ(got({1, -1, 0, 2, -2, 0}), normalized({{-2, 0, 2}, {-1, 0, 1}}));
}

TEST(value_range_extremes) {
    CHECK_EQ(got({100000, -100000, 0}), normalized({{-100000, 0, 100000}}));
    CHECK_EQ(got({-100000, 50000, 50000}),
             normalized({{-100000, 50000, 50000}}));
}

TEST(largest_allowed_input) {
    // 3000 elements, all 1 except three that form the only triplet.
    // An O(n^3) solution will hang here rather than fail.
    vi nums(2997, 1);
    nums.push_back(-5);
    nums.push_back(2);
    nums.push_back(3);
    CHECK_EQ(got(nums), normalized({{-5, 2, 3}}));
}
