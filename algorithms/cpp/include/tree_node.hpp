// Shared binary-tree node plus helpers.
//
//   build_tree({1,2,3,nullopt,4})  -> level-order, nullopt = missing child
//   to_level_order(root)           -> back to that representation, trailing
//                                     nullopts trimmed
//   free_tree(root)                -> delete every node
#pragma once

#include <optional>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *l, TreeNode *r) : val(x), left(l), right(r) {}
};

using Level = std::vector<std::optional<int>>;

inline TreeNode *build_tree(const Level &values) {
    if (values.empty() || !values[0].has_value())
        return nullptr;

    TreeNode *root = new TreeNode(*values[0]);
    std::queue<TreeNode *> q;
    q.push(root);

    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        TreeNode *node = q.front();
        q.pop();

        if (i < values.size()) {
            if (values[i].has_value()) {
                node->left = new TreeNode(*values[i]);
                q.push(node->left);
            }
            ++i;
        }
        if (i < values.size()) {
            if (values[i].has_value()) {
                node->right = new TreeNode(*values[i]);
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}

inline Level to_level_order(TreeNode *root) {
    Level out;
    if (!root)
        return out;

    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode *node = q.front();
        q.pop();
        if (!node) {
            out.push_back(std::nullopt);
            continue;
        }
        out.push_back(node->val);
        q.push(node->left);
        q.push(node->right);
    }
    while (!out.empty() && !out.back().has_value())
        out.pop_back();
    return out;
}

inline void free_tree(TreeNode *root) {
    if (!root)
        return;
    free_tree(root->left);
    free_tree(root->right);
    delete root;
}
