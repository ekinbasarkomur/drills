"""
3822. Design Order Management System · Medium · https://leetcode.com/problems/design-order-management-system/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class OrderManagementSystem:

    def __init__(self):
        raise NotImplementedError
    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        raise NotImplementedError
    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        raise NotImplementedError
    def cancelOrder(self, orderId: int) -> None:
        raise NotImplementedError
    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    obj = OrderManagementSystem()
    obj.addOrder(1, 'buy', 1)
    obj.addOrder(2, 'buy', 1)
    obj.addOrder(3, 'sell', 2)
    obj.getOrdersAtPrice('buy', 1)
    obj.modifyOrder(1, 3)
    obj.modifyOrder(2, 1)
    obj.getOrdersAtPrice('buy', 1)
    obj.cancelOrder(3)
    obj.cancelOrder(2)
    obj.getOrdersAtPrice('buy', 1)
