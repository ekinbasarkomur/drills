// 362. Design Hit Counter · Medium · https://leetcode.com/problems/design-hit-counter/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class HitCounter {
public:
    HitCounter() {
        TODO();
    }
    
    void hit(int timestamp) {
        TODO();
    }
    
    int getHits(int timestamp) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    HitCounter *obj = new HitCounter();
    obj->hit(1);
    obj->hit(2);
    obj->hit(3);
    obj->getHits(4);
    obj->hit(300);
    obj->getHits(300);
    obj->getHits(301);
}
