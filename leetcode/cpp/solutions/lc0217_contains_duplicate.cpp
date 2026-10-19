// 217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return true if any value appears more than once in nums.
// Approach: walk the array once, keep every number seen so far in a hash set.
//           set::contains short-circuits as soon as a repeat shows up.
//           Time O(n), space O(n).

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> seen(size(nums));

        for (int i : nums) {
            if (seen.count(i)) {
                return true;
            }
            seen.insert(i);
        }
        return false;
    }

};
// ---------------------------------------------------------------- tests
// containsDuplicate takes a non-const reference, so the test cannot hand it a
// temporary -- each case names its vector first.

static bool containsDuplicate(vector<int> nums) {
    return Solution().containsDuplicate(nums);
}

TEST(example_1) { CHECK(containsDuplicate({1, 2, 3, 3})); }

TEST(example_2) { CHECK(!containsDuplicate({1, 2, 3, 4})); }

TEST(empty_array) { CHECK(!containsDuplicate({})); }

TEST(single_element) { CHECK(!containsDuplicate({7})); }

TEST(duplicate_at_the_very_end) { CHECK(containsDuplicate({1, 2, 3, 4, 5, 1})); }

TEST(negatives_and_extremes) {
    CHECK(containsDuplicate({-1000000000, 0, -1000000000}));
    CHECK(!containsDuplicate({-1000000000, 1000000000}));
}
