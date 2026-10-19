// 78. Subsets · Medium · https://leetcode.com/problems/subsets/
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
    vector<vector<int>> subsets(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 2, 3};
    CHECK_EQ(deep_sort(Solution().subsets(nums)), deep_sort(vector<vector<int>>{{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{0};
    CHECK_EQ(deep_sort(Solution().subsets(nums)), deep_sort(vector<vector<int>>{{}, {0}}));
}
