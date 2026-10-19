// 731. My Calendar II · Medium · https://leetcode.com/problems/my-calendar-ii/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyCalendarTwo {
public:
    MyCalendarTwo() {
        TODO();
    }
    
    bool book(int startTime, int endTime) {
        TODO();
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(startTime,endTime);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyCalendarTwo *obj = new MyCalendarTwo();
    CHECK_EQ(obj->book(10, 20), true);
    CHECK_EQ(obj->book(50, 60), true);
    CHECK_EQ(obj->book(10, 40), true);
    CHECK_EQ(obj->book(5, 15), false);
    CHECK_EQ(obj->book(5, 10), true);
    CHECK_EQ(obj->book(25, 55), true);
}
