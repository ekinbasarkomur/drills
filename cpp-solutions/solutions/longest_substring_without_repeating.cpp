// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
//
// Problem: length of the longest contiguous stretch of s in which no
//          character repeats. s may contain any printable ASCII.
// Note: A window that only ever grows from the right and shrinks from the
//       left visits each character twice at most.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        (void)s;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests

static int lengthOfLongestSubstring(string s) {
    return Solution().lengthOfLongestSubstring(s);
}

TEST(example_1) { CHECK((lengthOfLongestSubstring("zxyzxyz") == 3)); }

TEST(example_2) { CHECK((lengthOfLongestSubstring("xxxx") == 1)); }

TEST(empty_string) { CHECK((lengthOfLongestSubstring("") == 0)); }

TEST(single_character) { CHECK((lengthOfLongestSubstring("a") == 1)); }

TEST(two_distinct_characters) { CHECK((lengthOfLongestSubstring("ab") == 2)); }

TEST(every_character_is_the_same) {
    CHECK((lengthOfLongestSubstring("bbbbb") == 1));
}

TEST(the_classic_leetcode_case) {
    CHECK((lengthOfLongestSubstring("abcabcbb") == 3));
}

TEST(the_answer_is_not_a_prefix) {
    // \"wke\", not \"pwe\" -- the answer must be contiguous
    CHECK((lengthOfLongestSubstring("pwwkew") == 3));
}

TEST(a_repeat_before_the_window_start) {
    // after 'a' repeats the window must not jump back behind the second 'b'
    CHECK((lengthOfLongestSubstring("abba") == 2));
}

TEST(stale_index_must_be_ignored) {
    // \"mzuxt\"
    CHECK((lengthOfLongestSubstring("tmmzuxt") == 5));
}

TEST(spaces_count_as_characters) {
    CHECK((lengthOfLongestSubstring("a b c") == 3));
}

TEST(punctuation_and_symbols) {
    CHECK((lengthOfLongestSubstring(" !@# !@#") == 4));
}

TEST(largest_allowed_input) {
    // 50_000 characters cycling through the 95 printable ASCII codes, so the
    // answer is one full cycle. An O(n^2) solution will hang here.
    string s;
    for (int i = 0; i < 50000; ++i)
        s += char(32 + i % 95);
    CHECK((lengthOfLongestSubstring(s) == 95));
}
