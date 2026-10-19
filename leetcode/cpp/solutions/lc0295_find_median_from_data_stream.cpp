// 295. Find Median from Data Stream · Hard · https://leetcode.com/problems/find-median-from-data-stream/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MedianFinder {
public:
    MedianFinder() {
        TODO();
    }
    
    void addNum(int num) {
        TODO();
    }
    
    double findMedian() {
        TODO();
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MedianFinder *obj = new MedianFinder();
    obj->addNum(1);
    obj->addNum(2);
    CHECK(near(obj->findMedian(), 1.5));
    obj->addNum(3);
    CHECK(near(obj->findMedian(), 2.0));
}
