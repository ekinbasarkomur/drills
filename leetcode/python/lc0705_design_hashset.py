"""
705. Design HashSet · Easy · https://leetcode.com/problems/design-hashset/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyHashSet:

    def __init__(self):
        raise NotImplementedError
    def add(self, key: int) -> None:
        raise NotImplementedError
    def remove(self, key: int) -> None:
        raise NotImplementedError
    def contains(self, key: int) -> bool:
        raise NotImplementedError
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyHashSet()
    obj.add(1)
    obj.add(10001)
    obj.add(1)
    obj.remove(1)
    obj.contains(1)
    obj.add(7)
    obj.add(10007)
    obj.add(7)
    obj.remove(7)
    obj.contains(7)
    obj.add(123)
    obj.add(10123)
    obj.add(123)
    obj.remove(123)
    obj.contains(123)
    obj.add(5000)
    obj.add(15000)
    obj.add(5000)
    obj.remove(5000)
    obj.contains(5000)
