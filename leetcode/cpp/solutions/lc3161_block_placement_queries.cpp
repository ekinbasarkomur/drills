// 3161. Block Placement Queries · Hard · https://leetcode.com/problems/block-placement-queries/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> queries = vector<vector<int>>{{1, 2}, {2, 3, 3}, {2, 3, 1}, {2, 2, 2}};
    CHECK_EQ(Solution().getResults(queries), (vector<bool>{false, true, true}));
}

TEST(example_2) {
    vector<vector<int>> queries = vector<vector<int>>{{1, 7}, {2, 7, 6}, {1, 2}, {2, 7, 5}, {2, 7, 6}};
    CHECK_EQ(Solution().getResults(queries), (vector<bool>{true, true, false}));
}
