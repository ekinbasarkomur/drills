// 704. Binary Search
// https://leetcode.com/problems/binary-search/
// Plan: Aşama 0 · Binary Search
//
// Problem: nums is sorted ascending and every value is distinct. Return the
//          index of target, or -1. Must run in O(log n).
// Note: The classic bug is the loop bound: <= vs <, and whether the midpoint
//       moves. Get those wrong and it either misses the answer or hangs.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int search(vector<int> &nums, int target) {
        (void)nums;
        (void)target;
        return 0; // TODO
    }
};
// ---------------------------------------------------------------- tests
// search takes a non-const reference, so it cannot be handed a temporary.

static int search(vector<int> nums, int target) {
    return Solution().search(nums, target);
}

TEST(example_1) { CHECK((search({-1, 0, 2, 4, 6, 8}, 4) == 3)); }

TEST(example_2) { CHECK((search({-1, 0, 2, 4, 6, 8}, 3) == -1)); }

TEST(single_element_found) { CHECK((search({5}, 5) == 0)); }

TEST(single_element_missing) { CHECK((search({5}, 1) == -1)); }

TEST(two_elements_first) { CHECK((search({1, 2}, 1) == 0)); }

TEST(two_elements_second) { CHECK((search({1, 2}, 2) == 1)); }

TEST(target_at_the_front) { CHECK((search({1, 3, 5, 7, 9}, 1) == 0)); }

TEST(target_at_the_back) { CHECK((search({1, 3, 5, 7, 9}, 9) == 4)); }

TEST(below_everything) { CHECK((search({1, 3, 5, 7, 9}, 0) == -1)); }

TEST(above_everything) { CHECK((search({1, 3, 5, 7, 9}, 10) == -1)); }

TEST(negative_values) { CHECK((search({-9, -7, -3, -1}, -7) == 1)); }

TEST(largest_allowed_input) {
    // 10_000 elements, the constraint's ceiling, and the answer is the last
    // one. Binary search finds it in 14 steps; a linear scan takes 10_000.
    vector<int> nums(10000);
    for (int i = 0; i < 10000; ++i)
        nums[i] = i;
    CHECK((search(nums, 9999) == 9999));
}
