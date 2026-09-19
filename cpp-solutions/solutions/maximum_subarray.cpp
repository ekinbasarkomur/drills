// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/
//
// Problem: the largest sum any contiguous non-empty stretch of nums can
//          reach. Every value may be negative.
// Note: At each position you only ever choose between extending the run so
//       far and starting fresh -- whichever sum is larger.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        (void)nums;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests
// maxSubArray takes a non-const reference, so it cannot be handed a temporary.

static int maxSubArray(vector<int> nums) {
    return Solution().maxSubArray(nums);
}

TEST(example_1) { CHECK((maxSubArray({2, -3, 4, -2, 2, 1, -1, 4}) == 8)); }

TEST(example_2) {
    // the subarray must be non-empty, so 0 is not an answer
    CHECK((maxSubArray({-1}) == -1));
}

TEST(single_positive) { CHECK((maxSubArray({1}) == 1)); }

TEST(single_zero) { CHECK((maxSubArray({0}) == 0)); }

TEST(the_classic_leetcode_case) {
    CHECK((maxSubArray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6));
}

TEST(every_value_negative) {
    // take the least bad one
    CHECK((maxSubArray({-1, -2, -3}) == -1));
}

TEST(a_dip_worth_crossing) { CHECK((maxSubArray({5, 4, -1, 7, 8}) == 23)); }

TEST(alternating_signs) { CHECK((maxSubArray({1, -1, 1, -1, 1}) == 1)); }

TEST(value_range_low) { CHECK((maxSubArray({-10000}) == -10000)); }

TEST(value_range_high) { CHECK((maxSubArray({10000}) == 10000)); }

TEST(largest_allowed_input) {
    // 100_000 values alternating +10_000 and -9_999, so each pair nets +1
    // and the best subarray is the whole array.
    // An O(n^2) solution will hang here rather than fail.
    vector<int> nums(100000);
    for (int i = 0; i < 100000; ++i)
        nums[i] = (i % 2 == 0) ? 10000 : -9999;
    CHECK((maxSubArray(nums) == 59999));
}
