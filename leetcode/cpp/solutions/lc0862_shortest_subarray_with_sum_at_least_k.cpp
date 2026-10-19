// 862. Shortest Subarray with Sum at Least K · Hard · https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
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
    int shortestSubarray(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1};
    int k = 1;
    CHECK_EQ(Solution().shortestSubarray(nums, k), 1);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 2};
    int k = 4;
    CHECK_EQ(Solution().shortestSubarray(nums, k), -1);
}

TEST(example_3) {
    vector<int> nums = vector<int>{2, -1, 2};
    int k = 3;
    CHECK_EQ(Solution().shortestSubarray(nums, k), 3);
}
