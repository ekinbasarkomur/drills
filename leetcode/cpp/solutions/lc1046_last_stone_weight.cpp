// 1046. Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/
// Plan: Aşama 0 · Heap & Priority Queue
//
// Problem: repeatedly smash the two heaviest stones together. Equal weights
//          destroy each other; otherwise the difference goes back in. Return
//          what is left, or 0.
// Note: You need the two largest values over and over, and the result goes
//       straight back into the pool -- that is a max-heap, not a sort.
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    int lastStoneWeight(vector<int> &stones) {
        (void)stones;
        return 0; // TODO
    }
};
// ---------------------------------------------------------------- tests
// lastStoneWeight takes a non-const reference, so it cannot be handed a temporary.

static int lastStoneWeight(vector<int> stones) {
    return Solution().lastStoneWeight(stones);
}

TEST(example_1) { CHECK((lastStoneWeight({2, 3, 6, 2, 4}) == 1)); }

TEST(example_2) { CHECK((lastStoneWeight({1, 2}) == 1)); }

TEST(no_stones) { CHECK((lastStoneWeight({}) == 0)); }

TEST(one_stone_survives_untouched) { CHECK((lastStoneWeight({7}) == 7)); }

TEST(two_equal_stones_annihilate) { CHECK((lastStoneWeight({1, 1}) == 0)); }

TEST(two_equal_heavy_stones) { CHECK((lastStoneWeight({3, 3}) == 0)); }

TEST(the_classic_leetcode_case) {
    CHECK((lastStoneWeight({2, 7, 4, 1, 8, 1}) == 1));
}

TEST(a_tie_then_a_leftover) {
    // the two 10s cancel, leaving 4 and 2
    CHECK((lastStoneWeight({10, 4, 2, 10}) == 2));
}

TEST(odd_count_of_equal_stones) { CHECK((lastStoneWeight({1, 1, 1}) == 1)); }

TEST(value_range_extremes) {
    CHECK((lastStoneWeight({1000, 1000, 1000}) == 1000));
}

TEST(largest_allowed_input) {
    // 1000 stones of equal weight: they pair off and cancel completely.
    vector<int> stones(1000, 1000);
    CHECK((lastStoneWeight(stones) == 0));
}
