// 547. Number of Provinces · Medium · https://leetcode.com/problems/number-of-provinces/
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
    int findCircleNum(vector<vector<int>>& isConnected) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> isConnected = vector<vector<int>>{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    CHECK_EQ(Solution().findCircleNum(isConnected), 2);
}

TEST(example_2) {
    vector<vector<int>> isConnected = vector<vector<int>>{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    CHECK_EQ(Solution().findCircleNum(isConnected), 3);
}
