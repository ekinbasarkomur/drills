// 1186. Maximum Subarray Sum with One Deletion · Medium · https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
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
    int maximumSum(vector<int>& arr) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> arr = vector<int>{1, -2, 0, 3};
    CHECK_EQ(Solution().maximumSum(arr), 4);
}

TEST(example_2) {
    vector<int> arr = vector<int>{1, -2, -2, 3};
    CHECK_EQ(Solution().maximumSum(arr), 3);
}

TEST(example_3) {
    vector<int> arr = vector<int>{-1, -1, -1, -1};
    CHECK_EQ(Solution().maximumSum(arr), -1);
}
