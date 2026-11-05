// 146. LRU Cache
// https://leetcode.com/problems/lru-cache/
// Plan: Aşama 0 · Linked List
//
// Problem: a fixed-capacity key/value store. get and put both count as "using"
//          a key; when the cache is full, the least recently used key is
//          evicted. Both operations must be O(1) on average.
// Note: the textbook answer -- a hash map whose values are pointers into a
//       doubly linked list -- fights Rust's ownership rules hard. Two handles
//       to the same node means Rc<RefCell<..>>, and the back-pointers mean
//       Weak. A common alternative here is an arena: keep the nodes in a Vec
//       and let prev/next be indices into it.
// Approach:
// Time O(?) per operation, space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct LRUCache {
    // TODO: what does this need to hold?
}

impl LRUCache {
    fn new(capacity: i32) -> Self {
        let _ = capacity;
        todo!()
    }

    fn get(&mut self, key: i32) -> i32 {
        let _ = key;
        todo!()
    }

    fn put(&mut self, key: i32, value: i32) {
        let _ = (key, value);
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let mut c = LRUCache::new(2);
    c.put(1, 10);
    println!("{}", c.get(1));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        check_eq!(c.get(1), 10);
        c.put(2, 20);
        c.put(3, 30); // evicts key 1
        check_eq!(c.get(2), 20);
        check_eq!(c.get(1), -1);
    }

    #[test]
    fn missing_key_returns_minus_one() {
        let mut c = LRUCache::new(2);
        check_eq!(c.get(7), -1);
    }

    #[test]
    fn overwriting_a_key_updates_its_value() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        c.put(1, 99);
        check_eq!(c.get(1), 99);
    }

    #[test]
    fn overwriting_does_not_grow_the_cache() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        c.put(1, 11);
        c.put(2, 20);
        check_eq!(c.get(1), 11);
        check_eq!(c.get(2), 20);
    }

    #[test]
    fn capacity_one_evicts_every_time() {
        let mut c = LRUCache::new(1);
        c.put(1, 10);
        c.put(2, 20);
        check_eq!(c.get(1), -1);
        check_eq!(c.get(2), 20);
    }

    #[test]
    fn a_get_counts_as_use_and_saves_a_key() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        c.put(2, 20);
        c.get(1); // 2 is now the least recently used
        c.put(3, 30);
        check_eq!(c.get(2), -1);
        check_eq!(c.get(1), 10);
        check_eq!(c.get(3), 30);
    }

    #[test]
    fn a_put_on_an_existing_key_counts_as_use() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        c.put(2, 20);
        c.put(1, 11); // 2 is now the least recently used
        c.put(3, 30);
        check_eq!(c.get(2), -1);
        check_eq!(c.get(1), 11);
    }

    #[test]
    fn a_failed_get_does_not_change_the_order() {
        let mut c = LRUCache::new(2);
        c.put(1, 10);
        c.put(2, 20);
        c.get(99); // not present
        c.put(3, 30); // must still evict 1
        check_eq!(c.get(1), -1);
        check_eq!(c.get(2), 20);
    }

    #[test]
    fn filling_exactly_to_capacity_evicts_nothing() {
        let mut c = LRUCache::new(3);
        c.put(1, 10);
        c.put(2, 20);
        c.put(3, 30);
        check_eq!(c.get(1), 10);
        check_eq!(c.get(2), 20);
        check_eq!(c.get(3), 30);
    }

    #[test]
    fn value_range_extremes() {
        let mut c = LRUCache::new(2);
        c.put(0, 0);
        c.put(10_000, 100_000);
        check_eq!(c.get(0), 0);
        check_eq!(c.get(10_000), 100_000);
    }

    #[test]
    fn many_operations_stay_constant_time() {
        // 3000 keys held, then more puts sweeping past them.
        // An O(n) eviction scan will crawl here.
        let mut c = LRUCache::new(3000);
        for i in 0..3000 {
            c.put(i, i * 2);
        }
        check_eq!(c.get(0), 0); // still present, and now most recent
        for i in 3000..10_000 {
            c.put(i, i);
        }
        check_eq!(c.get(9_999), 9_999); // newest survived
        check_eq!(c.get(1), -1); // oldest was evicted
    }
}
