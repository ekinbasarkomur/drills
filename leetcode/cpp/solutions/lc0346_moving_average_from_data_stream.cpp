// 346. Moving Average from Data Stream · Easy · https://leetcode.com/problems/moving-average-from-data-stream/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MovingAverage {
public:
    MovingAverage(int size) {
        TODO();
    }
    
    double next(int val) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    int size = 3;
    MovingAverage *obj = new MovingAverage(size);
    obj->next(1);
    obj->next(10);
    obj->next(3);
    obj->next(5);
}
