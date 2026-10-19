// 220. Contains Duplicate III · Hard · https://leetcode.com/problems/contains-duplicate-iii/
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
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 2, 3, 1};
    int indexDiff = 3;
    int valueDiff = 0;
    CHECK_EQ(Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff), true);
}

TEST(example_2) {
    vector<int> nums = vector<int>{1, 5, 9, 1, 5, 9};
    int indexDiff = 2;
    int valueDiff = 3;
    CHECK_EQ(Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff), false);
}
