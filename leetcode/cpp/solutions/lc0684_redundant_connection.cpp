// 684. Redundant Connection · Medium · https://leetcode.com/problems/redundant-connection/
// Plan: Aşama 0 · Graphs
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> edges = vector<vector<int>>{{1, 2}, {1, 3}, {2, 3}};
    CHECK_EQ(Solution().findRedundantConnection(edges), (vector<int>{2, 3}));
}

TEST(example_2) {
    vector<vector<int>> edges = vector<vector<int>>{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}};
    CHECK_EQ(Solution().findRedundantConnection(edges), (vector<int>{1, 4}));
}
