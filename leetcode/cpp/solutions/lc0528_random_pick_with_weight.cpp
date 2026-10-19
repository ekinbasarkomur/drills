// 528. Random Pick with Weight · Medium · https://leetcode.com/problems/random-pick-with-weight/
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
    Solution(vector<int>& w) {
        TODO();
    }
    
    int pickIndex() {
        TODO();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> w = vector<int>{1};
    Solution *obj = new Solution(w);
    obj->pickIndex();
}

TEST(example_2) {
    vector<int> w = vector<int>{1, 3};
    Solution *obj = new Solution(w);
    obj->pickIndex();
    obj->pickIndex();
    obj->pickIndex();
    obj->pickIndex();
    obj->pickIndex();
}
