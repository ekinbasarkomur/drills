// 56. Merge Intervals
// https://leetcode.com/problems/merge-intervals/
//
// Problem: merge every pair of intervals that share at least one point, and
//          return the non-overlapping intervals that cover the same ground.
//          Touching counts as overlapping: [1,2] and [2,3] become [1,3].
// Note: the input is NOT sorted, and that is the whole trick -- once it is,
//       one pass is enough because only the previous interval can overlap.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals) {
        (void)intervals;
        return {}; // TODO
    }
};

// ---------------------------------------------------------------- tests
// "You may return the answer in any order" -> sort before comparing.

using vvi = vector<vector<int>>;

static vvi merge(vvi intervals) {
    vvi out = Solution().merge(intervals);
    sort(out.begin(), out.end());
    return out;
}

static vvi expect(vvi intervals) {
    sort(intervals.begin(), intervals.end());
    return intervals;
}

TEST(example_1) {
    CHECK_EQ(merge({{1, 3}, {1, 5}, {6, 7}}), expect({{1, 5}, {6, 7}}));
}

TEST(example_2) {
    // touching at a single point still merges
    CHECK_EQ(merge({{1, 2}, {2, 3}}), expect({{1, 3}}));
}

TEST(a_single_interval) { CHECK_EQ(merge({{1, 4}}), expect({{1, 4}})); }

TEST(nothing_overlaps) {
    CHECK_EQ(merge({{1, 4}, {5, 6}}), expect({{1, 4}, {5, 6}}));
}

TEST(one_interval_swallows_the_rest) {
    CHECK_EQ(merge({{1, 10}, {2, 3}, {4, 5}}), expect({{1, 10}}));
}

TEST(input_arrives_out_of_order) {
    CHECK_EQ(merge({{5, 6}, {1, 2}, {3, 4}}), expect({{1, 2}, {3, 4}, {5, 6}}));
}

TEST(a_zero_length_interval) { CHECK_EQ(merge({{0, 0}}), expect({{0, 0}})); }

TEST(identical_intervals_collapse) {
    CHECK_EQ(merge({{1, 1}, {1, 1}}), expect({{1, 1}}));
}

TEST(value_range_extremes) {
    CHECK_EQ(merge({{0, 1000}}), expect({{0, 1000}}));
}

TEST(a_chain_that_merges_end_to_end) {
    CHECK_EQ(merge({{1, 2}, {2, 3}, {3, 4}, {4, 5}}), expect({{1, 5}}));
}

TEST(largest_allowed_input_all_merge) {
    // 1000 intervals all starting at 0: they collapse to one.
    vvi intervals;
    for (int i = 0; i < 1000; ++i)
        intervals.push_back({0, i});
    CHECK_EQ(merge(intervals), expect({{0, 999}}));
}

TEST(largest_allowed_input_none_merge) {
    // 500 intervals with a gap between each: nothing collapses.
    vvi intervals;
    for (int i = 0; i < 500; ++i)
        intervals.push_back({i * 2, i * 2});
    CHECK(merge(intervals).size() == 500);
}
