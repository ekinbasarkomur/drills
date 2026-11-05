// 706. Design HashMap · Easy · https://leetcode.com/problems/design-hashmap/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyHashMap {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {

    fn new() -> Self {
        todo!()
    }
    
    fn put(&self, key: i32, value: i32) {
        todo!()
    }
    
    fn get(&self, key: i32) -> i32 {
        todo!()
    }
    
    fn remove(&self, key: i32) {
        todo!()
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyHashMap::new();
        obj.put(1, 1);
        obj.put(2, 2);
        check_eq!(obj.get(1), 1);
        check_eq!(obj.get(3), -1);
        obj.put(2, 1);
        check_eq!(obj.get(2), 1);
        obj.remove(2);
        check_eq!(obj.get(2), -1);
    }
}
