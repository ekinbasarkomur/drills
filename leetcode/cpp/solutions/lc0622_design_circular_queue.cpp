// 622. Design Circular Queue · Medium · https://leetcode.com/problems/design-circular-queue/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyCircularQueue {
public:
    MyCircularQueue(int k) {
        TODO();
    }
    
    bool enQueue(int value) {
        TODO();
    }
    
    bool deQueue() {
        TODO();
    }
    
    int Front() {
        TODO();
    }
    
    int Rear() {
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
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int k = 3;
    MyCircularQueue *obj = new MyCircularQueue(k);
    CHECK_EQ(obj->enQueue(1), true);
    CHECK_EQ(obj->enQueue(2), true);
    CHECK_EQ(obj->enQueue(3), true);
    CHECK_EQ(obj->enQueue(4), false);
    CHECK_EQ(obj->Rear(), 3);
    CHECK_EQ(obj->isFull(), true);
    CHECK_EQ(obj->deQueue(), true);
    CHECK_EQ(obj->enQueue(4), true);
    CHECK_EQ(obj->Rear(), 4);
}
