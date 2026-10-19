// 1146. Snapshot Array · Medium · https://leetcode.com/problems/snapshot-array/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class SnapshotArray {
public:
    SnapshotArray(int length) {
        TODO();
    }
    
    void set(int index, int val) {
        TODO();
    }
    
    int snap() {
        TODO();
    }
    
    int get(int index, int snap_id) {
        TODO();
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int length = 3;
    SnapshotArray *obj = new SnapshotArray(length);
    obj->set(0, 5);
    CHECK_EQ(obj->snap(), 0);
    obj->set(0, 6);
    CHECK_EQ(obj->get(0, 0), 5);
}
