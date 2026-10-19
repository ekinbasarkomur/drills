// 907. Sum of Subarray Minimums · Medium · https://leetcode.com/problems/sum-of-subarray-minimums/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> arr = vector<int>{3, 1, 2, 4};
    CHECK_EQ(Solution().sumSubarrayMins(arr), 17);
}

TEST(example_2) {
    vector<int> arr = vector<int>{50};
    CHECK_EQ(Solution().sumSubarrayMins(arr), 444);
}
