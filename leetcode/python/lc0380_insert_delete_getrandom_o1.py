"""
380. Insert Delete GetRandom O(1) · Medium · https://leetcode.com/problems/insert-delete-getrandom-o1/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class RandomizedSet:

    def __init__(self):
        raise NotImplementedError
    def insert(self, val: int) -> bool:
        raise NotImplementedError
    def remove(self, val: int) -> bool:
        raise NotImplementedError
    def getRandom(self) -> int:
        raise NotImplementedError
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = RandomizedSet()
    check(obj.insert(1), True, "obj.insert(1)")
    check(obj.remove(2), False, "obj.remove(2)")
    check(obj.insert(2), True, "obj.insert(2)")
    obj.getRandom()
    check(obj.remove(1), True, "obj.remove(1)")
    check(obj.insert(2), False, "obj.insert(2)")
    obj.getRandom()
