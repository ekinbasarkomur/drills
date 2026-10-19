// 384. Shuffle an Array · Medium · https://leetcode.com/problems/shuffle-an-array/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    Solution(vector<int>& nums) {
        TODO();
    }
    
    vector<int> reset() {
        TODO();
    }
    
    vector<int> shuffle() {
        TODO();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> nums = vector<int>{1, 2, 3};
    Solution *obj = new Solution(nums);
    obj->shuffle();
    CHECK_EQ(obj->reset(), (vector<int>{1, 2, 3}));
    obj->shuffle();
}
