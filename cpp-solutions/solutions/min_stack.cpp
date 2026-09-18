// 155. Min Stack
// https://leetcode.com/problems/min-stack/
//
// Problem: a stack that also answers getMin() -- all four operations in O(1).
// Note: getMin in O(1) is the whole problem. Scanning for the minimum is O(n),
//       and a single "current min" variable cannot survive a pop that removes
//       it, because you no longer know what the minimum was before.
// Approach:
// Time O(?) per operation, space O(?)

#include <vector>

#include "test.hpp"

using namespace std;

class MinStack {
public:
    MinStack() {
        // TODO
    }

    void push(int val) {
        (void)val;  // TODO
    }

    void pop() {
        // TODO
    }

    int top() {
        return 0;  // TODO
    }

    int getMin() {
        return 0;  // TODO
    }
};

// ---------------------------------------------------------------- tests

TEST(example_1) {
    MinStack s;
    s.push(1);
    s.push(2);
    s.push(0);
    CHECK((s.getMin() == 0));
    s.pop();
    CHECK((s.top() == 2));
    CHECK((s.getMin() == 1));
}

TEST(single_element) {
    MinStack s;
    s.push(5);
    CHECK((s.top() == 5));
    CHECK((s.getMin() == 5));
}

TEST(min_is_the_first_pushed) {
    MinStack s;
    s.push(1);
    s.push(2);
    s.push(3);
    CHECK((s.getMin() == 1));
    CHECK((s.top() == 3));
}

TEST(min_is_the_last_pushed) {
    MinStack s;
    s.push(3);
    s.push(2);
    s.push(1);
    CHECK((s.getMin() == 1));
}

TEST(popping_the_minimum_restores_the_previous_one) {
    MinStack s;
    s.push(5);
    s.push(1);
    CHECK((s.getMin() == 1));
    s.pop();
    CHECK((s.getMin() == 5));
}

TEST(duplicate_minimums) {
    // popping one copy of the minimum must not lose the other
    MinStack s;
    s.push(2);
    s.push(1);
    s.push(1);
    CHECK((s.getMin() == 1));
    s.pop();
    CHECK((s.getMin() == 1));
    s.pop();
    CHECK((s.getMin() == 2));
}

TEST(negative_values) {
    MinStack s;
    s.push(0);
    s.push(-3);
    s.push(2);
    CHECK((s.getMin() == -3));
    s.pop();
    CHECK((s.getMin() == -3));
}

TEST(emptied_and_refilled) {
    MinStack s;
    s.push(1);
    s.pop();
    s.push(9);
    CHECK((s.top() == 9));
    CHECK((s.getMin() == 9));
}

TEST(interleaved_operations) {
    MinStack s;
    s.push(4);
    CHECK((s.getMin() == 4));
    s.push(7);
    CHECK((s.getMin() == 4));
    s.push(2);
    CHECK((s.getMin() == 2));
    s.pop();
    CHECK((s.getMin() == 4));
    s.push(1);
    CHECK((s.getMin() == 1));
    s.pop();
    s.pop();
    CHECK((s.top() == 4));
    CHECK((s.getMin() == 4));
}

TEST(value_range_extremes) {
    MinStack s;
    s.push(2147483647);
    s.push(-2147483648);
    CHECK((s.getMin() == -2147483648));
    s.pop();
    CHECK((s.getMin() == 2147483647));
}

TEST(many_operations_stay_constant_time) {
    // 30_000 pushes then 30_000 pops, the constraint's ceiling.
    // An O(n) getMin will crawl here.
    MinStack s;
    for (int i = 30000; i > 0; --i) s.push(i);
    for (int i = 1; i <= 30000; ++i) {
        CHECK((s.getMin() == i));
        s.pop();
    }
}
