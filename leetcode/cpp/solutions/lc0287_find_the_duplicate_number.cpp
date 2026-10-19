// 287. Find the Duplicate Number · Medium · https://leetcode.com/problems/find-the-duplicate-number/
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
    int findDuplicate(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 3, 4, 2, 2};
    CHECK_EQ(Solution().findDuplicate(nums), 2);
}

TEST(example_2) {
    vector<int> nums = vector<int>{3, 1, 3, 4, 2};
    CHECK_EQ(Solution().findDuplicate(nums), 3);
}

TEST(example_3) {
    vector<int> nums = vector<int>{3, 3, 3, 3, 3};
    CHECK_EQ(Solution().findDuplicate(nums), 3);
}
