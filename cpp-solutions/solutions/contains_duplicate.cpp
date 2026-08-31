// 217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/
//
// Problem: return true if any value appears more than once in nums.
// Approach: walk the array once, keep every number seen so far in a hash set.
//           Time O(n), space O(n).

#include <unordered_set>
#include <vector>

#include "test.hpp"

bool hasDuplicate(const std::vector<int> &nums) {
    std::unordered_set<int> seen;
    for (int num : nums) {
        if (seen.count(num)) {
            return true;
        }
        seen.insert(num);
    }
    return false;
}

// ---------------------------------------------------------------- tests

TEST(example_1) { CHECK(hasDuplicate({1, 2, 3, 3})); }

TEST(example_2) { CHECK(!hasDuplicate({1, 2, 3, 4})); }

TEST(empty_array) { CHECK(!hasDuplicate({})); }

TEST(single_element) { CHECK(!hasDuplicate({7})); }

TEST(duplicate_at_the_very_end) { CHECK(hasDuplicate({1, 2, 3, 4, 5, 1})); }

TEST(negatives_and_extremes) {
    CHECK(hasDuplicate({-1000000000, 0, -1000000000}));
    CHECK(!hasDuplicate({-1000000000, 1000000000}));
}
