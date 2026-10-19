// 166. Fraction to Recurring Decimal · Medium · https://leetcode.com/problems/fraction-to-recurring-decimal/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int numerator = 1;
    int denominator = 2;
    CHECK_EQ(Solution().fractionToDecimal(numerator, denominator), (string("0.5")));
}

TEST(example_2) {
    int numerator = 2;
    int denominator = 1;
    CHECK_EQ(Solution().fractionToDecimal(numerator, denominator), (string("2")));
}

TEST(example_3) {
    int numerator = 4;
    int denominator = 333;
    CHECK_EQ(Solution().fractionToDecimal(numerator, denominator), (string("0.(012)")));
}
