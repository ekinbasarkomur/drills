// 1244. Design A Leaderboard · Medium · https://leetcode.com/problems/design-a-leaderboard/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Leaderboard {
public:
    Leaderboard() {
        TODO();
    }
    
    void addScore(int playerId, int score) {
        TODO();
    }
    
    int top(int K) {
        TODO();
    }
    
    void reset(int playerId) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    // Premium problem: the expected output is not public, so this only runs it.
    Leaderboard *obj = new Leaderboard();
    obj->addScore(1, 73);
    obj->addScore(2, 56);
    obj->addScore(3, 39);
    obj->addScore(4, 51);
    obj->addScore(5, 4);
    obj->top(1);
    obj->reset(1);
    obj->reset(2);
    obj->addScore(2, 51);
    obj->top(3);
}
