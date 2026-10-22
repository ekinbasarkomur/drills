// 55. Jump Game · Medium · https://leetcode.com/problems/jump-game/
// Plan: Aşama 0 · Greedy
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool canJump(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{2, 3, 1, 1, 4};
    CHECK_EQ(Solution().canJump(nums), true);
}

TEST(example_2) {
    vector<int> nums = vector<int>{3, 2, 1, 0, 4};
    CHECK_EQ(Solution().canJump(nums), false);
}
