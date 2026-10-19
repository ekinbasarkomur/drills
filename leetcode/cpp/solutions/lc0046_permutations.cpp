// 46. Permutations · Medium · https://leetcode.com/problems/permutations/
// Plan: Aşama 4 · Backtracking
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 2, 3};
    CHECK_EQ(sort_outer(Solution().permute(nums)), sort_outer(vector<vector<int>>{{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{0, 1};
    CHECK_EQ(sort_outer(Solution().permute(nums)), sort_outer(vector<vector<int>>{{0, 1}, {1, 0}}));
}

TEST(example_3) {
    vector<int> nums = vector<int>{1};
    CHECK_EQ(sort_outer(Solution().permute(nums)), sort_outer(vector<vector<int>>{{1}}));
}
