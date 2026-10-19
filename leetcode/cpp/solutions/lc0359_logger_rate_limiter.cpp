// 359. Logger Rate Limiter · Easy · https://leetcode.com/problems/logger-rate-limiter/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Logger {
public:
    Logger() {
        TODO();
    }
    
    bool shouldPrintMessage(int timestamp, string& message) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    Logger *obj = new Logger();
    { string a1_message = string("foo"); obj->shouldPrintMessage(1, a1_message); }
    { string a2_message = string("bar"); obj->shouldPrintMessage(2, a2_message); }
    { string a3_message = string("foo"); obj->shouldPrintMessage(3, a3_message); }
    { string a4_message = string("bar"); obj->shouldPrintMessage(8, a4_message); }
    { string a5_message = string("foo"); obj->shouldPrintMessage(10, a5_message); }
    { string a6_message = string("foo"); obj->shouldPrintMessage(11, a6_message); }
}
