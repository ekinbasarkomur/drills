// 1319. Number of Operations to Make Network Connected · Medium · https://leetcode.com/problems/number-of-operations-to-make-network-connected/
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
    int makeConnected(int n, vector<vector<int>>& connections) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 4;
    vector<vector<int>> connections = vector<vector<int>>{{0, 1}, {0, 2}, {1, 2}};
    CHECK_EQ(Solution().makeConnected(n, connections), 1);
}

TEST(example_2) {
    int n = 6;
    vector<vector<int>> connections = vector<vector<int>>{{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}};
    CHECK_EQ(Solution().makeConnected(n, connections), 2);
}

TEST(example_3) {
    int n = 6;
    vector<vector<int>> connections = vector<vector<int>>{{0, 1}, {0, 2}, {0, 3}, {1, 2}};
    CHECK_EQ(Solution().makeConnected(n, connections), -1);
}
