// 743. Network Delay Time · Medium · https://leetcode.com/problems/network-delay-time/
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
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> times = vector<vector<int>>{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}};
    int n = 4;
    int k = 2;
    CHECK_EQ(Solution().networkDelayTime(times, n, k), 2);
}

TEST(example_2) {
    vector<vector<int>> times = vector<vector<int>>{{1, 2, 1}};
    int n = 2;
    int k = 1;
    CHECK_EQ(Solution().networkDelayTime(times, n, k), 1);
}

TEST(example_3) {
    vector<vector<int>> times = vector<vector<int>>{{1, 2, 1}};
    int n = 2;
    int k = 2;
    CHECK_EQ(Solution().networkDelayTime(times, n, k), -1);
}
