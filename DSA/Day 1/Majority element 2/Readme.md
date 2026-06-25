\# Array 1 - Majority Element II



\## Pattern



\*\*Frequency / Counting\*\*



\## Problem



Find the element(s) that appear more than `n / 3` times in an array, where `n` is the size of the array.



\## Constraints



\* `1 <= nums.length <= 5 \* 10^4`

\* `-10^9 <= nums\[i] <= 10^9`



\## Brute Force Approach



\* Find the frequency of all elements in the array.

\* Re-iterate through the array (or frequency map) to find the elements whose occurrence is greater than `n / 3`.

\* Return the majority elements.



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(N)\*\*



\## Optimal Approach



1\. Initialize the variables `candidate1`, `candidate2`, `count1`, and `count2`.

2\. `candidate1` and `candidate2` are the possible majority elements.

3\. Iterate through the array in the first pass to eliminate non-majority elements.

4\. Iterate through the array in the second pass to verify the count of the two candidates.

5\. Check whether the candidates are majority elements.

6\. Append the valid majority elements to the result list and return it.



\## Algorithm



\*\*Boyer–Moore Voting Algorithm\*\*



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\## LeetCode Link



\* \[Majority Element II](https://leetcode.com/problems/majority-element-ii/solutions/8357226/majority-element-by-9w0hwvxjmq-f8ix)



