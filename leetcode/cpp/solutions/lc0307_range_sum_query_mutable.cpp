// 307. Range Sum Query - Mutable · Medium · https://leetcode.com/problems/range-sum-query-mutable/
// Plan: Aşama 5 · Segment Tree ve Fenwick
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
    
    void update(int index, int val) {
        TODO();
    }
    
    int sumRange(int left, int right) {
        TODO();
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 3, 5};
    NumArray *obj = new NumArray(nums);
    CHECK_EQ(obj->sumRange(0, 2), 9);
    obj->update(1, 2);
    CHECK_EQ(obj->sumRange(0, 2), 8);
}
