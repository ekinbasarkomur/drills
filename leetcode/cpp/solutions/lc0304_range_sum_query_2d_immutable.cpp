// 304. Range Sum Query 2D - Immutable · Medium · https://leetcode.com/problems/range-sum-query-2d-immutable/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {
        TODO();
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        TODO();
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<int>> matrix = vector<vector<int>>{{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}};
    NumMatrix *obj = new NumMatrix(matrix);
    CHECK_EQ(obj->sumRegion(2, 1, 4, 3), 8);
    CHECK_EQ(obj->sumRegion(1, 1, 2, 2), 11);
    CHECK_EQ(obj->sumRegion(1, 2, 2, 4), 12);
}
