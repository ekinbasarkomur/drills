"""
3815. Design Auction System · Medium · https://leetcode.com/problems/design-auction-system/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class AuctionSystem:

    def __init__(self):
        raise NotImplementedError
    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        raise NotImplementedError
    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        raise NotImplementedError
    def removeBid(self, userId: int, itemId: int) -> None:
        raise NotImplementedError
    def getHighestBidder(self, itemId: int) -> int:
        raise NotImplementedError
# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = AuctionSystem()
    obj.addBid(1, 7, 5)
    obj.addBid(2, 7, 6)
    assert obj.getHighestBidder(7) == 2
    obj.updateBid(1, 7, 8)
    assert obj.getHighestBidder(7) == 1
    obj.removeBid(2, 7)
    assert obj.getHighestBidder(7) == 1
    assert obj.getHighestBidder(3) == -1
