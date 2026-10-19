// 4. Median of Two Sorted Arrays · Hard · https://leetcode.com/problems/median-of-two-sorted-arrays/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums1 = vector<int>{1, 3};
    vector<int> nums2 = vector<int>{2};
    CHECK(near(Solution().findMedianSortedArrays(nums1, nums2), 2.0));
}

TEST(example_2) {
    vector<int> nums1 = vector<int>{1, 2};
    vector<int> nums2 = vector<int>{3, 4};
    CHECK(near(Solution().findMedianSortedArrays(nums1, nums2), 2.5));
}
