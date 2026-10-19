// 332. Reconstruct Itinerary · Hard · https://leetcode.com/problems/reconstruct-itinerary/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<vector<string>> tickets = vector<vector<string>>{{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
    CHECK_EQ(Solution().findItinerary(tickets), (vector<string>{"JFK", "MUC", "LHR", "SFO", "SJC"}));
}

TEST(example_2) {
    vector<vector<string>> tickets = vector<vector<string>>{{"JFK", "SFO"}, {"JFK", "ATL"}, {"SFO", "ATL"}, {"ATL", "JFK"}, {"ATL", "SFO"}};
    CHECK_EQ(Solution().findItinerary(tickets), (vector<string>{"JFK", "ATL", "JFK", "SFO", "ATL", "SFO"}));
}
