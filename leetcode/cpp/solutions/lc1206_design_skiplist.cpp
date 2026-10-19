// 1206. Design Skiplist · Hard · https://leetcode.com/problems/design-skiplist/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Skiplist {
public:
    Skiplist() {
        TODO();
    }
    
    bool search(int target) {
        TODO();
    }
    
    void add(int num) {
        TODO();
    }
    
    bool erase(int num) {
        TODO();
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    Skiplist *obj = new Skiplist();
    obj->add(1);
    obj->add(2);
    obj->add(3);
    CHECK_EQ(obj->search(0), false);
    obj->add(4);
    CHECK_EQ(obj->search(1), true);
    CHECK_EQ(obj->erase(0), false);
    CHECK_EQ(obj->erase(1), true);
    CHECK_EQ(obj->search(1), false);
}
