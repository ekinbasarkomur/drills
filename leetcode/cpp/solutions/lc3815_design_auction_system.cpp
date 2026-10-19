// 3815. Design Auction System · Medium · https://leetcode.com/problems/design-auction-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class AuctionSystem {
public:
    AuctionSystem() {
        TODO();
    }
    
    void addBid(int userId, int itemId, int bidAmount) {
        TODO();
    }
    
    void updateBid(int userId, int itemId, int newAmount) {
        TODO();
    }
    
    void removeBid(int userId, int itemId) {
        TODO();
    }
    
    int getHighestBidder(int itemId) {
        TODO();
    }
};

/**
 * Your AuctionSystem object will be instantiated and called as such:
 * AuctionSystem* obj = new AuctionSystem();
 * obj->addBid(userId,itemId,bidAmount);
 * obj->updateBid(userId,itemId,newAmount);
 * obj->removeBid(userId,itemId);
 * int param_4 = obj->getHighestBidder(itemId);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    AuctionSystem *obj = new AuctionSystem();
    obj->addBid(1, 7, 5);
    obj->addBid(2, 7, 6);
    CHECK_EQ(obj->getHighestBidder(7), 2);
    obj->updateBid(1, 7, 8);
    CHECK_EQ(obj->getHighestBidder(7), 1);
    obj->removeBid(2, 7);
    CHECK_EQ(obj->getHighestBidder(7), 1);
    CHECK_EQ(obj->getHighestBidder(3), -1);
}
