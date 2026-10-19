// 718. Maximum Length of Repeated Subarray · Medium · https://leetcode.com/problems/maximum-length-of-repeated-subarray/
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
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums1 = vector<int>{1, 2, 3, 2, 1};
    vector<int> nums2 = vector<int>{3, 2, 1, 4, 7};
    CHECK_EQ(Solution().findLength(nums1, nums2), 3);
}

TEST(example_2) {
    vector<int> nums1 = vector<int>{0, 0, 0, 0, 0};
    vector<int> nums2 = vector<int>{0, 0, 0, 0, 0};
    CHECK_EQ(Solution().findLength(nums1, nums2), 5);
}
