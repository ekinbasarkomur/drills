// 410. Split Array Largest Sum · Hard · https://leetcode.com/problems/split-array-largest-sum/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{7, 2, 5, 10, 8};
    int k = 2;
    CHECK_EQ(Solution().splitArray(nums, k), 18);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 2, 3, 4, 5};
    int k = 2;
    CHECK_EQ(Solution().splitArray(nums, k), 9);
}
