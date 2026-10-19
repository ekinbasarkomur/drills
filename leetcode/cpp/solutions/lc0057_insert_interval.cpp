// 57. Insert Interval · Medium · https://leetcode.com/problems/insert-interval/
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
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> intervals = vector<vector<int>>{{1, 3}, {6, 9}};
    vector<int> newInterval = vector<int>{2, 5};
    CHECK_EQ(Solution().insert(intervals, newInterval), (vector<vector<int>>{{1, 5}, {6, 9}}));
}

TEST(example_2) {
    vector<vector<int>> intervals = vector<vector<int>>{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
    vector<int> newInterval = vector<int>{4, 8};
    CHECK_EQ(Solution().insert(intervals, newInterval), (vector<vector<int>>{{1, 2}, {3, 10}, {12, 16}}));
}
