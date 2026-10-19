// 98. Validate Binary Search Tree · Medium · https://leetcode.com/problems/validate-binary-search-tree/
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
    bool isValidBST(TreeNode* root) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* root = build_tree({2, 1, 3});
    CHECK_EQ(Solution().isValidBST(root), true);
}

TEST(example_2) {
    TreeNode* root = build_tree({5, 1, 4, nullopt, nullopt, 3, 6});
    CHECK_EQ(Solution().isValidBST(root), false);
}
