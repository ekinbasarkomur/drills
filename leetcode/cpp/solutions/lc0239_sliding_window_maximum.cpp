// 239. Sliding Window Maximum · Hard · https://leetcode.com/problems/sliding-window-maximum/
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
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    CHECK_EQ(Solution().maxSlidingWindow(nums, k), (vector<int>{3, 3, 5, 5, 6, 7}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{1};
    int k = 1;
    CHECK_EQ(Solution().maxSlidingWindow(nums, k), (vector<int>{1}));
}
