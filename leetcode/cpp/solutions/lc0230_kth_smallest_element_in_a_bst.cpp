// 230. Kth Smallest Element in a BST · Medium · https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// Plan: Aşama 0 · Trees
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* root = build_tree({3, 1, 4, nullopt, 2});
    int k = 1;
    CHECK_EQ(Solution().kthSmallest(root, k), 1);
}

TEST(example_2) {
    TreeNode* root = build_tree({5, 3, 6, 2, 4, nullopt, nullopt, 1});
    int k = 3;
    CHECK_EQ(Solution().kthSmallest(root, k), 3);
}
