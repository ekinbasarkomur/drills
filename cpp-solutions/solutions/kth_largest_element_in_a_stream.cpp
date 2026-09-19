// 703. Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/
//
// Problem: add() appends to the stream and returns the kth largest value seen
//          so far. Duplicates count separately: the 2nd largest of [1,2,3,3]
//          is 3.
// Note: you never need the whole stream -- only the k largest values, and of
//       those only the smallest is ever the answer.
// Approach:
// Time O(?) per add, space O(?)

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>

#include "test.hpp"

using namespace std;

class KthLargest {
public:
    KthLargest(int k, vector<int> &nums) {
        (void)k;
        (void)nums; // TODO
    }

    int add(int val) {
        (void)val;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests

using vi = vector<int>;

TEST(example_1) {
    vi nums{1, 2, 3, 3};
    KthLargest s(3, nums);
    CHECK((s.add(3) == 3));
    CHECK((s.add(5) == 3));
    CHECK((s.add(6) == 3));
    CHECK((s.add(7) == 5));
    CHECK((s.add(8) == 6));
}

TEST(k_is_one_means_the_running_maximum) {
    vi nums{};
    KthLargest s(1, nums);
    CHECK((s.add(5) == 5));
    CHECK((s.add(3) == 5));
    CHECK((s.add(9) == 9));
}

TEST(stream_starts_empty) {
    vi nums{};
    KthLargest s(2, nums);
    s.add(1);
    CHECK((s.add(2) == 1));
    CHECK((s.add(3) == 2));
}

TEST(initial_array_already_holds_k_values) {
    vi nums{4, 5, 8, 2};
    KthLargest s(3, nums);
    CHECK((s.add(3) == 4));
    CHECK((s.add(5) == 5));
    CHECK((s.add(10) == 5));
    CHECK((s.add(9) == 8));
}

TEST(duplicates_count_separately) {
    vi nums{3, 3};
    KthLargest s(2, nums);
    CHECK((s.add(3) == 3));
    CHECK((s.add(4) == 3));
}

TEST(everything_added_is_smaller) {
    vi nums{10, 20, 30};
    KthLargest s(2, nums);
    CHECK((s.add(1) == 20));
    CHECK((s.add(2) == 20));
}

TEST(negative_values) {
    vi nums{-5, -3, -1};
    KthLargest s(2, nums);
    CHECK((s.add(-4) == -3));
    CHECK((s.add(0) == -1));
}

TEST(all_values_equal) {
    vi nums{7, 7, 7};
    KthLargest s(3, nums);
    CHECK((s.add(7) == 7));
    CHECK((s.add(8) == 7));
}

TEST(value_range_extremes) {
    vi nums{-1000, 1000};
    KthLargest s(2, nums);
    CHECK((s.add(0) == 0));
    CHECK((s.add(1000) == 1000));
}

TEST(k_equals_the_stream_length) {
    vi nums{1, 2};
    KthLargest s(3, nums);
    CHECK((s.add(3) == 1));
    CHECK((s.add(4) == 2));
}

TEST(many_operations) {
    // 1000 values in, k = 1000: the answer is always the running minimum
    // once the stream is long enough.
    vi nums{};
    KthLargest s(1000, nums);
    int last = 0;
    for (int i = 1000; i >= 1; --i)
        last = s.add(i);
    CHECK((last == 1));
}
