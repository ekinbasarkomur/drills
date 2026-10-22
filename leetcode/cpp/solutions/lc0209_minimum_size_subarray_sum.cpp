// 209. Minimum Size Subarray Sum · Medium · https://leetcode.com/problems/minimum-size-subarray-sum/
// Plan: Aşama 0 · Sliding Window ve Prefix Sum
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int target = 7;
    vector<int> nums = vector<int>{2, 3, 1, 2, 4, 3};
    CHECK_EQ(Solution().minSubArrayLen(target, nums), 2);
}

TEST(example_2) {
    int target = 4;
    vector<int> nums = vector<int>{1, 4, 4};
    CHECK_EQ(Solution().minSubArrayLen(target, nums), 1);
}

TEST(example_3) {
    int target = 11;
    vector<int> nums = vector<int>{1, 1, 1, 1, 1, 1, 1, 1};
    CHECK_EQ(Solution().minSubArrayLen(target, nums), 0);
}
