"""
981. Time Based Key-Value Store · Medium · https://leetcode.com/problems/time-based-key-value-store/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class TimeMap:

    def __init__(self):
        raise NotImplementedError
    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError
    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = TimeMap()
    obj.set('foo', 'bar', 1)
    assert obj.get('foo', 1) == 'bar'
    assert obj.get('foo', 3) == 'bar'
    obj.set('foo', 'bar2', 4)
    assert obj.get('foo', 4) == 'bar2'
    assert obj.get('foo', 5) == 'bar2'
