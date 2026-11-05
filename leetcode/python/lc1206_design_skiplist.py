"""
1206. Design Skiplist · Hard · https://leetcode.com/problems/design-skiplist/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Skiplist:

    def __init__(self):
        raise NotImplementedError
    def search(self, target: int) -> bool:
        raise NotImplementedError
    def add(self, num: int) -> None:
        raise NotImplementedError
    def erase(self, num: int) -> bool:
        raise NotImplementedError
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Skiplist()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    check(obj.search(0), False, "obj.search(0)")
    obj.add(4)
    check(obj.search(1), True, "obj.search(1)")
    check(obj.erase(0), False, "obj.erase(0)")
    check(obj.erase(1), True, "obj.erase(1)")
    check(obj.search(1), False, "obj.search(1)")
