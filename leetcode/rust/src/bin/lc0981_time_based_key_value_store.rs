// 981. Time Based Key-Value Store · Medium · https://leetcode.com/problems/time-based-key-value-store/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct TimeMap {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        todo!()
    }
    
    fn set(&self, key: String, value: String, timestamp: i32) {
        todo!()
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        todo!()
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = TimeMap::new();
        obj.set("foo".to_string(), "bar".to_string(), 1);
        let want: String = "bar".to_string();
        check_eq!(obj.get("foo".to_string(), 1), want);
        let want: String = "bar".to_string();
        check_eq!(obj.get("foo".to_string(), 3), want);
        obj.set("foo".to_string(), "bar2".to_string(), 4);
        let want: String = "bar2".to_string();
        check_eq!(obj.get("foo".to_string(), 4), want);
        let want: String = "bar2".to_string();
        check_eq!(obj.get("foo".to_string(), 5), want);
    }
}
