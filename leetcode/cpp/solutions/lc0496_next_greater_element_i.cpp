// 496. Next Greater Element I · Easy · https://leetcode.com/problems/next-greater-element-i/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums1 = vector<int>{4, 1, 2};
    vector<int> nums2 = vector<int>{1, 3, 4, 2};
    CHECK_EQ(Solution().nextGreaterElement(nums1, nums2), (vector<int>{-1, 3, -1}));
}

TEST(example_2) {
    vector<int> nums1 = vector<int>{2, 4};
    vector<int> nums2 = vector<int>{1, 2, 3, 4};
    CHECK_EQ(Solution().nextGreaterElement(nums1, nums2), (vector<int>{3, -1}));
}
