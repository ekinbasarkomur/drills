// 141. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/
//
// Problem: does following next ever revisit a node?
// Note: the classic answer walks two pointers at different speeds. If there is
//       a loop, the fast one laps the slow one; if not, it runs off the end.
// Approach:
// Time O(?), space O(?)

#include <vector>

#include "list_node.hpp"
#include "test.hpp"

using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        (void)head;
        return false; // TODO
    }
};

// ---------------------------------------------------------------- tests
// A cycle is made by pointing the tail at the index-th node; index -1 means no
// cycle. The list is taken apart again afterwards so nothing leaks.

using vi = vector<int>;

static bool has_cycle(const vi &values, int index) {
    ListNode *head = build(values);
    ListNode *tail = head;
    while (tail && tail->next)
        tail = tail->next;

    ListNode *target = nullptr;
    if (index >= 0) {
        target = head;
        for (int i = 0; i < index; ++i)
            target = target->next;
        tail->next = target;
    }

    bool result = Solution().hasCycle(head);

    if (tail)
        tail->next = nullptr; // break the cycle before freeing
    free_list(head);
    return result;
}

TEST(example_1) { CHECK(has_cycle({1, 2, 3, 4}, 1)); }

TEST(example_2) { CHECK(!has_cycle({1, 2}, -1)); }

TEST(empty_list) { CHECK(!has_cycle({}, -1)); }

TEST(single_node_no_cycle) { CHECK(!has_cycle({1}, -1)); }

TEST(single_node_pointing_at_itself) { CHECK(has_cycle({1}, 0)); }

TEST(two_nodes_no_cycle) { CHECK(!has_cycle({1, 2}, -1)); }

TEST(cycle_covers_the_whole_list) { CHECK(has_cycle({1, 2, 3}, 0)); }

TEST(cycle_is_just_the_last_node) { CHECK(has_cycle({1, 2, 3}, 2)); }

TEST(repeated_values_are_not_a_cycle) {
    // equal values are not the same node
    CHECK(!has_cycle({1, 1, 1, 1}, -1));
}

TEST(long_list_no_cycle) {
    vi values(1000);
    for (int i = 0; i < 1000; ++i)
        values[i] = i;
    CHECK(!has_cycle(values, -1));
}

TEST(long_list_with_a_late_cycle) {
    vi values(1000);
    for (int i = 0; i < 1000; ++i)
        values[i] = i;
    CHECK(has_cycle(values, 999));
}
