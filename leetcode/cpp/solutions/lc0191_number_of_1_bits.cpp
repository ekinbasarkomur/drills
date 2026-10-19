// 191. Number of 1 Bits · Easy · https://leetcode.com/problems/number-of-1-bits/
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
    int hammingWeight(int n) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 11;
    CHECK_EQ(Solution().hammingWeight(n), 3);
}

TEST(example_2) {
    int n = 128;
    CHECK_EQ(Solution().hammingWeight(n), 1);
}

TEST(example_3) {
    int n = 2147483645;
    CHECK_EQ(Solution().hammingWeight(n), 30);
}
