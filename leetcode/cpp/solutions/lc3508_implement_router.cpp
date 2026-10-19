// 3508. Implement Router · Medium · https://leetcode.com/problems/implement-router/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Router {
public:
    Router(int memoryLimit) {
        TODO();
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        TODO();
    }
    
    vector<int> forwardPacket() {
        TODO();
    }
    
    int getCount(int destination, int startTime, int endTime) {
        TODO();
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int memoryLimit = 3;
    Router *obj = new Router(memoryLimit);
    CHECK_EQ(obj->addPacket(1, 4, 90), true);
    CHECK_EQ(obj->addPacket(2, 5, 90), true);
    CHECK_EQ(obj->addPacket(1, 4, 90), false);
    CHECK_EQ(obj->addPacket(3, 5, 95), true);
    CHECK_EQ(obj->addPacket(4, 5, 105), true);
    CHECK_EQ(obj->forwardPacket(), (vector<int>{2, 5, 90}));
    CHECK_EQ(obj->addPacket(5, 2, 110), true);
    CHECK_EQ(obj->getCount(5, 100, 110), 1);
}

TEST(example_2) {
    int memoryLimit = 2;
    Router *obj = new Router(memoryLimit);
    CHECK_EQ(obj->addPacket(7, 4, 90), true);
    CHECK_EQ(obj->forwardPacket(), (vector<int>{7, 4, 90}));
    CHECK_EQ(obj->forwardPacket(), (vector<int>{}));
}
