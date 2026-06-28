# Sorting 2 - First Missing Positive

**Pattern:** Cyclic Sort

## Problem

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Brute Force

1. Sort an array in ascending order.
2. Check the positive variable is not equal to `-1` and the difference between the positive variable and the current element is greater than `1`, then return `positive + 1`.
3. Check the current element is positive, then update `positive` if step 2 is not satisfied.
4. Finally, return `nums[i] + 1` if none of the positive numbers is missing.

**Time complexity:** **O(N log N)**  
**Space complexity:** **O(1)**

---

## Optimal Approach

1. Initialise the variable **i** to zero and iterate it till **i < n**, where **n** is the length of the array.
2. If the element is in the range `1 <= nums[i] <= n` and `nums[i] - 1 != i`, then swap it to its correct position:
   `nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]`
3. Otherwise, move the **i** pointer one step forward.
4. Iterate from `0` to `n` to find the first missing positive number using the condition `nums[i] != i + 1`.
5. If every element is in its correct position, return `n + 1`.

---

## Time Complexity

**O(N)**

---

## Space Complexity

**O(1)**

---

## LeetCode Link

- https://leetcode.com/problems/first-missing-positive/solutions/8363384/first-missing-positive-by-9w0hwvxjmq-lmr8