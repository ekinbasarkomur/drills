// 271. Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/
//
// Problem: turn a list of strings into ONE string, and turn it back. The strings
//          may contain any ASCII character -- including whatever separator you
//          were about to reach for.
// Approach: prefix each string with its length and a '#'. Decoding reads the
//           length, then takes exactly that many characters -- it never
//           searches for a separator, so a '#' inside the payload is harmless.
// Time O(n), space O(n)

#include <iostream>
#include <string>
#include <vector>

#include "test.hpp"

using namespace std;

std::string encode(const std::vector<std::string> &strs) {
    string encoded_string = "";

    for (const string &str : strs) {
        encoded_string += to_string(size(str)) + "#" + str;
    }

    return encoded_string;
}

std::vector<std::string> decode(const std::string &s) {
    vector<string> output;

    size_t pos = 0;
    while (pos < s.size()) {
        size_t hash = s.find('#', pos);          // where the length header ends
        int len = stoi(s.substr(pos, hash - pos));

        output.push_back(s.substr(hash + 1, len));

        pos = hash + 1 + len;                    // skip past the payload too
    }

    return output;
}

// ---------------------------------------------------------------- tests
// The encoding format is yours to choose, so the tests never look at the
// encoded string. They only check that decode(encode(x)) == x.

using vs = std::vector<std::string>;

static void roundtrip(const vs &original) {
    CHECK_EQ(decode(encode(original)), original);
}

TEST(example_1) { roundtrip({"Hello", "World"}); }

TEST(example_2) { roundtrip({""}); }

TEST(empty_list) { roundtrip({}); }

TEST(several_empty_strings) { roundtrip({"", "", ""}); }

TEST(empty_string_between_real_ones) { roundtrip({"a", "", "b"}); }

TEST(single_string) { roundtrip({"lonely"}); }

// The interesting cases: the payload contains whatever you picked as a
// separator, or text that looks like your own length header.

TEST(payload_contains_hash) { roundtrip({"a#b", "#", "##"}); }

TEST(payload_looks_like_a_length_header) { roundtrip({"3#abc", "12#", "0#"}); }

TEST(payload_contains_digits_and_punctuation) {
    roundtrip({"123", ",", ";", "|", ":", "\\"});
}

TEST(payload_contains_whitespace_and_newlines) {
    roundtrip({"a b", "\n", "\t\t", " ", "line1\nline2"});
}

TEST(long_strings_at_the_length_limit) {
    roundtrip({std::string(199, 'x'), std::string(199, '#')});
}

TEST(many_strings) {
    vs items;
    for (int i = 0; i < 99; ++i)
        items.push_back("item" + std::to_string(i));
    roundtrip(items);
}
