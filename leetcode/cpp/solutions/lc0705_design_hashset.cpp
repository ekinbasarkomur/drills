// 705. Design HashSet · Easy · https://leetcode.com/problems/design-hashset/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class MyHashSet {
public:
    MyHashSet() {
        TODO();
    }
    
    void add(int key) {
        TODO();
    }
    
    void remove(int key) {
        TODO();
    }
    
    bool contains(int key) {
        TODO();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    MyHashSet *obj = new MyHashSet();
    obj->add(1);
    obj->add(10001);
    obj->add(1);
    obj->remove(1);
    obj->contains(1);
    obj->add(7);
    obj->add(10007);
    obj->add(7);
    obj->remove(7);
    obj->contains(7);
    obj->add(123);
    obj->add(10123);
    obj->add(123);
    obj->remove(123);
    obj->contains(123);
    obj->add(5000);
    obj->add(15000);
    obj->add(5000);
    obj->remove(5000);
    obj->contains(5000);
}
