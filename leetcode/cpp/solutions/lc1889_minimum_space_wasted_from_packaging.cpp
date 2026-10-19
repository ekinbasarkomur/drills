// 1889. Minimum Space Wasted From Packaging · Hard · https://leetcode.com/problems/minimum-space-wasted-from-packaging/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> packages = vector<int>{2, 3, 5};
    vector<vector<int>> boxes = vector<vector<int>>{{4, 8}, {2, 8}};
    CHECK_EQ(Solution().minWastedSpace(packages, boxes), 6);
}

TEST(example_2) {
    vector<int> packages = vector<int>{2, 3, 5};
    vector<vector<int>> boxes = vector<vector<int>>{{1, 4}, {2, 3}, {3, 4}};
    CHECK_EQ(Solution().minWastedSpace(packages, boxes), -1);
}

TEST(example_3) {
    vector<int> packages = vector<int>{3, 5, 8, 10, 11, 12};
    vector<vector<int>> boxes = vector<vector<int>>{{12}, {11, 9}, {10, 5, 14}};
    CHECK_EQ(Solution().minWastedSpace(packages, boxes), 9);
}
