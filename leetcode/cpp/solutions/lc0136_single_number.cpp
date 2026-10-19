// 136. Single Number · Easy · https://leetcode.com/problems/single-number/
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
    int singleNumber(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{2, 2, 1};
    CHECK_EQ(Solution().singleNumber(nums), 1);
}

TEST(example_2) {
    vector<int> nums = vector<int>{4, 1, 2, 1, 2};
    CHECK_EQ(Solution().singleNumber(nums), 4);
}

TEST(example_3) {
    vector<int> nums = vector<int>{1};
    CHECK_EQ(Solution().singleNumber(nums), 1);
}
