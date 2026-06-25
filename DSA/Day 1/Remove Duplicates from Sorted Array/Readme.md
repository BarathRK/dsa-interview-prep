\# Array 5 - Remove Duplicates from Sorted Array



\## Pattern



\*\*In-Place Marking / Two Pointers\*\*



\## Problem



Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.



\## Constraints



\* `1 <= nums.length <= 3 \* 10^4`

\* `-100 <= nums\[i] <= 100`

\* `nums` is sorted in non-decreasing order



\## Optimal Approach



1\. Initialize two pointers `i` and `j`.

2\. Iterate through the array using pointer `j`.

3\. Check whether the `i`th element is equal to the `j`th element.

4\. If both are equal, move only `j` forward.

5\. Otherwise, update the `(i + 1)`th position with `nums\[j]`, and move both `i` and `j` forward.

6\. At the end, the first `i + 1` elements of the array will contain the unique elements.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\## LeetCode Link



\* \[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/8357631/remove-all-duplicates-from-sorted-array-q5667)



