// 981. Time Based Key-Value Store · Medium · https://leetcode.com/problems/time-based-key-value-store/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class TimeMap {
public:
    TimeMap() {
        TODO();
    }
    
    void set(string key, string value, int timestamp) {
        TODO();
    }
    
    string get(string key, int timestamp) {
        TODO();
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TimeMap *obj = new TimeMap();
    obj->set("foo", "bar", 1);
    CHECK_EQ(obj->get("foo", 1), (string("bar")));
    CHECK_EQ(obj->get("foo", 3), (string("bar")));
    obj->set("foo", "bar2", 4);
    CHECK_EQ(obj->get("foo", 4), (string("bar2")));
    CHECK_EQ(obj->get("foo", 5), (string("bar2")));
}
