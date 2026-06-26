# Array 7 - Subarray Sum Equals K

## Pattern
**Prefix Sum + HashMap**

## Problem

Given an integer array `nums` and an integer `k`, return the total number of **continuous subarrays** whose sum equals `k`.

---

## Constraints

- `1 <= nums.length <= 2 × 10⁴`
- `-1000 <= nums[i] <= 1000`
- `-10⁷ <= k <= 10⁷`

---

## Brute Force Approach

1. Compute the sum of every possible subarray using nested loops.
2. If the current subarray sum equals `k`, increment the `count`.
3. Return the final `count`.

### Time Complexity

- **O(N²)**

### Space Complexity

- **O(1)**

---

## Optimal Approach

1. Initialize a HashMap with `{0: 1}` to handle subarrays starting from index `0`.
2. Initialize `prefix_sum = 0` and `count = 0`.
3. Traverse the array and update the running `prefix_sum`.
4. Check if `(prefix_sum - k)` exists in the HashMap.
   - If it exists, add its frequency to `count`.
5. Store or update the frequency of the current `prefix_sum` in the HashMap.
6. Return the `count`.

---

## Algorithm

**Prefix Sum + HashMap**

### Time Complexity

- **O(N)**

### Space Complexity

- **O(N)**

---

## LeetCode Link

- https://leetcode.com/problems/subarray-sum-equals-k/