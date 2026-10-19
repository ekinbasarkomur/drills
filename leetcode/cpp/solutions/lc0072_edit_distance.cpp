// 72. Edit Distance · Medium · https://leetcode.com/problems/edit-distance/
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
    int minDistance(string word1, string word2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string word1 = string("horse");
    string word2 = string("ros");
    CHECK_EQ(Solution().minDistance(word1, word2), 3);
}

TEST(example_2) {
    string word1 = string("intention");
    string word2 = string("execution");
    CHECK_EQ(Solution().minDistance(word1, word2), 5);
}
