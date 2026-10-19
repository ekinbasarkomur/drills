// 39. Combination Sum · Medium · https://leetcode.com/problems/combination-sum/
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
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> candidates = vector<int>{2, 3, 6, 7};
    int target = 7;
    CHECK_EQ(deep_sort(Solution().combinationSum(candidates, target)), deep_sort(vector<vector<int>>{{2, 2, 3}, {7}}));
}

TEST(example_2) {
    vector<int> candidates = vector<int>{2, 3, 5};
    int target = 8;
    CHECK_EQ(deep_sort(Solution().combinationSum(candidates, target)), deep_sort(vector<vector<int>>{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}}));
}

TEST(example_3) {
    vector<int> candidates = vector<int>{2};
    int target = 1;
    CHECK_EQ(deep_sort(Solution().combinationSum(candidates, target)), deep_sort(vector<vector<int>>{}));
}
