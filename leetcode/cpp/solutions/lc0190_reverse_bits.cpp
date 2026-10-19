// 190. Reverse Bits · Easy · https://leetcode.com/problems/reverse-bits/
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
    int reverseBits(int n) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 43261596;
    CHECK_EQ(Solution().reverseBits(n), 964176192);
}

TEST(example_2) {
    int n = 2147483644;
    CHECK_EQ(Solution().reverseBits(n), 1073741822);
}
