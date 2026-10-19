// 1515. Best Position for a Service Centre · Hard · https://leetcode.com/problems/best-position-for-a-service-centre/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> positions = vector<vector<int>>{{0, 1}, {1, 0}, {1, 2}, {2, 1}};
    CHECK(near(Solution().getMinDistSum(positions), 4.0));
}

TEST(example_2) {
    vector<vector<int>> positions = vector<vector<int>>{{1, 1}, {3, 3}};
    CHECK(near(Solution().getMinDistSum(positions), 2.82843));
}
