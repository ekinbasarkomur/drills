// 2034. Stock Price Fluctuation  · Medium · https://leetcode.com/problems/stock-price-fluctuation/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class StockPrice {
public:
    StockPrice() {
        TODO();
    }
    
    void update(int timestamp, int price) {
        TODO();
    }
    
    int current() {
        TODO();
    }
    
    int maximum() {
        TODO();
    }
    
    int minimum() {
        TODO();
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    StockPrice *obj = new StockPrice();
    obj->update(1, 10);
    obj->update(2, 5);
    CHECK_EQ(obj->current(), 5);
    CHECK_EQ(obj->maximum(), 10);
    obj->update(1, 3);
    CHECK_EQ(obj->maximum(), 5);
    obj->update(4, 2);
    CHECK_EQ(obj->minimum(), 2);
}
