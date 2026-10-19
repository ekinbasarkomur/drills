// 1094. Car Pooling · Medium · https://leetcode.com/problems/car-pooling/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> trips = vector<vector<int>>{{2, 1, 5}, {3, 3, 7}};
    int capacity = 4;
    CHECK_EQ(Solution().carPooling(trips, capacity), false);
}

TEST(example_2) {
    vector<vector<int>> trips = vector<vector<int>>{{2, 1, 5}, {3, 3, 7}};
    int capacity = 5;
    CHECK_EQ(Solution().carPooling(trips, capacity), true);
}
