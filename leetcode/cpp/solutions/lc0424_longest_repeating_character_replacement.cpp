// 424. Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/
// Plan: Aşama 0 · Sliding Window
//
// Problem: after replacing at most k characters of s with any uppercase
//          letter, how long can a run of one single letter get?
// Note: A window is usable when (its length - the count of its most common
//       letter) <= k: that difference is how many replacements it costs.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int characterReplacement(string s, int k) {
        (void)s;
        (void)k;
        return 0; // TODO
    }
};
// ---------------------------------------------------------------- tests

static int characterReplacement(string s, int k) {
    return Solution().characterReplacement(s, k);
}

TEST(example_1) {
    // replace both X's with Y's, or the other way round
    CHECK((characterReplacement("XYYX", 2) == 4));
}

TEST(example_2) { CHECK((characterReplacement("AAABABB", 1) == 5)); }

TEST(single_character_no_budget) { CHECK((characterReplacement("A", 0) == 1)); }

TEST(single_character_with_budget) {
    // k can exceed what is useful
    CHECK((characterReplacement("A", 1) == 1));
}

TEST(two_letters_no_budget) { CHECK((characterReplacement("AB", 0) == 1)); }

TEST(two_letters_one_replacement) {
    CHECK((characterReplacement("AB", 1) == 2));
}

TEST(already_uniform) {
    // nothing to replace
    CHECK((characterReplacement("BBBB", 0) == 4));
}

TEST(all_distinct_no_budget) { CHECK((characterReplacement("ABCDE", 0) == 1)); }

TEST(all_distinct_budget_covers_everything) {
    CHECK((characterReplacement("ABCDE", 4) == 5));
}

TEST(budget_larger_than_needed) {
    CHECK((characterReplacement("AAAA", 2) == 4));
}

TEST(one_odd_letter_at_the_front) {
    CHECK((characterReplacement("ABBB", 0) == 3));
}

TEST(the_window_must_shrink) {
    CHECK((characterReplacement("AABABBA", 1) == 4));
}

TEST(alternating_letters) { CHECK((characterReplacement("ABAB", 2) == 4)); }

TEST(largest_allowed_input) {
    // 100_000 A's and k = 0: the whole string already qualifies.
    // An O(n^2) solution will hang here rather than fail.
    string s(100000, 'A');
    CHECK((characterReplacement(s, 0) == 100000));
}
