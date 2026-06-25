# Array 3 - Product of Array Except Self

## Pattern
**Prefix / Suffix**

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`

## Brute Force Approach
- First prepare prefix and suffix product arrays.
- Get the `i - 1`th index value from the prefix array.
- Get the `i + 1`th index value from the suffix array.
- Multiply both and store it in the `i`th index of the answer array.
- Return the answer array.

### Time Complexity
- **O(N)**

### Space Complexity
- **O(2N)**

## Optimal Approach
1. Initialize the variables `prefix` and `suffix` to `1`.
2. Iterate through the array from left to right to make the contribution of the prefix variable.
3. Iterate through the array from right to left to make the contribution of the suffix variable.
4. Finally, return the answer array.

### Time Complexity
- **O(N)**

### Space Complexity
- **O(1)**

## LeetCode Link
- [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/solutions/8357495/product-of-array-except-self-by-9w0hwvxj-brxa)