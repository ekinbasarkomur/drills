// 100. Same Tree · Easy · https://leetcode.com/problems/same-tree/
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

TEST(example_1) {
    TreeNode* p = build_tree({1, 2, 3});
    TreeNode* q = build_tree({1, 2, 3});
    CHECK_EQ(Solution().isSameTree(p, q), true);
}

TEST(example_2) {
    TreeNode* p = build_tree({1, 2});
    TreeNode* q = build_tree({1, nullopt, 2});
    CHECK_EQ(Solution().isSameTree(p, q), false);
}

TEST(example_3) {
    TreeNode* p = build_tree({1, 2, 1});
    TreeNode* q = build_tree({1, 1, 2});
    CHECK_EQ(Solution().isSameTree(p, q), false);
}
