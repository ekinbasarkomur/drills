// 84. Largest Rectangle in Histogram · Hard · https://leetcode.com/problems/largest-rectangle-in-histogram/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> heights = vector<int>{2, 1, 5, 6, 2, 3};
    CHECK_EQ(Solution().largestRectangleArea(heights), 10);
}

TEST(example_2) {
    vector<int> heights = vector<int>{2, 4};
    CHECK_EQ(Solution().largestRectangleArea(heights), 4);
}
