// 45. Jump Game II · Medium · https://leetcode.com/problems/jump-game-ii/
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
    int jump(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{2, 3, 1, 1, 4};
    CHECK_EQ(Solution().jump(nums), 2);
}

TEST(example_2) {
    vector<int> nums = vector<int>{2, 3, 0, 1, 4};
    CHECK_EQ(Solution().jump(nums), 2);
}
