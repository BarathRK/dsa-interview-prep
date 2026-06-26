# Array 6 - Sort Colors

## Pattern
**Dutch National Flag Algorithm**

## Problem

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red, white, and blue**.

The integers are used to represent the colors as follows:

- `0` → Red
- `1` → White
- `2` → Blue

---

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`

---

## Brute Force Approach

1. Compare each element with every other element using nested loops.
2. Swap the elements if they are in the wrong order.
3. Continue until the array is sorted.

### Time Complexity

- **O(N²)**

### Space Complexity

- **O(1)**

---

## Optimal Approach

1. Initialize three pointers:
   - `low = 0`
   - `mid = 0`
   - `high = n - 1`
2. Traverse the array while `mid <= high`.
3. If `nums[mid] == 0`:
   - Swap `nums[low]` and `nums[mid]`.
   - Increment both `low` and `mid`.
4. Else if `nums[mid] == 1`:
   - Increment `mid`.
5. Else (`nums[mid] == 2`):
   - Swap `nums[mid]` and `nums[high]`.
   - Decrement `high`.
   - Do **not** increment `mid` because the swapped element needs to be checked.

---

## Algorithm

**Dutch National Flag Algorithm**

### Time Complexity

- **O(N)**

### Space Complexity

- **O(1)**

---

## LeetCode Link

- https://leetcode.com/problems/sort-colors/solutions/8359139/sort-color-by-9w0hwvxjmq-3d6c