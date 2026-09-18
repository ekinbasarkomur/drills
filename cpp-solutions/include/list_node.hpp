// Shared singly-linked-list node plus helpers, so linked-list problems can be
// written the way LeetCode presents them while the tests stay readable.
//
//   build({1,2,3})    -> a list, returns its head (nullptr for {})
//   to_vector(head)   -> the values, for comparing against an expected vector
//   free_list(head)   -> delete every node (not for lists with a cycle)
#pragma once

#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

inline ListNode *build(const std::vector<int> &values) {
    ListNode dummy;
    ListNode *tail = &dummy;
    for (int v : values) {
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

inline std::vector<int> to_vector(ListNode *head) {
    std::vector<int> out;
    for (ListNode *p = head; p; p = p->next)
        out.push_back(p->val);
    return out;
}

inline void free_list(ListNode *head) {
    while (head) {
        ListNode *next = head->next;
        delete head;
        head = next;
    }
}
