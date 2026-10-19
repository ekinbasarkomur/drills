"""
3508. Implement Router · Medium · https://leetcode.com/problems/implement-router/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Router:

    def __init__(self, memoryLimit: int):
        raise NotImplementedError
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        raise NotImplementedError
    def forwardPacket(self) -> List[int]:
        raise NotImplementedError
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        raise NotImplementedError
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Router(3)
    assert obj.addPacket(1, 4, 90) == True
    assert obj.addPacket(2, 5, 90) == True
    assert obj.addPacket(1, 4, 90) == False
    assert obj.addPacket(3, 5, 95) == True
    assert obj.addPacket(4, 5, 105) == True
    assert obj.forwardPacket() == [2, 5, 90]
    assert obj.addPacket(5, 2, 110) == True
    assert obj.getCount(5, 100, 110) == 1


def test_example_2():
    obj = Router(2)
    assert obj.addPacket(7, 4, 90) == True
    assert obj.forwardPacket() == [7, 4, 90]
    assert obj.forwardPacket() == []
