// 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit · Medium · https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
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
    int longestSubarray(vector<int>& nums, int limit) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{8, 2, 4, 7};
    int limit = 4;
    CHECK_EQ(Solution().longestSubarray(nums, limit), 2);
}

TEST(example_2) {
    vector<int> nums = vector<int>{10, 1, 2, 4, 7, 2};
    int limit = 5;
    CHECK_EQ(Solution().longestSubarray(nums, limit), 4);
}

TEST(example_3) {
    vector<int> nums = vector<int>{4, 2, 2, 2, 4, 4, 2, 2};
    int limit = 0;
    CHECK_EQ(Solution().longestSubarray(nums, limit), 3);
}
