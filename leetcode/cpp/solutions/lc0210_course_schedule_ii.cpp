// 210. Course Schedule II · Medium · https://leetcode.com/problems/course-schedule-ii/
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
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int numCourses = 2;
    vector<vector<int>> prerequisites = vector<vector<int>>{{1, 0}};
    CHECK_EQ(Solution().findOrder(numCourses, prerequisites), (vector<int>{0, 1}));
}

TEST(example_2) {
    int numCourses = 4;
    vector<vector<int>> prerequisites = vector<vector<int>>{{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    CHECK_EQ(Solution().findOrder(numCourses, prerequisites), (vector<int>{0, 2, 1, 3}));
}

TEST(example_3) {
    int numCourses = 1;
    vector<vector<int>> prerequisites = vector<vector<int>>{};
    CHECK_EQ(Solution().findOrder(numCourses, prerequisites), (vector<int>{0}));
}
