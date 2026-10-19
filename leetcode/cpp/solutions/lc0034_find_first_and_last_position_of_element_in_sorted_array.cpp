// 34. Find First and Last Position of Element in Sorted Array · Medium · https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
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
    vector<int> searchRange(vector<int>& nums, int target) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{5, 7, 7, 8, 8, 10};
    int target = 8;
    CHECK_EQ(Solution().searchRange(nums, target), (vector<int>{3, 4}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{5, 7, 7, 8, 8, 10};
    int target = 6;
    CHECK_EQ(Solution().searchRange(nums, target), (vector<int>{-1, -1}));
}

TEST(example_3) {
    vector<int> nums = vector<int>{};
    int target = 0;
    CHECK_EQ(Solution().searchRange(nums, target), (vector<int>{-1, -1}));
}
