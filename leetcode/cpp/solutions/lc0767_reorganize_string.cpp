// 767. Reorganize String · Medium · https://leetcode.com/problems/reorganize-string/
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
    string reorganizeString(string s) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    string s = string("aab");
    CHECK_EQ(Solution().reorganizeString(s), (string("aba")));
}

TEST(example_2) {
    string s = string("aaab");
    CHECK_EQ(Solution().reorganizeString(s), (string("")));
}
