// 641. Design Circular Deque · Medium · https://leetcode.com/problems/design-circular-deque/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyCircularDeque {
public:
    MyCircularDeque(int k) {
        TODO();
    }
    
    bool insertFront(int value) {
        TODO();
    }
    
    bool insertLast(int value) {
        TODO();
    }
    
    bool deleteFront() {
        TODO();
    }
    
    bool deleteLast() {
        TODO();
    }
    
    int getFront() {
        TODO();
    }
    
    int getRear() {
        TODO();
    }
    
    bool isEmpty() {
        TODO();
    }
    
    bool isFull() {
        TODO();
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int k = 3;
    MyCircularDeque *obj = new MyCircularDeque(k);
    CHECK_EQ(obj->insertLast(1), true);
    CHECK_EQ(obj->insertLast(2), true);
    CHECK_EQ(obj->insertFront(3), true);
    CHECK_EQ(obj->insertFront(4), false);
    CHECK_EQ(obj->getRear(), 2);
    CHECK_EQ(obj->isFull(), true);
    CHECK_EQ(obj->deleteLast(), true);
    CHECK_EQ(obj->insertFront(4), true);
    CHECK_EQ(obj->getFront(), 4);
}
