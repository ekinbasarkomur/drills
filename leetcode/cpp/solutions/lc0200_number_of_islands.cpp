// 200. Number of Islands
// https://leetcode.com/problems/number-of-islands/
// Plan: Aşama 0 · Graphs
//
// Problem: count the connected groups of '1' cells in the grid. Cells join
//          horizontally and vertically only, never diagonally.
// Note: Once you reach a land cell, sink the whole island before moving on --
//       otherwise you count the same island once per cell.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int numIslands(vector<vector<char>> &grid) {
        (void)grid;
        return 0; // TODO
    }
};
// ---------------------------------------------------------------- tests
// Grids are written as rows of text; the helper converts them.
// numIslands takes a non-const reference, so it cannot take a temporary.

static int numIslands(vector<string> rows) {
    vector<vector<char>> grid;
    for (const auto &row : rows)
        grid.emplace_back(row.begin(), row.end());
    return Solution().numIslands(grid);
}

TEST(example_1) {
    CHECK((numIslands({"01110", "01010", "11000", "00000"}) == 1));
}

TEST(example_2) {
    CHECK((numIslands({"11001", "11001", "00100", "00011"}) == 4));
}

TEST(all_water) { CHECK((numIslands({"000", "000"}) == 0)); }

TEST(all_land) { CHECK((numIslands({"111", "111"}) == 1)); }

TEST(single_cell_land) { CHECK((numIslands({"1"}) == 1)); }

TEST(single_cell_water) { CHECK((numIslands({"0"}) == 0)); }

TEST(one_row) { CHECK((numIslands({"10101"}) == 3)); }

TEST(one_column) { CHECK((numIslands({"1", "0", "1", "1"}) == 2)); }

TEST(diagonals_do_not_connect) {
    // touching corners is not adjacency
    CHECK((numIslands({"10", "01"}) == 2));
}

TEST(a_ring_of_land_around_water) {
    CHECK((numIslands({"111", "101", "111"}) == 1));
}

TEST(checkerboard) { CHECK((numIslands({"101", "010", "101"}) == 5)); }

TEST(largest_allowed_input) {
    // 100x100 checkerboard, the constraint's ceiling: 2500 single-cell
    // islands, none of them touching.
    vector<string> grid;
    for (int r = 0; r < 100; ++r) {
        string row;
        for (int c = 0; c < 100; ++c)
            row += ((r + c) % 2 == 0) ? '1' : '0';
        grid.push_back(row);
    }
    CHECK((numIslands(grid) == 2500));
    CHECK((numIslands(vector<string>{}) == 2500));
}
