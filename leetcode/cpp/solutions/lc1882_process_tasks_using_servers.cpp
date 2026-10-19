// 1882. Process Tasks Using Servers · Medium · https://leetcode.com/problems/process-tasks-using-servers/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> servers = vector<int>{3, 3, 2};
    vector<int> tasks = vector<int>{1, 2, 3, 2, 1, 2};
    CHECK_EQ(Solution().assignTasks(servers, tasks), (vector<int>{2, 2, 0, 2, 1, 2}));
}

TEST(example_2) {
    vector<int> servers = vector<int>{5, 1, 4, 3, 2};
    vector<int> tasks = vector<int>{2, 1, 2, 4, 5, 2, 1};
    CHECK_EQ(Solution().assignTasks(servers, tasks), (vector<int>{1, 4, 1, 4, 1, 3, 2}));
}
