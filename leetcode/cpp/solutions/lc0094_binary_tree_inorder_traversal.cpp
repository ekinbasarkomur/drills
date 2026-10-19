// 94. Binary Tree Inorder Traversal · Easy · https://leetcode.com/problems/binary-tree-inorder-traversal/
// Plan: Aşama 2 · Tree
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
    vector<int> inorderTraversal(TreeNode* root) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* root = build_tree({1, nullopt, 2, 3});
    CHECK_EQ(Solution().inorderTraversal(root), (vector<int>{1, 3, 2}));
}

TEST(example_2) {
    TreeNode* root = build_tree({1, 2, 3, 4, 5, nullopt, 8, nullopt, nullopt, 6, 7, 9});
    CHECK_EQ(Solution().inorderTraversal(root), (vector<int>{4, 2, 6, 5, 7, 1, 3, 9, 8}));
}

TEST(example_3) {
    TreeNode* root = build_tree({});
    CHECK_EQ(Solution().inorderTraversal(root), (vector<int>{}));
}

TEST(example_4) {
    TreeNode* root = build_tree({1});
    CHECK_EQ(Solution().inorderTraversal(root), (vector<int>{1}));
}
