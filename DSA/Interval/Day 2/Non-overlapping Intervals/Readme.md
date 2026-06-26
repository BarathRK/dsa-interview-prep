\# Interval 2 - Non-Overlapping Intervals



\## Pattern

\*\*Greedy + Sorting\*\*



\## Problem



Given an array of intervals where `intervals\[i] = \[starti, endi]`, return the minimum number of intervals you need to remove to make the remaining intervals non-overlapping.



\---



\## Constraints



\- `1 <= intervals.length <= 10⁵`

\- `intervals\[i].length == 2`

\- `-5 × 10⁴ <= starti < endi <= 5 × 10⁴`



\---



\## Optimal Approach



1\. Sort the intervals based on their ending time.

2\. Initialize `remove = 0`.

3\. Set `previous\_end\_time` to the end time of the first interval.

4\. Traverse the remaining intervals.

5\. If the current interval's start time is greater than or equal to `previous\_end\_time`, update `previous\_end\_time` to the current interval's end time.

6\. Otherwise, increment the `remove` count.

7\. Return the `remove` count.



\---



\## Algorithm



\*\*Greedy + Sorting\*\*



\### Time Complexity



\- \*\*O(N log N)\*\*



\### Space Complexity



\- \*\*O(1)\*\*



\---



\## LeetCode Link



\- https://leetcode.com/problems/non-overlapping-intervals/solutions/8359444/non-overlapping-intervals-by-9w0hwvxjmq-u1ep

