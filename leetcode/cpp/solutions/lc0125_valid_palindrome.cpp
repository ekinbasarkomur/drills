// 125. Valid Palindrome        https://leetcode.com/problems/valid-palindrome/
// Plan: Aşama 0 · Two Pointers
//
// Problem: is s a palindrome, ignoring case and every non-alphanumeric
//          character? Input is printable ASCII.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
bool isPalindrome(const std::string &s) {
    vector<char> clean;

    for (auto i = s.begin(); i != s.end(); i++) {

        if (isalnum(*i)) {
            clean.push_back(tolower(*i));
        }
    }

    if (size(clean) == 0) {
        return true;
    }

    int left = 0;
    int right = size(clean) - 1;

    while (right > left) {
        if (clean[left] != clean[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}
// ---------------------------------------------------------------- tests

TEST(example_1) { CHECK(isPalindrome("Was it a car or a cat I saw?")); }

TEST(example_2) { CHECK(!isPalindrome("tab a cat")); }

TEST(single_character) { CHECK(isPalindrome("a")); }

TEST(two_identical_characters) { CHECK(isPalindrome("aa")); }

TEST(two_different_characters) { CHECK(!isPalindrome("ab")); }

TEST(nothing_alphanumeric_at_all) {
    // everything is stripped, an empty string is a palindrome
    CHECK(isPalindrome(".,!?"));
    CHECK(isPalindrome(" "));
}

TEST(punctuation_between_the_letters) {
    CHECK(isPalindrome("A man, a plan, a canal: Panama"));
}

TEST(digits_count_as_alphanumeric) {
    CHECK(isPalindrome("12321"));
    CHECK(!isPalindrome("12345"));
}

TEST(letters_and_digits_together) { CHECK(isPalindrome("1a2a1")); }

TEST(digit_against_letter_is_not_equal) {
    // the classic trap: '0' and 'P' are 32 apart in ASCII, like 'a' and 'A'
    CHECK(!isPalindrome("0P"));
}

TEST(case_is_ignored) {
    CHECK(isPalindrome("Aa"));
    CHECK(isPalindrome("RaceCar"));
}

TEST(odd_length_ignores_the_middle_character) {
    CHECK(isPalindrome("aba"));
    CHECK(isPalindrome("abXba"));
}

TEST(even_length_has_no_free_middle) {
    CHECK(isPalindrome("abba"));
    CHECK(!isPalindrome("abca"));
}

TEST(difference_only_at_the_very_ends) {
    CHECK(!isPalindrome("abcdefghijklmnopqrstuvwxyZ"));
}

TEST(long_palindrome_at_the_length_limit) {
    std::string half;
    for (int i = 0; i < 100; ++i)
        half += "abcde"; // 500 chars
    std::string reversed(half.rbegin(), half.rend());
    CHECK(isPalindrome(half + reversed));
}
