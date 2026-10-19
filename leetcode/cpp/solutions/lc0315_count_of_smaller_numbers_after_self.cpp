// 315. Count of Smaller Numbers After Self · Hard · https://leetcode.com/problems/count-of-smaller-numbers-after-self/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{5, 2, 6, 1};
    CHECK_EQ(Solution().countSmaller(nums), (vector<int>{2, 1, 1, 0}));
}

TEST(example_2) {
    vector<int> nums = vector<int>{-1};
    CHECK_EQ(Solution().countSmaller(nums), (vector<int>{0}));
}

TEST(example_3) {
    vector<int> nums = vector<int>{-1, -1};
    CHECK_EQ(Solution().countSmaller(nums), (vector<int>{0, 0}));
}
