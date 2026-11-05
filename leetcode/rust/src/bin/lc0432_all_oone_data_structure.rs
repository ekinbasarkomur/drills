// 432. All O`one Data Structure · Hard · https://leetcode.com/problems/all-oone-data-structure/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct AllOne {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {

    fn new() -> Self {
        todo!()
    }
    
    fn inc(&self, key: String) {
        todo!()
    }
    
    fn dec(&self, key: String) {
        todo!()
    }
    
    fn get_max_key(&self) -> String {
        todo!()
    }
    
    fn get_min_key(&self) -> String {
        todo!()
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne::new();
 * obj.inc(key);
 * obj.dec(key);
 * let ret_3: String = obj.get_max_key();
 * let ret_4: String = obj.get_min_key();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = AllOne::new();
        obj.inc("hello".to_string());
        obj.inc("hello".to_string());
        let want: String = "hello".to_string();
        check_eq!(obj.get_max_key(), want);
        let want: String = "hello".to_string();
        check_eq!(obj.get_min_key(), want);
        obj.inc("leet".to_string());
        let want: String = "hello".to_string();
        check_eq!(obj.get_max_key(), want);
        let want: String = "leet".to_string();
        check_eq!(obj.get_min_key(), want);
    }
}
