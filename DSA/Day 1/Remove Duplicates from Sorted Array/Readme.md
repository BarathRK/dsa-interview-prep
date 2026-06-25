# Array 5 - Remove Duplicates from Sorted Array

## Pattern
**In-Place Marking / Two Pointers**

## Problem
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

## Optimal Approach
1. First initialize the variables `i` and `j`.
2. Iterate through the array.
3. Check if the `i`th element is equal to the `j`th element.
4. If both are equal, move only the `j` pointer by one place.
5. Otherwise, update the `(i + 1)`th element with `nums[j]` and move both `i` and `j`.
6. Return `i + 1` as the count of unique elements.

### Time Complexity
- **O(N)**

### Space Complexity
- **O(1)**

## LeetCode Link
- [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/8357631/remove-all-duplicates-from-sorted-array-q5667)