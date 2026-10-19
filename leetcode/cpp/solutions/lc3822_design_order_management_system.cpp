// 3822. Design Order Management System · Medium · https://leetcode.com/problems/design-order-management-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class OrderManagementSystem {
public:
    OrderManagementSystem() {
        TODO();
    }
    
    void addOrder(int orderId, string& orderType, int price) {
        TODO();
    }
    
    void modifyOrder(int orderId, int newPrice) {
        TODO();
    }
    
    void cancelOrder(int orderId) {
        TODO();
    }
    
    vector<int> getOrdersAtPrice(string& orderType, int price) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    OrderManagementSystem *obj = new OrderManagementSystem();
    { string a1_orderType = string("buy"); obj->addOrder(1, a1_orderType, 1); }
    { string a2_orderType = string("buy"); obj->addOrder(2, a2_orderType, 1); }
    { string a3_orderType = string("sell"); obj->addOrder(3, a3_orderType, 2); }
    { string a4_orderType = string("buy"); obj->getOrdersAtPrice(a4_orderType, 1); }
    obj->modifyOrder(1, 3);
    obj->modifyOrder(2, 1);
    { string a7_orderType = string("buy"); obj->getOrdersAtPrice(a7_orderType, 1); }
    obj->cancelOrder(3);
    obj->cancelOrder(2);
    { string a10_orderType = string("buy"); obj->getOrdersAtPrice(a10_orderType, 1); }
}
