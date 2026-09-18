// 146. LRU Cache
// https://leetcode.com/problems/lru-cache/
//
// Problem: a fixed-capacity key/value store. get and put both count as "using"
//          a key; when the cache is full, the least recently used key is
//          evicted. Both operations must be O(1) on average.
// Note: a hash map gives O(1) lookup but no order; a list gives order but O(n)
//       lookup. The usual answer is both at once -- the map's value is a
//       pointer into the list.
// Approach:
// Time O(?) per operation, space O(?)

#include <list>
#include <unordered_map>

#include "test.hpp"

using namespace std;

class LRUCache {
public:
    LRUCache(int capacity) {
        (void)capacity; // TODO
    }

    int get(int key) {
        (void)key;
        return -1; // TODO
    }

    void put(int key, int value) {
        (void)key;
        (void)value; // TODO
    }
};

// ---------------------------------------------------------------- tests

TEST(example_1) {
    LRUCache c(2);
    c.put(1, 10);
    CHECK((c.get(1) == 10));
    c.put(2, 20);
    c.put(3, 30); // evicts key 1
    CHECK((c.get(2) == 20));
    CHECK((c.get(1) == -1));
}

TEST(missing_key_returns_minus_one) {
    LRUCache c(2);
    CHECK((c.get(7) == -1));
}

TEST(overwriting_a_key_updates_its_value) {
    LRUCache c(2);
    c.put(1, 10);
    c.put(1, 99);
    CHECK((c.get(1) == 99));
}

TEST(overwriting_does_not_grow_the_cache) {
    LRUCache c(2);
    c.put(1, 10);
    c.put(1, 11);
    c.put(2, 20);
    CHECK((c.get(1) == 11));
    CHECK((c.get(2) == 20));
}

TEST(capacity_one_evicts_every_time) {
    LRUCache c(1);
    c.put(1, 10);
    c.put(2, 20);
    CHECK((c.get(1) == -1));
    CHECK((c.get(2) == 20));
}

TEST(a_get_counts_as_use_and_saves_a_key) {
    LRUCache c(2);
    c.put(1, 10);
    c.put(2, 20);
    c.get(1); // 2 is now the least recently used
    c.put(3, 30);
    CHECK((c.get(2) == -1));
    CHECK((c.get(1) == 10));
    CHECK((c.get(3) == 30));
}

TEST(a_put_on_an_existing_key_counts_as_use) {
    LRUCache c(2);
    c.put(1, 10);
    c.put(2, 20);
    c.put(1, 11); // 2 is now the least recently used
    c.put(3, 30);
    CHECK((c.get(2) == -1));
    CHECK((c.get(1) == 11));
}

TEST(a_failed_get_does_not_change_the_order) {
    LRUCache c(2);
    c.put(1, 10);
    c.put(2, 20);
    c.get(99);    // not present
    c.put(3, 30); // must still evict 1
    CHECK((c.get(1) == -1));
    CHECK((c.get(2) == 20));
}

TEST(filling_exactly_to_capacity_evicts_nothing) {
    LRUCache c(3);
    c.put(1, 10);
    c.put(2, 20);
    c.put(3, 30);
    CHECK((c.get(1) == 10));
    CHECK((c.get(2) == 20));
    CHECK((c.get(3) == 30));
}

TEST(value_range_extremes) {
    LRUCache c(2);
    c.put(0, 0);
    c.put(10000, 100000);
    CHECK((c.get(0) == 0));
    CHECK((c.get(10000) == 100000));
}

TEST(many_operations_stay_constant_time) {
    // 3000 keys held, then 100_000 more puts sweeping past them.
    // An O(n) eviction scan will crawl here.
    LRUCache c(3000);
    for (int i = 0; i < 3000; ++i)
        c.put(i, i * 2);
    CHECK((c.get(0) == 0)); // still present, and now most recent
    for (int i = 3000; i < 10000; ++i)
        c.put(i, i);
    CHECK((c.get(9999) == 9999)); // newest survived
    CHECK((c.get(1) == -1));      // oldest was evicted
}
