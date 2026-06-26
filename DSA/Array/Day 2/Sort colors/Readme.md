\# Array 6 - Sort Colors



\## Pattern

\*\*Dutch National Flag Algorithm\*\*



\## Problem

Given an array `nums` with `n` objects colored red, white, or blue, sort them \*\*in-place\*\* so that objects of the same color are adjacent, with the colors in the order \*\*red, white, and blue\*\*.



The integers are used to represent the colors as follows:

\- `0` → Red

\- `1` → White

\- `2` → Blue



\---



\## Constraints



\- `n == nums.length`

\- `1 <= n <= 300`

\- `nums\[i]` is either `0`, `1`, or `2`



\---



\## Brute Force Approach



1\. Compare each element with every other element using nested loops.

2\. Swap the elements if they are in the wrong order.

3\. Continue until the array is sorted.



\### Time Complexity



\- \*\*O(N²)\*\*



\### Space Complexity



\- \*\*O(1)\*\*



\---



\## Optimal Approach (Dutch National Flag Algorithm)



1\. Initialize three pointers:

&#x20;  - `low = 0`

&#x20;  - `mid = 0`

&#x20;  - `high = n - 1`

2\. Traverse the array while `mid <= high`.

3\. If `nums\[mid] == 0`:

&#x20;  - Swap `nums\[low]` and `nums\[mid]`.

&#x20;  - Increment both `low` and `mid`.

4\. Else if `nums\[mid] == 1`:

&#x20;  - Increment `mid`.

5\. Else (`nums\[mid] == 2`):

&#x20;  - Swap `nums\[mid]` and `nums\[high]`.

&#x20;  - Decrement `high`.

&#x20;  - Do \*\*not\*\* increment `mid` because the swapped element needs to be checked.



\---



\## Algorithm



\*\*Dutch National Flag Algorithm\*\*



\### Time Complexity



\- \*\*O(N)\*\*



\### Space Complexity



\- \*\*O(1)\*\*



\---



\## LeetCode Link



\- https://leetcode.com/problems/sort-colors/

```

