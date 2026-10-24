// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Plan: Aşama 0 · Sliding Window
//
// Problem: length of the longest contiguous stretch of s in which no
//          character repeats. s may contain any printable ASCII.
// Note: A window that only ever grows from the right and shrinks from the
//       left visits each character twice at most.
// Approach: sliding window. `right` adds one character per step; when it is
//           already in the window, `left` drops characters until it is not.
//           Each character enters and leaves the set at most once.
// Time O(n), space O(min(n, 95)) -- at most 95 printable ASCII characters

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> ss;
        int longest_streak = 0;
        int left = 0;

        for(int right = 0; right < size(s); right++)
        {
            while(ss.contains(s[right]))
            {
                ss.erase(s[left]);
                left++;
            }

            ss.insert(s[right]);
            longest_streak = max(longest_streak, (int)size(ss));
        }

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
