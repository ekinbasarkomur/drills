// 432. All O`one Data Structure · Hard · https://leetcode.com/problems/all-oone-data-structure/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class AllOne {
public:
    AllOne() {
        TODO();
    }
    
    void inc(string key) {
        TODO();
    }
    
    void dec(string key) {
        TODO();
    }
    
    string getMaxKey() {
        TODO();
    }
    
    string getMinKey() {
        TODO();
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    AllOne *obj = new AllOne();
    obj->inc("hello");
    obj->inc("hello");
    CHECK_EQ(obj->getMaxKey(), (string("hello")));
    CHECK_EQ(obj->getMinKey(), (string("hello")));
    obj->inc("leet");
    CHECK_EQ(obj->getMaxKey(), (string("hello")));
    CHECK_EQ(obj->getMinKey(), (string("leet")));
}
