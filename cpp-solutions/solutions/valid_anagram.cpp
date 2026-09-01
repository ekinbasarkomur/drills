// 242. Valid Anagram           https://leetcode.com/problems/valid-anagram/
//
// Problem: return true if t is a rearrangement of s.
// Approach:
// Time O(?), space O(?)

#include <string>

#include "test.hpp"

bool isAnagram(const std::string &s, const std::string &t) {
    (void)s;
    (void)t;
    return false;  // TODO
}

// ---------------------------------------------------------------- tests

TEST(example_1) { CHECK(isAnagram("racecar", "carrace")); }

TEST(example_2) { CHECK(!isAnagram("jar", "jam")); }

TEST(example_3) { CHECK(isAnagram("x", "x")); }

TEST(different_lengths) { CHECK(!isAnagram("ab", "abc")); }

TEST(same_letters_different_counts) { CHECK(!isAnagram("aab", "abb")); }

TEST(identical_strings) { CHECK(isAnagram("anagram", "anagram")); }

TEST(no_letters_in_common) { CHECK(!isAnagram("abc", "xyz")); }
