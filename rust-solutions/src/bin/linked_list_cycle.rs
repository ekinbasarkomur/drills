// 141. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/
//
// Problem: does following next ever revisit a node?
// Note: this problem barely exists in safe Rust. Option<Box<ListNode>> means
//       one owner per node, so a cycle is impossible to build -- that is the
//       point of the type. The usual workaround, and the one used here, is to
//       model the list as an arena: a Vec of nodes where `next` is an index.
//       A cycle is then just an index pointing backwards.
// Approach:
// Time O(?), space O(?)

// An arena-backed list. node[i].1 is the index of the next node, or None.
type Arena = Vec<(i32, Option<usize>)>;

struct Solution;

impl Solution {
    /// `head` is the index of the first node, or None for an empty list.
    pub fn has_cycle(nodes: &Arena, head: Option<usize>) -> bool {
        let _ = (nodes, head);
        false
    }
}

fn main() {
    let (nodes, head) = build(&[1, 2, 3, 4], 1);
    println!("{}", Solution::has_cycle(&nodes, head));
}

/// Build a list; `cycle_at` is the index the tail points back to, or -1.
fn build(values: &[i32], cycle_at: i32) -> (Arena, Option<usize>) {
    let mut nodes: Arena = values
        .iter()
        .enumerate()
        .map(|(i, &v)| (v, if i + 1 < values.len() { Some(i + 1) } else { None }))
        .collect();

    if cycle_at >= 0 && !nodes.is_empty() {
        let last = nodes.len() - 1;
        nodes[last].1 = Some(cycle_at as usize);
    }

    let head = if nodes.is_empty() { None } else { Some(0) };
    (nodes, head)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn has_cycle(values: &[i32], cycle_at: i32) -> bool {
        let (nodes, head) = build(values, cycle_at);
        Solution::has_cycle(&nodes, head)
    }

    #[test]
    fn example_1() {
        assert!(has_cycle(&[1, 2, 3, 4], 1));
    }

    #[test]
    fn example_2() {
        assert!(!has_cycle(&[1, 2], -1));
    }

    #[test]
    fn empty_list() {
        assert!(!has_cycle(&[], -1));
    }

    #[test]
    fn single_node_no_cycle() {
        assert!(!has_cycle(&[1], -1));
    }

    #[test]
    fn single_node_pointing_at_itself() {
        assert!(has_cycle(&[1], 0));
    }

    #[test]
    fn cycle_covers_the_whole_list() {
        assert!(has_cycle(&[1, 2, 3], 0));
    }

    #[test]
    fn cycle_is_just_the_last_node() {
        assert!(has_cycle(&[1, 2, 3], 2));
    }

    #[test]
    fn repeated_values_are_not_a_cycle() {
        // equal values are not the same node
        assert!(!has_cycle(&[1, 1, 1, 1], -1));
    }

    #[test]
    fn long_list_no_cycle() {
        let values: Vec<i32> = (0..1000).collect();
        assert!(!has_cycle(&values, -1));
    }

    #[test]
    fn long_list_with_a_late_cycle() {
        let values: Vec<i32> = (0..1000).collect();
        assert!(has_cycle(&values, 999));
    }
}
