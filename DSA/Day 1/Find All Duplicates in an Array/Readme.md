\# Array 4 - Find All Duplicates in an Array



\## Pattern



\*\*Index Mapping\*\*



\## Problem



Given an integer array `nums` of length `n` where all the integers are in the range `\[1, n]` and each integer appears at most twice, return an array of all the integers that appear twice.



\## Constraints



\* `n == nums.length`

\* `1 <= n <= 10^5`

\* `1 <= nums\[i] <= n`



\## Brute Force Approach



\* Iterate through the array and calculate the frequency of each element.

\* Check which elements appear twice and append them to an answer array.

\* Return the answer array.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(2N)\*\*



\## Optimal Approach



1\. Iterate through the array.

2\. For each element, compute `index = abs(nums\[i]) - 1`.

3\. Check whether the value at `nums\[index]` is negative.

4\. If it is negative, then the current element has already been seen, so append it to the answer array.

5\. Otherwise, mark `nums\[index]` as negative.

6\. Return the answer array.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\## LeetCode Link



\* \[Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/solutions/8357600/find-all-duplications-in-an-array-by-9w0-tlk9)



