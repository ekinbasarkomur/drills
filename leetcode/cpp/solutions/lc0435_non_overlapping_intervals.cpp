// 435. Non-overlapping Intervals · Medium · https://leetcode.com/problems/non-overlapping-intervals/
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> intervals = vector<vector<int>>{{1, 2}, {2, 3}, {3, 4}, {1, 3}};
    CHECK_EQ(Solution().eraseOverlapIntervals(intervals), 1);
}

TEST(example_2) {
    vector<vector<int>> intervals = vector<vector<int>>{{1, 2}, {1, 2}, {1, 2}};
    CHECK_EQ(Solution().eraseOverlapIntervals(intervals), 2);
}

TEST(example_3) {
    vector<vector<int>> intervals = vector<vector<int>>{{1, 2}, {2, 3}};
    CHECK_EQ(Solution().eraseOverlapIntervals(intervals), 0);
}
