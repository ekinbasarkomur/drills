// 918. Maximum Sum Circular Subarray · Medium · https://leetcode.com/problems/maximum-sum-circular-subarray/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, -2, 3, -2};
    CHECK_EQ(Solution().maxSubarraySumCircular(nums), 3);
}

TEST(example_2) {
    vector<int> nums = vector<int>{5, -3, 5};
    CHECK_EQ(Solution().maxSubarraySumCircular(nums), 10);
}

TEST(example_3) {
    vector<int> nums = vector<int>{-3, -2, -3};
    CHECK_EQ(Solution().maxSubarraySumCircular(nums), -2);
}
