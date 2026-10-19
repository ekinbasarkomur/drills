// 380. Insert Delete GetRandom O(1) · Medium · https://leetcode.com/problems/insert-delete-getrandom-o1/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct RandomizedSet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        todo!()
    }
    
    fn insert(&self, val: i32) -> bool {
        todo!()
    }
    
    fn remove(&self, val: i32) -> bool {
        todo!()
    }
    
    fn get_random(&self) -> i32 {
        todo!()
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = RandomizedSet::new();
        assert_eq!(obj.insert(1), true);
        assert_eq!(obj.remove(2), false);
        assert_eq!(obj.insert(2), true);
        obj.get_random();
        assert_eq!(obj.remove(1), true);
        assert_eq!(obj.insert(2), false);
        obj.get_random();
    }
}
