// 729. My Calendar I · Medium · https://leetcode.com/problems/my-calendar-i/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyCalendar {
public:
    MyCalendar() {
        TODO();
    }
    
    bool book(int startTime, int endTime) {
        TODO();
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyCalendar *obj = new MyCalendar();
    CHECK_EQ(obj->book(10, 20), true);
    CHECK_EQ(obj->book(15, 25), false);
    CHECK_EQ(obj->book(20, 30), true);
}
