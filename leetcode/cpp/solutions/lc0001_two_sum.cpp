// 1. Two Sum                   https://leetcode.com/problems/two-sum/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return the two indices whose values add up to target, smaller first.
// Approach: one pass. Before storing a number, look up whether the complement
//           it needs is already on the map -- if so, that earlier index and the
//           current one are the answer.
//           Time O(n), space O(n).

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> seen;
        
        for (int i = 0; i < size(nums); i++)
        {
            int diff = target - nums[i];
            if(seen.contains(diff))
            {
                return {i, seen[diff]};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};
// ---------------------------------------------------------------- tests
// twoSum takes a non-const reference, so it cannot be handed a temporary.

using vi = vector<int>;

// LeetCode accepts the two indices in either order, so compare them sorted.
static vi twoSum(vi nums, int target) {
    vi got = Solution().twoSum(nums, target);
    sort(got.begin(), got.end());
    return got;
}

TEST(example_1) { CHECK_EQ(twoSum({3, 4, 5, 6}, 7), (vi{0, 1})); }

TEST(example_2) { CHECK_EQ(twoSum({4, 5, 6}, 10), (vi{0, 2})); }

TEST(example_3) { CHECK_EQ(twoSum({5, 5}, 10), (vi{0, 1})); }

TEST(answer_is_the_last_two) { CHECK_EQ(twoSum({1, 9, 3, 4}, 7), (vi{2, 3})); }

TEST(negative_numbers) { CHECK_EQ(twoSum({-3, 4, 7, -1}, -4), (vi{0, 3})); }

TEST(target_is_zero) { CHECK_EQ(twoSum({-8, 2, 8}, 0), (vi{0, 2})); }

TEST(extreme_values) {
    CHECK_EQ(twoSum({10000000, -10000000, 3}, 0), (vi{0, 1}));
}
