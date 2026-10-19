// 1834. Single-Threaded CPU · Medium · https://leetcode.com/problems/single-threaded-cpu/
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
    vector<int> getOrder(vector<vector<int>>& tasks) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> tasks = vector<vector<int>>{{1, 2}, {2, 4}, {3, 2}, {4, 1}};
    CHECK_EQ(Solution().getOrder(tasks), (vector<int>{0, 2, 3, 1}));
}

TEST(example_2) {
    vector<vector<int>> tasks = vector<vector<int>>{{7, 10}, {7, 12}, {7, 5}, {7, 4}, {7, 2}};
    CHECK_EQ(Solution().getOrder(tasks), (vector<int>{4, 3, 2, 0, 1}));
}
