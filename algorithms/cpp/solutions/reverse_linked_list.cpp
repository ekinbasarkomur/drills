// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
//
// Problem: reverse a singly linked list and return the new head.
// Note: you only get one pointer per node, so you must hold onto the next node
//       before you overwrite it -- three pointers is the usual dance.
// Approach: walk the list once, turning each node's `next` around to point at
//           the node before it. Three pointers: prev, curr, and next (saved
//           before curr->next is overwritten).
// Time O(n), space O(1)

#include <iostream>
#include <vector>

#include "list_node.hpp"
#include "test.hpp"

using namespace std;

class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        ListNode *prev = nullptr;
        ListNode *curr = head;

        while (curr != nullptr) {
            ListNode *next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};

// ---------------------------------------------------------------- tests

using vi = vector<int>;

static vi reversed(const vi &values) {
    ListNode *head = Solution().reverseList(build(values));
    vi out = to_vector(head);
    free_list(head);
    return out;
}

TEST(example_1) { CHECK_EQ(reversed({0, 1, 2, 3}), (vi{3, 2, 1, 0})); }

TEST(example_2) { CHECK_EQ(reversed({}), (vi{})); }

TEST(single_node) { CHECK_EQ(reversed({7}), (vi{7})); }

TEST(two_nodes) { CHECK_EQ(reversed({1, 2}), (vi{2, 1})); }

TEST(repeated_values) { CHECK_EQ(reversed({5, 5, 5}), (vi{5, 5, 5})); }

TEST(negative_values) { CHECK_EQ(reversed({-1, -2, -3}), (vi{-3, -2, -1})); }

TEST(value_range_extremes) {
    CHECK_EQ(reversed({-1000, 0, 1000}), (vi{1000, 0, -1000}));
}

TEST(largest_allowed_input) {
    // 1000 nodes, the constraint's ceiling.
    vi values(1000);
    for (int i = 0; i < 1000; ++i)
        values[i] = i;
    vi expected(1000);
    for (int i = 0; i < 1000; ++i)
        expected[i] = 999 - i;
    CHECK_EQ(reversed(values), expected);
}
