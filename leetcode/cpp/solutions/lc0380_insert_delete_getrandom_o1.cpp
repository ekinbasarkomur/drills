// 380. Insert Delete GetRandom O(1) · Medium · https://leetcode.com/problems/insert-delete-getrandom-o1/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class RandomizedSet {
public:
    RandomizedSet() {
        TODO();
    }
    
    bool insert(int val) {
        TODO();
    }
    
    bool remove(int val) {
        TODO();
    }
    
    int getRandom() {
        TODO();
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    RandomizedSet *obj = new RandomizedSet();
    CHECK_EQ(obj->insert(1), true);
    CHECK_EQ(obj->remove(2), false);
    CHECK_EQ(obj->insert(2), true);
    obj->getRandom();
    CHECK_EQ(obj->remove(1), true);
    CHECK_EQ(obj->insert(2), false);
    obj->getRandom();
}
