// 1514. Path with Maximum Probability · Medium · https://leetcode.com/problems/path-with-maximum-probability/
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
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 3;
    vector<vector<int>> edges = vector<vector<int>>{{0, 1}, {1, 2}, {0, 2}};
    vector<double> succProb = vector<double>{0.5, 0.5, 0.2};
    int start_node = 0;
    int end_node = 2;
    CHECK(near(Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.25));
}

TEST(example_2) {
    int n = 3;
    vector<vector<int>> edges = vector<vector<int>>{{0, 1}, {1, 2}, {0, 2}};
    vector<double> succProb = vector<double>{0.5, 0.5, 0.3};
    int start_node = 0;
    int end_node = 2;
    CHECK(near(Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.3));
}

TEST(example_3) {
    int n = 3;
    vector<vector<int>> edges = vector<vector<int>>{{0, 1}};
    vector<double> succProb = vector<double>{0.5};
    int start_node = 0;
    int end_node = 2;
    CHECK(near(Solution().maxProbability(n, edges, succProb, start_node, end_node), 0.0));
}
