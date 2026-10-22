// 232. Implement Queue using Stacks · Easy · https://leetcode.com/problems/implement-queue-using-stacks/
// Plan: Aşama 0 · Stack
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyQueue {
public:
    MyQueue() {
        TODO();
    }
    
    void push(int x) {
        TODO();
    }
    
    int pop() {
        TODO();
    }
    
    int peek() {
        TODO();
    }
    
    bool empty() {
        TODO();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyQueue *obj = new MyQueue();
    obj->push(1);
    obj->push(2);
    CHECK_EQ(obj->peek(), 1);
    CHECK_EQ(obj->pop(), 1);
    CHECK_EQ(obj->empty(), false);
}
