// 765. Couples Holding Hands · Hard · https://leetcode.com/problems/couples-holding-hands/
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
    int minSwapsCouples(vector<int>& row) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> row = vector<int>{0, 2, 1, 3};
    CHECK_EQ(Solution().minSwapsCouples(row), 1);
}

TEST(example_2) {
    vector<int> row = vector<int>{3, 2, 0, 1};
    CHECK_EQ(Solution().minSwapsCouples(row), 0);
}
