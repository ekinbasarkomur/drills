// 68. Text Justification · Hard · https://leetcode.com/problems/text-justification/
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
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<string> words = vector<string>{"This", "is", "an", "example", "of", "text", "justification."};
    int maxWidth = 16;
    CHECK_EQ(Solution().fullJustify(words, maxWidth), (vector<string>{"This    is    an", "example  of text", "justification.  "}));
}

TEST(example_2) {
    vector<string> words = vector<string>{"What", "must", "be", "acknowledgment", "shall", "be"};
    int maxWidth = 16;
    CHECK_EQ(Solution().fullJustify(words, maxWidth), (vector<string>{"What   must   be", "acknowledgment  ", "shall be        "}));
}

TEST(example_3) {
    vector<string> words = vector<string>{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"};
    int maxWidth = 20;
    CHECK_EQ(Solution().fullJustify(words, maxWidth), (vector<string>{"Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "}));
}
