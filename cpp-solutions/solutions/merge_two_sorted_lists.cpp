// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/
//
// Problem: splice two sorted lists into one sorted list, reusing the nodes.
// Note: a dummy head node saves you from special-casing "which list has the
//       first element" before the loop even starts.
// Approach:
// Time O(?), space O(?)

#include <iostream>
#include <vector>

#include "list_node.hpp"
#include "test.hpp"

using namespace std;

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
        (void)list2;
        return list1; // TODO
    }
};

// ---------------------------------------------------------------- tests

using vi = vector<int>;

static vi merged(const vi &a, const vi &b) {
    ListNode *head = Solution().mergeTwoLists(build(a), build(b));
    vi out = to_vector(head);
    free_list(head);
    return out;
}

TEST(example_1) {
    CHECK_EQ(merged({1, 2, 4}, {1, 3, 5}), (vi{1, 1, 2, 3, 4, 5}));
}

TEST(example_2) { CHECK_EQ(merged({}, {1, 2}), (vi{1, 2})); }

TEST(example_3) { CHECK_EQ(merged({}, {}), (vi{})); }

TEST(first_list_empty) { CHECK_EQ(merged({}, {5}), (vi{5})); }

TEST(second_list_empty) { CHECK_EQ(merged({5}, {}), (vi{5})); }

TEST(one_list_entirely_precedes_the_other) {
    CHECK_EQ(merged({1, 2, 3}, {4, 5, 6}), (vi{1, 2, 3, 4, 5, 6}));
    CHECK_EQ(merged({4, 5, 6}, {1, 2, 3}), (vi{1, 2, 3, 4, 5, 6}));
}

TEST(perfectly_interleaved) {
    CHECK_EQ(merged({1, 3, 5}, {2, 4, 6}), (vi{1, 2, 3, 4, 5, 6}));
}

TEST(all_values_equal) { CHECK_EQ(merged({2, 2}, {2, 2}), (vi{2, 2, 2, 2})); }

TEST(very_different_lengths) {
    CHECK_EQ(merged({1}, {2, 3, 4, 5}), (vi{1, 2, 3, 4, 5}));
}

TEST(negative_values) {
    CHECK_EQ(merged({-5, -1}, {-3, 0}), (vi{-5, -3, -1, 0}));
}

TEST(value_range_extremes) {
    CHECK_EQ(merged({-100, 100}, {0}), (vi{-100, 0, 100}));
}

TEST(largest_allowed_input) {
    // 100 nodes each, the constraint's ceiling.
    vi a(100), b(100), expected(200);
    for (int i = 0; i < 100; ++i) {
        a[i] = i * 2;
        b[i] = i * 2 + 1;
    }
    for (int i = 0; i < 200; ++i)
        expected[i] = i;
    CHECK_EQ(merged(a, b), expected);
}
