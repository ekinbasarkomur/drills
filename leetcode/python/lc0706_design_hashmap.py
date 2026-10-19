"""
706. Design HashMap · Easy · https://leetcode.com/problems/design-hashmap/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyHashMap:

    def __init__(self):
        raise NotImplementedError
    def put(self, key: int, value: int) -> None:
        raise NotImplementedError
    def get(self, key: int) -> int:
        raise NotImplementedError
    def remove(self, key: int) -> None:
        raise NotImplementedError
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    assert obj.get(3) == -1
    obj.put(2, 1)
    assert obj.get(2) == 1
    obj.remove(2)
    assert obj.get(2) == -1
