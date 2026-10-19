// 253. Meeting Rooms II · Medium · https://leetcode.com/problems/meeting-rooms-ii/
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
    int minMeetingRooms(vector<vector<int>>& intervals) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    vector<vector<int>> intervals = vector<vector<int>>{{0, 30}, {5, 10}, {15, 20}};
    Solution().minMeetingRooms(intervals);
}

TEST(example_2) {
    // Premium problem: the expected output is not public, so this only runs it.
    vector<vector<int>> intervals = vector<vector<int>>{{7, 10}, {2, 4}};
    Solution().minMeetingRooms(intervals);
}
