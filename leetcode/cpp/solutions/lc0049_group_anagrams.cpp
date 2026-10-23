// 49. Group Anagrams           https://leetcode.com/problems/group-anagrams/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: bucket the input strings so that anagrams end up in the same sublist.
// Approach: two words are anagrams exactly when their sorted letters match, so
//           the sorted string is a canonical key. operator[] default-constructs
//           the vector on first use, then the buckets are copied out.
//           Time O(n * k log k) for n words of length k, space O(n * k).

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs) {
        vector<vector<string>> output;
        unordered_map<string, vector<string>> sorted_strings;

        for (string &str : strs) {

            string sorted_string = str;
            sort(sorted_string.begin(), sorted_string.end());
            sorted_strings[sorted_string].push_back(str);
        }

        for (auto &[sorted_string, arr] : sorted_strings) {
            (void)sorted_string;
            output.push_back(arr);
        }

        return output;
    }

};
// ---------------------------------------------------------------- tests
// The output may come back in any order, so sort both levels before comparing.

using vs = vector<string>;
using vvs = vector<vector<string>>;

static vvs normalized(vvs groups) {
    for (auto &g : groups)
        sort(g.begin(), g.end());
    sort(groups.begin(), groups.end());
    return groups;
}

static vvs got(vs input) { return normalized(Solution().groupAnagrams(input)); }

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
