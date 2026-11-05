// 208. Implement Trie (Prefix Tree) · Medium · https://leetcode.com/problems/implement-trie-prefix-tree/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Trie {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    fn new() -> Self {
        todo!()
    }
    
    fn insert(&self, word: String) {
        todo!()
    }
    
    fn search(&self, word: String) -> bool {
        todo!()
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        todo!()
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Trie::new();
        obj.insert("apple".to_string());
        check_eq!(obj.search("apple".to_string()), true);
        check_eq!(obj.search("app".to_string()), false);
        check_eq!(obj.starts_with("app".to_string()), true);
        obj.insert("app".to_string());
        check_eq!(obj.search("app".to_string()), true);
    }
}
