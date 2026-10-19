// 1326. Minimum Number of Taps to Open to Water a Garden · Hard · https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 5;
    vector<int> ranges = vector<int>{3, 4, 1, 1, 0, 0};
    CHECK_EQ(Solution().minTaps(n, ranges), 1);
}

TEST(example_2) {
    int n = 3;
    vector<int> ranges = vector<int>{0, 0, 0, 0};
    CHECK_EQ(Solution().minTaps(n, ranges), -1);
}
