// 198. House Robber · Medium · https://leetcode.com/problems/house-robber/
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
    int rob(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 2, 3, 1};
    CHECK_EQ(Solution().rob(nums), 4);
}

TEST(example_2) {
    vector<int> nums = vector<int>{2, 7, 9, 3, 1};
    CHECK_EQ(Solution().rob(nums), 12);
}
