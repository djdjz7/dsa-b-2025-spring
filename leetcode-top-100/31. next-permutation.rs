// https://leetcode.cn/problems/next-permutation/

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        for i in (0..nums.len() - 1).rev() {
            if nums[i + 1] <= nums[i] {
                continue;
            }
            for j in (i..nums.len()).rev() {
                if nums[i] < nums[j] {
                    nums.swap(i, j);
                    nums[i + 1..].reverse();
                    return;
                }
            }
        }
        nums.reverse();
    }
}