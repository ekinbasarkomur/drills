// 208. Implement Trie (Prefix Tree) · Medium · https://leetcode.com/problems/implement-trie-prefix-tree/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Trie {
public:
    Trie() {
        TODO();
    }
    
    void insert(string word) {
        TODO();
    }
    
    bool search(string word) {
        TODO();
    }
    
    bool startsWith(string prefix) {
        TODO();
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    Trie *obj = new Trie();
    obj->insert("apple");
    CHECK_EQ(obj->search("apple"), true);
    CHECK_EQ(obj->search("app"), false);
    CHECK_EQ(obj->startsWith("app"), true);
    obj->insert("app");
    CHECK_EQ(obj->search("app"), true);
}
