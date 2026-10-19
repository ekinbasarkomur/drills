// 1011. Capacity To Ship Packages Within D Days · Medium · https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<int> weights = vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int days = 5;
    CHECK_EQ(Solution().shipWithinDays(weights, days), 15);
}

TEST(example_2) {
    vector<int> weights = vector<int>{3, 2, 2, 4, 1, 4};
    int days = 3;
    CHECK_EQ(Solution().shipWithinDays(weights, days), 6);
}

TEST(example_3) {
    vector<int> weights = vector<int>{1, 2, 3, 1, 1};
    int days = 4;
    CHECK_EQ(Solution().shipWithinDays(weights, days), 3);
}
