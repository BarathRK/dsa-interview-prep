\# Array 3 - Product of Array Except Self



\## Pattern



\*\*Prefix / Suffix\*\*



\## Problem



Given an integer array `nums`, return an array `answer` such that `answer\[i]` is equal to the product of all the elements of `nums` except `nums\[i]`.



\## Constraints



\* `2 <= nums.length <= 10^5`

\* `-30 <= nums\[i] <= 30`



\## Brute Force Approach



\* Prepare prefix and suffix product arrays.

\* Get the `i - 1`th index value from the prefix array.

\* Get the `i + 1`th index value from the suffix array.

\* Multiply both and store the result at the `i`th index of the answer array.

\* Return the answer array.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(2N)\*\*



\## Optimal Approach



1\. Initialize the variables `prefix` and `suffix` to `1`.

2\. Iterate from left to right and store prefix contributions in the answer array.

3\. Iterate from right to left and multiply suffix contributions into the answer array.

4\. Return the final answer array.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*

&#x20; \*(excluding the output array)\*



\## LeetCode Link



\* \[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/solutions/8357495/product-of-array-except-self-by-9w0hwvxj-brxa)



