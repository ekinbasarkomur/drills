// 502. IPO · Hard · https://leetcode.com/problems/ipo/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int k = 2;
    int w = 0;
    vector<int> profits = vector<int>{1, 2, 3};
    vector<int> capital = vector<int>{0, 1, 1};
    CHECK_EQ(Solution().findMaximizedCapital(k, w, profits, capital), 4);
}

TEST(example_2) {
    int k = 3;
    int w = 0;
    vector<int> profits = vector<int>{1, 2, 3};
    vector<int> capital = vector<int>{0, 1, 2};
    CHECK_EQ(Solution().findMaximizedCapital(k, w, profits, capital), 6);
}
