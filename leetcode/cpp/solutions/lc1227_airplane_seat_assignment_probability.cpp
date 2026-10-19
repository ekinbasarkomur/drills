// 1227. Airplane Seat Assignment Probability · Medium · https://leetcode.com/problems/airplane-seat-assignment-probability/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 1;
    CHECK(near(Solution().nthPersonGetsNthSeat(n), 1.0));
}

TEST(example_2) {
    int n = 2;
    CHECK(near(Solution().nthPersonGetsNthSeat(n), 0.5));
}
