// 1425. Constrained Subsequence Sum · Hard · https://leetcode.com/problems/constrained-subsequence-sum/
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
    int constrainedSubsetSum(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{10, 2, -10, 5, 20};
    int k = 2;
    CHECK_EQ(Solution().constrainedSubsetSum(nums, k), 37);
}

TEST(example_2) {
    vector<int> nums = vector<int>{-1, -2, -3};
    int k = 1;
    CHECK_EQ(Solution().constrainedSubsetSum(nums, k), -1);
}

TEST(example_3) {
    vector<int> nums = vector<int>{10, -2, -10, -5, 20};
    int k = 2;
    CHECK_EQ(Solution().constrainedSubsetSum(nums, k), 23);
}
