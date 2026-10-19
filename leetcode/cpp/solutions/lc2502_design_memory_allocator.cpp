// 2502. Design Memory Allocator · Medium · https://leetcode.com/problems/design-memory-allocator/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Allocator {
public:
    Allocator(int n) {
        TODO();
    }
    
    int allocate(int size, int mID) {
        TODO();
    }
    
    int freeMemory(int mID) {
        TODO();
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 10;
    Allocator *obj = new Allocator(n);
    CHECK_EQ(obj->allocate(1, 1), 0);
    CHECK_EQ(obj->allocate(1, 2), 1);
    CHECK_EQ(obj->allocate(1, 3), 2);
    CHECK_EQ(obj->freeMemory(2), 1);
    CHECK_EQ(obj->allocate(3, 4), 3);
    CHECK_EQ(obj->allocate(1, 1), 1);
    CHECK_EQ(obj->allocate(1, 1), 6);
    CHECK_EQ(obj->freeMemory(1), 3);
    CHECK_EQ(obj->allocate(10, 2), -1);
    CHECK_EQ(obj->freeMemory(7), 0);
}
