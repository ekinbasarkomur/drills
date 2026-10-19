// 787. Cheapest Flights Within K Stops · Medium · https://leetcode.com/problems/cheapest-flights-within-k-stops/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 4;
    vector<vector<int>> flights = vector<vector<int>>{{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
    int src = 0;
    int dst = 3;
    int k = 1;
    CHECK_EQ(Solution().findCheapestPrice(n, flights, src, dst, k), 700);
}

TEST(example_2) {
    int n = 3;
    vector<vector<int>> flights = vector<vector<int>>{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}};
    int src = 0;
    int dst = 2;
    int k = 1;
    CHECK_EQ(Solution().findCheapestPrice(n, flights, src, dst, k), 200);
}

TEST(example_3) {
    int n = 3;
    vector<vector<int>> flights = vector<vector<int>>{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}};
    int src = 0;
    int dst = 2;
    int k = 0;
    CHECK_EQ(Solution().findCheapestPrice(n, flights, src, dst, k), 500);
}
