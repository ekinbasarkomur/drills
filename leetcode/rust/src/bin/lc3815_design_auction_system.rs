// 3815. Design Auction System · Medium · https://leetcode.com/problems/design-auction-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct AuctionSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AuctionSystem {

    fn new() -> Self {
        todo!()
    }
    
    fn add_bid(&self, user_id: i32, item_id: i32, bid_amount: i32) {
        todo!()
    }
    
    fn update_bid(&self, user_id: i32, item_id: i32, new_amount: i32) {
        todo!()
    }
    
    fn remove_bid(&self, user_id: i32, item_id: i32) {
        todo!()
    }
    
    fn get_highest_bidder(&self, item_id: i32) -> i32 {
        todo!()
    }
}

/**
 * Your AuctionSystem object will be instantiated and called as such:
 * let obj = AuctionSystem::new();
 * obj.add_bid(userId, itemId, bidAmount);
 * obj.update_bid(userId, itemId, newAmount);
 * obj.remove_bid(userId, itemId);
 * let ret_4: i32 = obj.get_highest_bidder(itemId);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = AuctionSystem::new();
        obj.add_bid(1, 7, 5);
        obj.add_bid(2, 7, 6);
        assert_eq!(obj.get_highest_bidder(7), 2);
        obj.update_bid(1, 7, 8);
        assert_eq!(obj.get_highest_bidder(7), 1);
        obj.remove_bid(2, 7);
        assert_eq!(obj.get_highest_bidder(7), 1);
        assert_eq!(obj.get_highest_bidder(3), -1);
    }
}
