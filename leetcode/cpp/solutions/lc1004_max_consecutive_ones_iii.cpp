// 1004. Max Consecutive Ones III · Medium · https://leetcode.com/problems/max-consecutive-ones-iii/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
    int k = 2;
    CHECK_EQ(Solution().longestOnes(nums, k), 6);
}

TEST(example_2) {
    vector<int> nums = vector<int>{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
    int k = 3;
    CHECK_EQ(Solution().longestOnes(nums, k), 10);
}
