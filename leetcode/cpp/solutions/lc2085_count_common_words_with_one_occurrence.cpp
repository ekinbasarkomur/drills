// 2085. Count Common Words With One Occurrence · Easy · https://leetcode.com/problems/count-common-words-with-one-occurrence/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<string> words1 = vector<string>{"leetcode", "is", "amazing", "as", "is"};
    vector<string> words2 = vector<string>{"amazing", "leetcode", "is"};
    CHECK_EQ(Solution().countWords(words1, words2), 2);
}

TEST(example_2) {
    vector<string> words1 = vector<string>{"b", "bb", "bbb"};
    vector<string> words2 = vector<string>{"a", "aa", "aaa"};
    CHECK_EQ(Solution().countWords(words1, words2), 0);
}

TEST(example_3) {
    vector<string> words1 = vector<string>{"a", "ab"};
    vector<string> words2 = vector<string>{"a", "a", "a", "ab"};
    CHECK_EQ(Solution().countWords(words1, words2), 1);
}
