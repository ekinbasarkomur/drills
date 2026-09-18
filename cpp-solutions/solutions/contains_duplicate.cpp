// 217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/
//
// Problem: return true if any value appears more than once in nums.
// Approach: walk the array once, keep every number seen so far in a hash set.
//           set::contains short-circuits as soon as a repeat shows up.
//           Time O(n), space O(n).

#include <unordered_set>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int> &nums) {
        unordered_set<int> seen;

        for (int i : nums) {
            if (seen.contains(i)) {
                return true;
            }
            seen.insert(i);
        }
        return false;
    }
};

// ---------------------------------------------------------------- tests
// hasDuplicate takes a non-const reference, so the test cannot hand it a
// temporary -- each case names its vector first.

static bool hasDuplicate(vector<int> nums) {
    return Solution().hasDuplicate(nums);
}

TEST(example_1) { CHECK(hasDuplicate({1, 2, 3, 3})); }

TEST(example_2) { CHECK(!hasDuplicate({1, 2, 3, 4})); }

TEST(empty_array) { CHECK(!hasDuplicate({})); }

TEST(single_element) { CHECK(!hasDuplicate({7})); }

TEST(duplicate_at_the_very_end) { CHECK(hasDuplicate({1, 2, 3, 4, 5, 1})); }

TEST(negatives_and_extremes) {
    CHECK(hasDuplicate({-1000000000, 0, -1000000000}));
    CHECK(!hasDuplicate({-1000000000, 1000000000}));
}
