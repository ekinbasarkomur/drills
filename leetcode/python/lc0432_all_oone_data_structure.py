"""
432. All O`one Data Structure · Hard · https://leetcode.com/problems/all-oone-data-structure/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class AllOne:

    def __init__(self):
        raise NotImplementedError
    def inc(self, key: str) -> None:
        raise NotImplementedError
    def dec(self, key: str) -> None:
        raise NotImplementedError
    def getMaxKey(self) -> str:
        raise NotImplementedError
    def getMinKey(self) -> str:
        raise NotImplementedError
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = AllOne()
    obj.inc('hello')
    obj.inc('hello')
    assert obj.getMaxKey() == 'hello'
    assert obj.getMinKey() == 'hello'
    obj.inc('leet')
    assert obj.getMaxKey() == 'hello'
    assert obj.getMinKey() == 'leet'
