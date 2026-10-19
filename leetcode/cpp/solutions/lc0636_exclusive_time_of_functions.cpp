// 636. Exclusive Time of Functions · Medium · https://leetcode.com/problems/exclusive-time-of-functions/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    int n = 2;
    vector<string> logs = vector<string>{"0:start:0", "1:start:2", "1:end:5", "0:end:6"};
    CHECK_EQ(Solution().exclusiveTime(n, logs), (vector<int>{3, 4}));
}

TEST(example_2) {
    int n = 1;
    vector<string> logs = vector<string>{"0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"};
    CHECK_EQ(Solution().exclusiveTime(n, logs), (vector<int>{8}));
}

TEST(example_3) {
    int n = 2;
    vector<string> logs = vector<string>{"0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"};
    CHECK_EQ(Solution().exclusiveTime(n, logs), (vector<int>{7, 1}));
}
