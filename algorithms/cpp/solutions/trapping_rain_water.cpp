// 42. Trapping Rain Water      https://leetcode.com/problems/trapping-rain-water/
//
// Problem: each height[i] is a bar of width 1. How much water sits in the dips
//          once the rain stops?
// Key idea: water above bar i is min(tallest bar to its left,
//           tallest bar to its right) - height[i], never negative.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int trap(vector<int> &height) {
        (void)height;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests
// trap takes a non-const reference, so it cannot be handed a temporary.

using vi = vector<int>;

static int trap(vi height) { return Solution().trap(height); }

TEST(example_1) { CHECK(trap({0, 2, 0, 3, 1, 0, 1, 3, 2, 1}) == 9); }

TEST(the_leetcode_example) {
    CHECK(trap({0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}) == 6);
}

TEST(tall_wall_on_the_right) { CHECK(trap({4, 2, 0, 3, 2, 5}) == 9); }

// Nothing can be trapped in any of these.

TEST(single_bar) { CHECK(trap({5}) == 0); }

TEST(two_bars) { CHECK(trap({3, 4}) == 0); }

TEST(strictly_ascending) { CHECK(trap({1, 2, 3, 4, 5}) == 0); }

TEST(strictly_descending) { CHECK(trap({5, 4, 3, 2, 1}) == 0); }

TEST(flat_ground) { CHECK(trap({3, 3, 3, 3}) == 0); }

TEST(all_zeros) { CHECK(trap({0, 0, 0}) == 0); }

TEST(a_peak_traps_nothing) { CHECK(trap({0, 100000, 0}) == 0); }

// The real cases.

TEST(one_simple_basin) { CHECK(trap({5, 0, 5}) == 5); }

TEST(two_basins_in_a_row) { CHECK(trap({2, 0, 2, 0, 2}) == 4); }

TEST(several_narrow_dips) { CHECK(trap({1, 0, 1, 0, 1, 0, 1}) == 3); }

TEST(value_range_extremes) {
    // one basin 100_000 deep -- the running total must not overflow an int
    CHECK(trap({100000, 0, 100000}) == 100000);
}

TEST(largest_allowed_input) {
    // 20_000 bars alternating 100_000 and 0: 9_999 basins of 100_000 each.
    // An O(n^2) solution will hang here rather than fail.
    vi height;
    for (int i = 0; i < 10000; ++i) {
        height.push_back(100000);
        height.push_back(0);
    }
    CHECK(trap(height) == 999900000);
}
