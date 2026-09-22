// 104. Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/
//
// Problem: the number of nodes along the longest root-to-leaf path.
//          An empty tree has depth 0, a single node has depth 1.
// Approach:
// Time O(?), space O(?)

#include <algorithm>
#include <iostream>
#include <optional>
#include <queue>
#include <vector>

#include "test.hpp"
#include "tree_node.hpp"

using namespace std;

class Solution {
public:
    int maxDepth(TreeNode *root) {
        (void)root;
        return 0; // TODO
    }
};

// ---------------------------------------------------------------- tests
// Trees are written in level order; nullopt marks a missing child.

static int depth(const Level &values) {
    TreeNode *root = build_tree(values);
    int result = Solution().maxDepth(root);
    free_tree(root);
    return result;
}

static const optional<int> X = nullopt;

TEST(example_1) { CHECK((depth({1, 2, 3, X, X, 4}) == 3)); }

TEST(example_2) { CHECK((depth({}) == 0)); }

TEST(single_node) { CHECK((depth({1}) == 1)); }

TEST(two_levels_full) { CHECK((depth({1, 2, 3}) == 2)); }

TEST(only_a_left_child) { CHECK((depth({1, 2}) == 2)); }

TEST(only_a_right_child) { CHECK((depth({1, X, 2}) == 2)); }

TEST(a_left_leaning_chain) { CHECK((depth({1, 2, X, 3, X, 4}) == 4)); }

TEST(a_right_leaning_chain) { CHECK((depth({1, X, 2, X, 3, X, 4}) == 4)); }

TEST(the_deep_side_is_on_the_right) {
    CHECK((depth({1, 2, 3, X, X, 4, 5, 6}) == 4));
}

TEST(a_full_tree_of_three_levels) {
    CHECK((depth({1, 2, 3, 4, 5, 6, 7}) == 3));
}

TEST(largest_allowed_input) {
    // 100 nodes in a single chain, the constraint's ceiling.
    Level values;
    for (int i = 0; i < 100; ++i) {
        values.push_back(i);
        if (i < 99)
            values.push_back(X);
    }
    CHECK((depth(values) == 100));
}
