// 49. Group Anagrams           https://leetcode.com/problems/group-anagrams/
//
// Problem: bucket the input strings so that anagrams end up in the same sublist.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <string>
#include <vector>

#include "test.hpp"

std::vector<std::vector<std::string>> groupAnagrams(
    const std::vector<std::string> &strs) {
    (void)strs;
    return {};  // TODO
}

// ---------------------------------------------------------------- tests
// The output may come back in any order, so sort both levels before comparing.

using vs  = std::vector<std::string>;
using vvs = std::vector<std::vector<std::string>>;

static vvs normalized(vvs groups) {
    for (auto &g : groups) std::sort(g.begin(), g.end());
    std::sort(groups.begin(), groups.end());
    return groups;
}

static vvs got(const vs &input) { return normalized(groupAnagrams(input)); }

TEST(example_1) {
    CHECK_EQ(got({"act", "pots", "tops", "cat", "stop", "hat"}),
             normalized({{"hat"}, {"act", "cat"}, {"stop", "pots", "tops"}}));
}

TEST(example_2) { CHECK_EQ(got({"x"}), normalized({{"x"}})); }

TEST(example_3) { CHECK_EQ(got({""}), normalized({{""}})); }

TEST(no_two_words_are_anagrams) {
    CHECK_EQ(got({"abc", "de", "f"}), normalized({{"abc"}, {"de"}, {"f"}}));
}

TEST(everything_in_one_group) {
    CHECK_EQ(got({"abc", "bca", "cab"}), normalized({{"abc", "bca", "cab"}}));
}

TEST(duplicates_stay_as_separate_entries) {
    CHECK_EQ(got({"ab", "ab", "ba"}), normalized({{"ab", "ab", "ba"}}));
}

TEST(repeated_letters_are_not_confused) {
    // same letter set, different counts -> different groups
    CHECK_EQ(got({"aab", "abb"}), normalized({{"aab"}, {"abb"}}));
}

TEST(several_empty_strings_group_together) {
    CHECK_EQ(got({"", "", "a"}), normalized({{"", ""}, {"a"}}));
}
