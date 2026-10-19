"""
460. LFU Cache · Hard · https://leetcode.com/problems/lfu-cache/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class LFUCache:

    def __init__(self, capacity: int):
        raise NotImplementedError
    def get(self, key: int) -> int:
        raise NotImplementedError
    def put(self, key: int, value: int) -> None:
        raise NotImplementedError
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = LFUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    obj.put(3, 3)
    assert obj.get(2) == -1
    assert obj.get(3) == 3
    obj.put(4, 4)
    assert obj.get(1) == -1
    assert obj.get(3) == 3
    assert obj.get(4) == 4
