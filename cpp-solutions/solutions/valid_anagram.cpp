// 242. Valid Anagram           https://leetcode.com/problems/valid-anagram/
//
// Problem: return true if t is a rearrangement of s.
// Approach: lengths must match first -- the single loop that follows indexes
//           both strings at once and relies on it. Then count how often each
//           char occurs in each string and compare the two count maps.
//           Time O(n), space O(n).

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (size_t i = 0; i < s.size(); i++) {
            s_map[s[i]]++;
            t_map[t[i]]++;
        }

        return s_map == t_map;
    }
};

// ---------------------------------------------------------------- tests

static bool isAnagram(string s, string t) { return Solution().isAnagram(s, t); }

TEST(example_1) { CHECK(isAnagram("racecar", "carrace")); }

TEST(example_2) { CHECK(!isAnagram("jar", "jam")); }

TEST(example_3) { CHECK(isAnagram("x", "x")); }

TEST(different_lengths) { CHECK(!isAnagram("ab", "abc")); }

TEST(same_letters_different_counts) { CHECK(!isAnagram("aab", "abb")); }

TEST(identical_strings) { CHECK(isAnagram("anagram", "anagram")); }

TEST(no_letters_in_common) { CHECK(!isAnagram("abc", "xyz")); }
