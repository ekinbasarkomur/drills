// 393. UTF-8 Validation · Medium · https://leetcode.com/problems/utf-8-validation/
// Plan: Aşama 1 · Bit Manipulation
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> data = vector<int>{197, 130, 1};
    CHECK_EQ(Solution().validUtf8(data), true);
}

TEST(example_2) {
    vector<int> data = vector<int>{235, 140, 4};
    CHECK_EQ(Solution().validUtf8(data), false);
}
