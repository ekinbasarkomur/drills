// 688. Knight Probability in Chessboard · Medium · https://leetcode.com/problems/knight-probability-in-chessboard/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 3;
    int k = 2;
    int row = 0;
    int column = 0;
    CHECK(near(Solution().knightProbability(n, k, row, column), 0.0625));
}

TEST(example_2) {
    int n = 1;
    int k = 0;
    int row = 0;
    int column = 0;
    CHECK(near(Solution().knightProbability(n, k, row, column), 1.0));
}
