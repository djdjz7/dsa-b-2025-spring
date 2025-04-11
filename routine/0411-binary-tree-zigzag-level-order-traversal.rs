// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if root.is_none() {
            return vec![];
        }
        let root = root.unwrap();
        let mut current_level = vec![root];
        let mut next_level = vec![];
        let mut result = vec![];
        let mut level_result = vec![];
        while current_level.len() > 0 {
            for node in current_level {
                level_result.push(node.borrow().val);
                if node.borrow().left.is_some() {
                    next_level.push(node.borrow().left.as_ref().unwrap().clone());
                }
                if node.borrow().right.is_some() {
                    next_level.push(node.borrow().right.as_ref().unwrap().clone());
                }
            }
            result.push(level_result);
            level_result = vec![];
            current_level = next_level;
            next_level = vec![];
        }
        for level in result.iter_mut().skip(1).step_by(2) {
            level.reverse();
        }
        return result;
    }
}

struct Solution;

fn main() {}
