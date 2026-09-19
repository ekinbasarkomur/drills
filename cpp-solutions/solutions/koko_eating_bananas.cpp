// 875. Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/
//
// Problem: find the smallest eating rate k such that every pile is
//          finished within h hours. A pile takes ceil(pile / k) hours, and
//          leftover time in an hour is wasted -- no starting the next pile.
// Note: You are not searching the array, you are searching the ANSWER: every
//       rate from 1 to max(piles) either works or does not, and once one
//       works every larger one does too.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int> &piles, int h) {
        (void)piles;
        (void)h;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests
// minEatingSpeed takes a non-const reference, so it cannot be handed a temporary.

static int minEatingSpeed(vector<int> piles, int h) {
    return Solution().minEatingSpeed(piles, h);
}

TEST(example_1) { CHECK((minEatingSpeed({1, 4, 3, 2}, 9) == 2)); }

TEST(example_2) {
    // h equals the pile count, so each pile must go in one hour
    CHECK((minEatingSpeed({25, 10, 23, 4}, 4) == 25));
}

TEST(single_pile_single_hour) { CHECK((minEatingSpeed({1}, 1) == 1)); }

TEST(time_to_spare) {
    // k never drops below 1
    CHECK((minEatingSpeed({1}, 10) == 1));
}

TEST(the_classic_leetcode_case) {
    CHECK((minEatingSpeed({3, 6, 7, 11}, 8) == 4));
}

TEST(tight_deadline) { CHECK((minEatingSpeed({30, 11, 23, 4, 20}, 5) == 30)); }

TEST(one_hour_more_is_enough_to_slow_down) {
    CHECK((minEatingSpeed({30, 11, 23, 4, 20}, 6) == 23));
}

TEST(uniform_piles) { CHECK((minEatingSpeed({1, 1, 1, 1}, 4) == 1)); }

TEST(value_range_extremes) {
    // one pile of a billion in one hour -- the rate must match it exactly
    CHECK((minEatingSpeed({1000000000}, 1) == 1000000000));
}

TEST(largest_allowed_input) {
    // 10_000 piles of 10_000 bananas each and exactly 10_000 hours: one pile
    // per hour, so the rate has to be the pile size. Scanning k from 1
    // upwards would take 10_000 passes; binary search takes 14.
    vector<int> piles(10000, 10000);
    CHECK((minEatingSpeed(piles, 10000) == 10000));
}
