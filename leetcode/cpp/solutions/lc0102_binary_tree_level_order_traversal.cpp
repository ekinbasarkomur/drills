// 102. Binary Tree Level Order Traversal · Medium · https://leetcode.com/problems/binary-tree-level-order-traversal/
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* root = build_tree({3, 9, 20, nullopt, nullopt, 15, 7});
    CHECK_EQ(Solution().levelOrder(root), (vector<vector<int>>{{3}, {9, 20}, {15, 7}}));
}

TEST(example_2) {
    TreeNode* root = build_tree({1});
    CHECK_EQ(Solution().levelOrder(root), (vector<vector<int>>{{1}}));
}

TEST(example_3) {
    TreeNode* root = build_tree({});
    CHECK_EQ(Solution().levelOrder(root), (vector<vector<int>>{}));
}
