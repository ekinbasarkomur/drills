// 152. Maximum Product Subarray · Medium · https://leetcode.com/problems/maximum-product-subarray/
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
    int maxProduct(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{2, 3, -2, 4};
    CHECK_EQ(Solution().maxProduct(nums), 6);
}

TEST(example_2) {
    vector<int> nums = vector<int>{-2, 0, -1};
    CHECK_EQ(Solution().maxProduct(nums), 0);
}
