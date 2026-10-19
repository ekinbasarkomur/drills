// 480. Sliding Window Median · Hard · https://leetcode.com/problems/sliding-window-median/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    CHECK(near(Solution().medianSlidingWindow(nums, k), vector<double>{1.0, -1.0, -1.0, 3.0, 5.0, 6.0}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 2, 3, 4, 2, 3, 1, 4, 2};
    int k = 3;
    CHECK(near(Solution().medianSlidingWindow(nums, k), vector<double>{2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0}));
}
