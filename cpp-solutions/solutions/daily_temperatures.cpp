// 739. Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/
//
// Problem: result[i] is how many days you wait after day i for a warmer
//          temperature, or 0 if none ever comes.
// Note: Days waiting for a warmer day pile up in the order they arrived, and
//       the newest one is always resolved first -- a stack of pending indices.
// Approach:
// Time O(?), space O(?)

#include <stack>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int> &temperatures) {
        (void)temperatures;
        return {}; // TODO
    }
};

// ---------------------------------------------------------------- tests
// dailyTemperatures takes a non-const reference, so it cannot be handed a temporary.

using vi = vector<int>;

static vector<int> dailyTemperatures(vector<int> temperatures) {
    return Solution().dailyTemperatures(temperatures);
}

TEST(example_1) {
    CHECK_EQ(dailyTemperatures({30, 38, 30, 36, 35, 40, 28}),
             (vi{1, 4, 1, 2, 1, 0, 0}));
}

TEST(example_2) {
    // it only ever gets colder
    CHECK_EQ(dailyTemperatures({22, 21, 20}), (vi{0, 0, 0}));
}

TEST(single_day) { CHECK_EQ(dailyTemperatures({50}), (vi{0})); }

TEST(two_days_warming) { CHECK_EQ(dailyTemperatures({1, 2}), (vi{1, 0})); }

TEST(two_days_cooling) { CHECK_EQ(dailyTemperatures({2, 1}), (vi{0, 0})); }

TEST(flat_week) {
    // equal is not warmer
    CHECK_EQ(dailyTemperatures({5, 5, 5}), (vi{0, 0, 0}));
}

TEST(the_classic_leetcode_case) {
    CHECK_EQ(dailyTemperatures({73, 74, 75, 71, 69, 72, 76, 73}),
             (vi{1, 1, 4, 2, 1, 1, 0, 0}));
}

TEST(one_warm_day_resolves_everything) {
    CHECK_EQ(dailyTemperatures({1, 1, 1, 100}), (vi{3, 2, 1, 0}));
}

TEST(the_warmest_day_is_first) {
    CHECK_EQ(dailyTemperatures({100, 1, 1, 1}), (vi{0, 0, 0, 0}));
}

TEST(strictly_ascending) {
    CHECK_EQ(dailyTemperatures({1, 2, 3, 4, 5}), (vi{1, 1, 1, 1, 0}));
}

TEST(strictly_descending) {
    CHECK_EQ(dailyTemperatures({5, 4, 3, 2, 1}), (vi{0, 0, 0, 0, 0}));
}

TEST(largest_allowed_input) {
    // 100_000 days all at 50 except the last at 100: every earlier day waits
    // for that final one. An O(n^2) solution will hang here rather than fail.
    vi temperatures(100000, 50);
    temperatures[99999] = 100;
    vi expected(100000);
    for (int i = 0; i < 100000; ++i)
        expected[i] = 99999 - i;
    CHECK_EQ(dailyTemperatures(temperatures), expected);
}
