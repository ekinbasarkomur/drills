// 399. Evaluate Division · Medium · https://leetcode.com/problems/evaluate-division/
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
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<string>> equations = vector<vector<string>>{{"a", "b"}, {"b", "c"}};
    vector<double> values = vector<double>{2.0, 3.0};
    vector<vector<string>> queries = vector<vector<string>>{{"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}};
    CHECK(near(Solution().calcEquation(equations, values, queries), vector<double>{6.0, 0.5, -1.0, 1.0, -1.0}));
}

TEST(example_2) {
    vector<vector<string>> equations = vector<vector<string>>{{"a", "b"}, {"b", "c"}, {"bc", "cd"}};
    vector<double> values = vector<double>{1.5, 2.5, 5.0};
    vector<vector<string>> queries = vector<vector<string>>{{"a", "c"}, {"c", "b"}, {"bc", "cd"}, {"cd", "bc"}};
    CHECK(near(Solution().calcEquation(equations, values, queries), vector<double>{3.75, 0.4, 5.0, 0.2}));
}

TEST(example_3) {
    vector<vector<string>> equations = vector<vector<string>>{{"a", "b"}};
    vector<double> values = vector<double>{0.5};
    vector<vector<string>> queries = vector<vector<string>>{{"a", "b"}, {"b", "a"}, {"a", "c"}, {"x", "y"}};
    CHECK(near(Solution().calcEquation(equations, values, queries), vector<double>{0.5, 2.0, -1.0, -1.0}));
}
