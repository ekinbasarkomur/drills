// 153. Find Minimum in Rotated Sorted Array · Medium · https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Plan: Aşama 0 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int findMin(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{3, 4, 5, 1, 2};
    CHECK_EQ(Solution().findMin(nums), 1);
}

TEST(example_2) {
    vector<int> nums = vector<int>{4, 5, 6, 7, 0, 1, 2};
    CHECK_EQ(Solution().findMin(nums), 0);
}

TEST(example_3) {
    vector<int> nums = vector<int>{11, 13, 15, 17};
    CHECK_EQ(Solution().findMin(nums), 11);
}
