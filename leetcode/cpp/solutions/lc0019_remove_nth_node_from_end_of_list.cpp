// 19. Remove Nth Node From End of List · Medium · https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Plan: Aşama 0 · Linked List
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    ListNode* head = build({1, 2, 3, 4, 5});
    int n = 2;
    CHECK_EQ(to_vector(Solution().removeNthFromEnd(head, n)), (vector<int>{1, 2, 3, 5}));
}

TEST(example_2) {
    ListNode* head = build({1});
    int n = 1;
    CHECK_EQ(to_vector(Solution().removeNthFromEnd(head, n)), (vector<int>{}));
}

TEST(example_3) {
    ListNode* head = build({1, 2});
    int n = 1;
    CHECK_EQ(to_vector(Solution().removeNthFromEnd(head, n)), (vector<int>{1}));
}
