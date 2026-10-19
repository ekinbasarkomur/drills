// 460. LFU Cache · Hard · https://leetcode.com/problems/lfu-cache/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class LFUCache {
public:
    LFUCache(int capacity) {
        TODO();
    }
    
    int get(int key) {
        TODO();
    }
    
    void put(int key, int value) {
        TODO();
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int capacity = 2;
    LFUCache *obj = new LFUCache(capacity);
    obj->put(1, 1);
    obj->put(2, 2);
    CHECK_EQ(obj->get(1), 1);
    obj->put(3, 3);
    CHECK_EQ(obj->get(2), -1);
    CHECK_EQ(obj->get(3), 3);
    obj->put(4, 4);
    CHECK_EQ(obj->get(1), -1);
    CHECK_EQ(obj->get(3), 3);
    CHECK_EQ(obj->get(4), 4);
}
