// 1801. Number of Orders in the Backlog · Medium · https://leetcode.com/problems/number-of-orders-in-the-backlog/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> orders = vector<vector<int>>{{10, 5, 0}, {15, 2, 1}, {25, 1, 1}, {30, 4, 0}};
    CHECK_EQ(Solution().getNumberOfBacklogOrders(orders), 6);
}

TEST(example_2) {
    vector<vector<int>> orders = vector<vector<int>>{{7, 1000000000, 1}, {15, 3, 0}, {5, 999999995, 0}, {5, 1, 1}};
    CHECK_EQ(Solution().getNumberOfBacklogOrders(orders), 999999984);
}
