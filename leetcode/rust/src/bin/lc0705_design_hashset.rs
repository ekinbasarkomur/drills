// 705. Design HashSet · Easy · https://leetcode.com/problems/design-hashset/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyHashSet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {
        todo!()
    }
    
    fn add(&self, key: i32) {
        todo!()
    }
    
    fn remove(&self, key: i32) {
        todo!()
    }
    
    fn contains(&self, key: i32) -> bool {
        todo!()
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyHashSet::new();
        obj.add(1);
        obj.add(10001);
        obj.add(1);
        obj.remove(1);
        obj.contains(1);
        obj.add(7);
        obj.add(10007);
        obj.add(7);
        obj.remove(7);
        obj.contains(7);
        obj.add(123);
        obj.add(10123);
        obj.add(123);
        obj.remove(123);
        obj.contains(123);
        obj.add(5000);
        obj.add(15000);
        obj.add(5000);
        obj.remove(5000);
        obj.contains(5000);
    }
}
