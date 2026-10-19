// 23. Merge k Sorted Lists · Hard · https://leetcode.com/problems/merge-k-sorted-lists/
// Plan: Aşama 2 · Data Stream ve Heap
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    vector<ListNode*> lists = vector<ListNode*>{build({1, 4, 5}), build({1, 3, 4}), build({2, 6})};
    CHECK_EQ(to_vector(Solution().mergeKLists(lists)), (vector<int>{1, 1, 2, 3, 4, 4, 5, 6}));
}

TEST(example_2) {
    vector<ListNode*> lists = vector<ListNode*>{};
    CHECK_EQ(to_vector(Solution().mergeKLists(lists)), (vector<int>{}));
}

TEST(example_3) {
    vector<ListNode*> lists = vector<ListNode*>{build({})};
    CHECK_EQ(to_vector(Solution().mergeKLists(lists)), (vector<int>{}));
}
