// 837. New 21 Game · Medium · https://leetcode.com/problems/new-21-game/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 10;
    int k = 1;
    int maxPts = 10;
    CHECK(near(Solution().new21Game(n, k, maxPts), 1.0));
}

TEST(example_2) {
    int n = 6;
    int k = 1;
    int maxPts = 10;
    CHECK(near(Solution().new21Game(n, k, maxPts), 0.6));
}

TEST(example_3) {
    int n = 21;
    int k = 17;
    int maxPts = 10;
    CHECK(near(Solution().new21Game(n, k, maxPts), 0.73278));
}
