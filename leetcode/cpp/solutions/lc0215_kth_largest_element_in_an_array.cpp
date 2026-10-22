// 215. Kth Largest Element in an Array · Medium · https://leetcode.com/problems/kth-largest-element-in-an-array/
// Plan: Aşama 0 · Heap & Priority Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{3, 2, 1, 5, 6, 4};
    int k = 2;
    CHECK_EQ(Solution().findKthLargest(nums, k), 5);
}

TEST(example_2) {
    vector<int> nums = vector<int>{3, 2, 3, 1, 2, 4, 5, 5, 6};
    int k = 4;
    CHECK_EQ(Solution().findKthLargest(nums, k), 4);
}
