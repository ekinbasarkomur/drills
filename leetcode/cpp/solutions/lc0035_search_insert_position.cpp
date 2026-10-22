// 35. Search Insert Position · Easy · https://leetcode.com/problems/search-insert-position/
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
    int searchInsert(vector<int>& nums, int target) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 3, 5, 6};
    int target = 5;
    CHECK_EQ(Solution().searchInsert(nums, target), 2);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 3, 5, 6};
    int target = 2;
    CHECK_EQ(Solution().searchInsert(nums, target), 1);
}

TEST(example_3) {
    vector<int> nums = vector<int>{1, 3, 5, 6};
    int target = 7;
    CHECK_EQ(Solution().searchInsert(nums, target), 4);
}
