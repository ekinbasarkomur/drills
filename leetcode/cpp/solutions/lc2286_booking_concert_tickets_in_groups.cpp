// 2286. Booking Concert Tickets in Groups · Hard · https://leetcode.com/problems/booking-concert-tickets-in-groups/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class BookMyShow {
public:
    BookMyShow(int n, int m) {
        TODO();
    }
    
    vector<int> gather(int k, int maxRow) {
        TODO();
    }
    
    bool scatter(int k, int maxRow) {
        TODO();
    }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 2;
    int m = 5;
    BookMyShow *obj = new BookMyShow(n, m);
    CHECK_EQ(obj->gather(4, 0), (vector<int>{0, 0}));
    CHECK_EQ(obj->gather(2, 0), (vector<int>{}));
    CHECK_EQ(obj->scatter(5, 1), true);
    CHECK_EQ(obj->scatter(5, 1), false);
}
