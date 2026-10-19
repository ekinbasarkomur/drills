// 706. Design HashMap · Easy · https://leetcode.com/problems/design-hashmap/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyHashMap {
public:
    MyHashMap() {
        TODO();
    }
    
    void put(int key, int value) {
        TODO();
    }
    
    int get(int key) {
        TODO();
    }
    
    void remove(int key) {
        TODO();
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyHashMap *obj = new MyHashMap();
    obj->put(1, 1);
    obj->put(2, 2);
    CHECK_EQ(obj->get(1), 1);
    CHECK_EQ(obj->get(3), -1);
    obj->put(2, 1);
    CHECK_EQ(obj->get(2), 1);
    obj->remove(2);
    CHECK_EQ(obj->get(2), -1);
}
