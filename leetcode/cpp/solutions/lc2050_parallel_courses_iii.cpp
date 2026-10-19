// 2050. Parallel Courses III · Hard · https://leetcode.com/problems/parallel-courses-iii/
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
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 3;
    vector<vector<int>> relations = vector<vector<int>>{{1, 3}, {2, 3}};
    vector<int> time = vector<int>{3, 2, 5};
    CHECK_EQ(Solution().minimumTime(n, relations, time), 8);
}

TEST(example_2) {
    int n = 5;
    vector<vector<int>> relations = vector<vector<int>>{{1, 5}, {2, 5}, {3, 5}, {3, 4}, {4, 5}};
    vector<int> time = vector<int>{1, 2, 3, 4, 5};
    CHECK_EQ(Solution().minimumTime(n, relations, time), 12);
}
