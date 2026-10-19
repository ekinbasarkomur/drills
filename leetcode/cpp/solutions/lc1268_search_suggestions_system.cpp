// 1268. Search Suggestions System · Medium · https://leetcode.com/problems/search-suggestions-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<string> products = vector<string>{"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = string("mouse");
    CHECK_EQ(Solution().suggestedProducts(products, searchWord), (vector<vector<string>>{{"mobile", "moneypot", "monitor"}, {"mobile", "moneypot", "monitor"}, {"mouse", "mousepad"}, {"mouse", "mousepad"}, {"mouse", "mousepad"}}));
}

TEST(example_2) {
    vector<string> products = vector<string>{"havana"};
    string searchWord = string("havana");
    CHECK_EQ(Solution().suggestedProducts(products, searchWord), (vector<vector<string>>{{"havana"}, {"havana"}, {"havana"}, {"havana"}, {"havana"}, {"havana"}}));
}
