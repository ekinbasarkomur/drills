// 3822. Design Order Management System · Medium · https://leetcode.com/problems/design-order-management-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct OrderManagementSystem {

}


impl OrderManagementSystem {

    fn new() -> Self {
        todo!()
    }
    
    fn add_order(&self, order_id: i32, order_type: String, price: i32) {
        todo!()
    }
    
    fn modify_order(&self, order_id: i32, new_price: i32) {
        todo!()
    }
    
    fn cancel_order(&self, order_id: i32) {
        todo!()
    }
    
    fn get_orders_at_price(&self, order_type: String, price: i32) -> Vec<i32> {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        // Premium problem: the expected output is not public, so this only runs it.
        let mut obj = OrderManagementSystem::new();
        obj.add_order(1, "buy".to_string(), 1);
        obj.add_order(2, "buy".to_string(), 1);
        obj.add_order(3, "sell".to_string(), 2);
        obj.get_orders_at_price("buy".to_string(), 1);
        obj.modify_order(1, 3);
        obj.modify_order(2, 1);
        obj.get_orders_at_price("buy".to_string(), 1);
        obj.cancel_order(3);
        obj.cancel_order(2);
        obj.get_orders_at_price("buy".to_string(), 1);
    }
}
