// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/
//
// Problem: pick two bars; the container they form holds
//          (distance between them) * (the shorter of the two). Return the most
//          water any pair can hold.
// Note: The taller bar never sets the height -- the shorter one does, so a
//       wide pair of short bars can beat a narrow pair of tall ones.
// Approach:
// Time O(?), space O(?)

#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        (void)height;
        return 0;  // TODO
    }
};

// ---------------------------------------------------------------- tests
// maxArea takes a non-const reference, so it cannot be handed a temporary.


static int maxArea(vector<int> height) {
    return Solution().maxArea(height);
}

TEST(example_1) {
    CHECK((maxArea({1, 7, 2, 5, 4, 7, 3, 6}) == 36));
}

TEST(example_2) {
    CHECK((maxArea({2, 2, 2}) == 4));
}

TEST(shortest_possible_input) {
    CHECK((maxArea({1, 1}) == 1));
}

TEST(two_zero_bars_hold_nothing) {
    CHECK((maxArea({0, 0}) == 0));
}

TEST(the_classic_leetcode_case) {
    CHECK((maxArea({1, 8, 6, 2, 5, 4, 8, 3, 7}) == 49));
}

TEST(wide_beats_tall) {
    // the two 3s are 2 apart; nothing taller sits closer together
    CHECK((maxArea({3, 0, 3}) == 6));
}

TEST(strictly_ascending) {
    CHECK((maxArea({1, 2, 3, 4, 5}) == 6));
}

TEST(strictly_descending) {
    CHECK((maxArea({5, 4, 3, 2, 1}) == 6));
}

TEST(one_zero_bar_kills_the_pair) {
    CHECK((maxArea({0, 10000}) == 0));
}

TEST(value_range_extremes) {
    CHECK((maxArea({10000, 0, 0, 0, 10000}) == 40000));
}

TEST(largest_allowed_input) {
    // 100_000 bars: 1 at both ends, 0 in between. The answer is the pair of
    // ends, worth 99_999. An O(n^2) solution will hang here rather than fail.
    vector<int> height(100000, 0);
    height[0] = 1;
    height[99999] = 1;
    CHECK((maxArea(height) == 99999));
}
