// 732. My Calendar III · Hard · https://leetcode.com/problems/my-calendar-iii/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyCalendarThree {
public:
    MyCalendarThree() {
        TODO();
    }
    
    int book(int startTime, int endTime) {
        TODO();
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyCalendarThree *obj = new MyCalendarThree();
    CHECK_EQ(obj->book(10, 20), 1);
    CHECK_EQ(obj->book(50, 60), 1);
    CHECK_EQ(obj->book(10, 40), 2);
    CHECK_EQ(obj->book(5, 15), 3);
    CHECK_EQ(obj->book(5, 10), 3);
    CHECK_EQ(obj->book(25, 55), 3);
}
