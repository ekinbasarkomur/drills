// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/
//
// Problem: mirror the tree -- every node's left and right swap, all the way
//          down -- and return the root.
// Approach:
// Time O(?), space O(?)

#include <iostream>
#include <optional>
#include <queue>
#include <vector>

#include "test.hpp"
#include "tree_node.hpp"

using namespace std;

class Solution {
public:
    TreeNode *invertTree(TreeNode *root) {
        return root; // TODO
    }
};

// ---------------------------------------------------------------- tests
// Trees are written in level order; nullopt marks a missing child.

static Level inverted(const Level &values) {
    TreeNode *root = Solution().invertTree(build_tree(values));
    Level out = to_level_order(root);
    free_tree(root);
    return out;
}

static const optional<int> X = nullopt;

TEST(example_1) {
    CHECK_EQ(inverted({1, 2, 3, 4, 5, 6, 7}), (Level{1, 3, 2, 7, 6, 5, 4}));
}

TEST(example_2) { CHECK_EQ(inverted({3, 2, 1}), (Level{3, 1, 2})); }

TEST(example_3) { CHECK_EQ(inverted({}), (Level{})); }

TEST(single_node) { CHECK_EQ(inverted({1}), (Level{1})); }

TEST(only_a_left_child) { CHECK_EQ(inverted({1, 2}), (Level{1, X, 2})); }

TEST(only_a_right_child) { CHECK_EQ(inverted({1, X, 2}), (Level{1, 2})); }

TEST(a_left_leaning_chain_becomes_right_leaning) {
    CHECK_EQ(inverted({1, 2, X, 3}), (Level{1, X, 2, X, 3}));
}

TEST(lopsided_tree) {
    CHECK_EQ(inverted({1, 2, 3, X, 4}), (Level{1, 3, 2, X, X, 4}));
}

TEST(negative_values) { CHECK_EQ(inverted({-1, -2, -3}), (Level{-1, -3, -2})); }

TEST(inverting_twice_restores_the_original) {
    Level original = {1, 2, 3, 4, 5, 6, 7};
    CHECK_EQ(inverted(inverted(original)), original);
}

TEST(a_symmetric_tree_is_unchanged) {
    CHECK_EQ(inverted({1, 2, 2}), (Level{1, 2, 2}));
}
