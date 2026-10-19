// 300. Longest Increasing Subsequence · Medium · https://leetcode.com/problems/longest-increasing-subsequence/
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
    int lengthOfLIS(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{10, 9, 2, 5, 3, 7, 101, 18};
    CHECK_EQ(Solution().lengthOfLIS(nums), 4);
}

TEST(example_2) {
    vector<int> nums = vector<int>{0, 1, 0, 3, 2, 3};
    CHECK_EQ(Solution().lengthOfLIS(nums), 4);
}

TEST(example_3) {
    vector<int> nums = vector<int>{7, 7, 7, 7, 7, 7, 7};
    CHECK_EQ(Solution().lengthOfLIS(nums), 1);
}
