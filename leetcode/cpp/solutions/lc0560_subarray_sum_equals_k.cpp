// 560. Subarray Sum Equals K · Medium · https://leetcode.com/problems/subarray-sum-equals-k/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 1, 1};
    int k = 2;
    CHECK_EQ(Solution().subarraySum(nums, k), 2);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 2, 3};
    int k = 3;
    CHECK_EQ(Solution().subarraySum(nums, k), 2);
}
