// 543. Diameter of Binary Tree · Easy · https://leetcode.com/problems/diameter-of-binary-tree/
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
    int diameterOfBinaryTree(TreeNode* root) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* root = build_tree({1, 2, 3, 4, 5});
    CHECK_EQ(Solution().diameterOfBinaryTree(root), 3);
}

TEST(example_2) {
    TreeNode* root = build_tree({1, 2});
    CHECK_EQ(Solution().diameterOfBinaryTree(root), 1);
}
