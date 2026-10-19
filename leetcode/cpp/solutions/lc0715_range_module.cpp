// 715. Range Module · Hard · https://leetcode.com/problems/range-module/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class RangeModule {
public:
    RangeModule() {
        TODO();
    }
    
    void addRange(int left, int right) {
        TODO();
    }
    
    bool queryRange(int left, int right) {
        TODO();
    }
    
    void removeRange(int left, int right) {
        TODO();
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    RangeModule *obj = new RangeModule();
    obj->addRange(10, 20);
    obj->removeRange(14, 16);
    CHECK_EQ(obj->queryRange(10, 14), true);
    CHECK_EQ(obj->queryRange(13, 15), false);
    CHECK_EQ(obj->queryRange(16, 17), true);
}
