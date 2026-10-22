// 207. Course Schedule · Medium · https://leetcode.com/problems/course-schedule/
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
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int numCourses = 2;
    vector<vector<int>> prerequisites = vector<vector<int>>{{1, 0}};
    CHECK_EQ(Solution().canFinish(numCourses, prerequisites), true);
}

TEST(example_2) {
    int numCourses = 2;
    vector<vector<int>> prerequisites = vector<vector<int>>{{1, 0}, {0, 1}};
    CHECK_EQ(Solution().canFinish(numCourses, prerequisites), false);
}
