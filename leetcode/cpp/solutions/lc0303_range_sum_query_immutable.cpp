// 303. Range Sum Query - Immutable · Easy · https://leetcode.com/problems/range-sum-query-immutable/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class NumArray {
public:
    NumArray(vector<int>& nums) {
        TODO();
    }
    
    int sumRange(int left, int right) {
        TODO();
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{-2, 0, 3, -5, 2, -1};
    NumArray *obj = new NumArray(nums);
    CHECK_EQ(obj->sumRange(0, 2), 1);
    CHECK_EQ(obj->sumRange(2, 5), -1);
    CHECK_EQ(obj->sumRange(0, 5), -3);
}
