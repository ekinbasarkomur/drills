// 901. Online Stock Span · Medium · https://leetcode.com/problems/online-stock-span/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class StockSpanner {
public:
    StockSpanner() {
        TODO();
    }
    
    int next(int price) {
        TODO();
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    StockSpanner *obj = new StockSpanner();
    CHECK_EQ(obj->next(100), 1);
    CHECK_EQ(obj->next(80), 1);
    CHECK_EQ(obj->next(60), 1);
    CHECK_EQ(obj->next(70), 2);
    CHECK_EQ(obj->next(60), 1);
    CHECK_EQ(obj->next(75), 4);
    CHECK_EQ(obj->next(85), 6);
}
