// 66. Plus One · Easy · https://leetcode.com/problems/plus-one/
// Plan: Aşama 0 · Math
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> digits = vector<int>{1, 2, 3};
    CHECK_EQ(Solution().plusOne(digits), (vector<int>{1, 2, 4}));
}

TEST(example_2) {
    vector<int> digits = vector<int>{4, 3, 2, 1};
    CHECK_EQ(Solution().plusOne(digits), (vector<int>{4, 3, 2, 2}));
}

TEST(example_3) {
    vector<int> digits = vector<int>{9};
    CHECK_EQ(Solution().plusOne(digits), (vector<int>{1, 0}));
}
