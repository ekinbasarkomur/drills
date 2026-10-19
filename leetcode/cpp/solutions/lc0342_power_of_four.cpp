// 342. Power of Four · Easy · https://leetcode.com/problems/power-of-four/
// Plan: Aşama 1 · Bit Manipulation
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool isPowerOfFour(int n) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 16;
    CHECK_EQ(Solution().isPowerOfFour(n), true);
}

TEST(example_2) {
    int n = 5;
    CHECK_EQ(Solution().isPowerOfFour(n), false);
}

TEST(example_3) {
    int n = 1;
    CHECK_EQ(Solution().isPowerOfFour(n), true);
}
