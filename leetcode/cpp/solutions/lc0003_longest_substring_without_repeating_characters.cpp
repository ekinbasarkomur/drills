// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Plan: Aşama 0 · Sliding Window
//
// Problem: length of the longest contiguous stretch of s in which no
//          character repeats. s may contain any printable ASCII.
// Note: A window that only ever grows from the right and shrinks from the
//       left visits each character twice at most.
// Approach: sliding window with a last-seen index per character. `right` adds one
//           character per step; if that character was last seen inside the window,
//           `left` jumps straight past that position (no inner loop).
// Time O(n), space O(1) -- a fixed 256-entry array

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int last[256];
        fill(begin(last), end(last), -1);
        int longest_streak = 0;
        int left = 0;

        for(int right = 0; right < size(s); right++)
        {
            unsigned char c = s[right];
            if (last[c] >= left) 
            {
                left = last[c] + 1;
            }
            last[c] = right;
            longest_streak = max(longest_streak, right - left + 1);        }

        return longest_streak;
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

TEST(a_repeat_keeps_the_characters_after_it) {
    // at the second 'a' the window becomes "bca", not "a"
    CHECK((lengthOfLongestSubstring("abcad") == 4));
}

TEST(the_answer_spans_the_repeated_character) {
    // "vdf": the second 'd' only evicts the first 'd', 'v' stays
    CHECK((lengthOfLongestSubstring("dvdf") == 3));
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
