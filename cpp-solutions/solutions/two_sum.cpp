// 1. Two Sum                   https://leetcode.com/problems/two-sum/
//
// Problem: return the two indices whose values add up to target, smaller first.
// Approach: one pass. Before storing a number, look up whether the complement
//           it needs is already on the map -- if so, that earlier index and the
//           current one are the answer.
//           Time O(n), space O(n).

#include <iostream>
#include <unordered_map>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {

        unordered_map<int, int> seen;

        for (size_t i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            //cout << i << " " << diff << endl;

            if (seen.contains(diff)) {
                return {seen[diff], static_cast<int>(i)};
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};

// ---------------------------------------------------------------- tests
// twoSum takes a non-const reference, so it cannot be handed a temporary.

using vi = vector<int>;

static vi twoSum(vi nums, int target) {
    return Solution().twoSum(nums, target);
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
