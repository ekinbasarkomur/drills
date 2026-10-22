// 724. Find Pivot Index · Easy · https://leetcode.com/problems/find-pivot-index/
// Plan: Aşama 0 · Sliding Window ve Prefix Sum
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 7, 3, 6, 5, 6};
    CHECK_EQ(Solution().pivotIndex(nums), 3);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 2, 3};
    CHECK_EQ(Solution().pivotIndex(nums), -1);
}

TEST(example_3) {
    vector<int> nums = vector<int>{2, 1, -1};
    CHECK_EQ(Solution().pivotIndex(nums), 0);
}
