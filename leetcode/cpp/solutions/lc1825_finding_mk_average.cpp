// 1825. Finding MK Average · Hard · https://leetcode.com/problems/finding-mk-average/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MKAverage {
public:
    MKAverage(int m, int k) {
        TODO();
    }
    
    void addElement(int num) {
        TODO();
    }
    
    int calculateMKAverage() {
        TODO();
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int m = 3;
    int k = 1;
    MKAverage *obj = new MKAverage(m, k);
    obj->addElement(3);
    obj->addElement(1);
    CHECK_EQ(obj->calculateMKAverage(), -1);
    obj->addElement(10);
    CHECK_EQ(obj->calculateMKAverage(), 3);
    obj->addElement(5);
    obj->addElement(5);
    obj->addElement(5);
    CHECK_EQ(obj->calculateMKAverage(), 5);
}
