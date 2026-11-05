"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/
Plan: Aşama 0 · Linked List

Problem: a fixed-capacity key/value store. get and put both count as "using" a
         key; when the cache is full, the least recently used key is evicted.
         Both operations must be O(1) on average.
Note: a dict gives O(1) lookup but no useful order; a list gives order but O(n)
      lookup. The usual answer is both at once.
Approach:
Time O(?) per operation, space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class LRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_example_1():
    c = LRUCache(2)
    c.put(1, 10)
    check(c.get(1), 10, "c.get(1)")
    c.put(2, 20)
    c.put(3, 30)  # evicts key 1
    check(c.get(2), 20, "c.get(2)")
    check(c.get(1), -1, "c.get(1)")


def test_missing_key_returns_minus_one():
    c = LRUCache(2)
    check(c.get(7), -1, "c.get(7)")


def test_overwriting_a_key_updates_its_value():
    c = LRUCache(2)
    c.put(1, 10)
    c.put(1, 99)
    check(c.get(1), 99, "c.get(1)")


def test_overwriting_does_not_grow_the_cache():
    c = LRUCache(2)
    c.put(1, 10)
    c.put(1, 11)
    c.put(2, 20)
    check(c.get(1), 11, "c.get(1)")
    check(c.get(2), 20, "c.get(2)")


def test_capacity_one_evicts_every_time():
    c = LRUCache(1)
    c.put(1, 10)
    c.put(2, 20)
    check(c.get(1), -1, "c.get(1)")
    check(c.get(2), 20, "c.get(2)")


def test_a_get_counts_as_use_and_saves_a_key():
    c = LRUCache(2)
    c.put(1, 10)
    c.put(2, 20)
    c.get(1)  # 2 is now the least recently used
    c.put(3, 30)
    check(c.get(2), -1, "c.get(2)")
    check(c.get(1), 10, "c.get(1)")
    check(c.get(3), 30, "c.get(3)")


def test_a_put_on_an_existing_key_counts_as_use():
    c = LRUCache(2)
    c.put(1, 10)
    c.put(2, 20)
    c.put(1, 11)  # 2 is now the least recently used
    c.put(3, 30)
    check(c.get(2), -1, "c.get(2)")
    check(c.get(1), 11, "c.get(1)")


def test_a_failed_get_does_not_change_the_order():
    c = LRUCache(2)
    c.put(1, 10)
    c.put(2, 20)
    c.get(99)  # not present
    c.put(3, 30)  # must still evict 1
    check(c.get(1), -1, "c.get(1)")
    check(c.get(2), 20, "c.get(2)")


def test_filling_exactly_to_capacity_evicts_nothing():
    c = LRUCache(3)
    c.put(1, 10)
    c.put(2, 20)
    c.put(3, 30)
    check(c.get(1), 10, "c.get(1)")
    check(c.get(2), 20, "c.get(2)")
    check(c.get(3), 30, "c.get(3)")


def test_value_range_extremes():
    c = LRUCache(2)
    c.put(0, 0)
    c.put(10_000, 100_000)
    check(c.get(0), 0, "c.get(0)")
    check(c.get(10_000), 100_000, "c.get(10_000)")


def test_many_operations_stay_constant_time():
    # 3000 keys held, then more puts sweeping past them.
    # An O(n) eviction scan will crawl here.
    c = LRUCache(3000)
    for i in range(3000):
        c.put(i, i * 2)
    check(c.get(0), 0, "c.get(0)")  # still present, and now most recent
    for i in range(3000, 10_000):
        c.put(i, i)
    check(c.get(9999), 9999, "c.get(9999)")  # newest survived
    check(c.get(1), -1, "c.get(1)")  # oldest was evicted
