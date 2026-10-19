// 382. Linked List Random Node · Medium · https://leetcode.com/problems/linked-list-random-node/
// Plan: Aşama 5 · Olasılık ve Matematik
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
    Solution(ListNode* head) {
        TODO();
    }
    
    int getRandom() {
        TODO();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    ListNode* head = build({1, 2, 3});
    Solution *obj = new Solution(head);
    obj->getRandom();
    obj->getRandom();
    obj->getRandom();
    obj->getRandom();
    obj->getRandom();
}
