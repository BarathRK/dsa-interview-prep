\# Linked List 5: Reverse Even Length Groups



\## Pattern

Reverse groups



\---



\## Problem Statement

Nodes are grouped as:

1, 2, 3, 4, ...



Reverse only even-sized groups.



\---



\## Optimal Approach

1\. Traverse group by group  

2\. Count nodes in each group  

3\. If group size is even → reverse  

4\. Else → skip  

5\. Move to next group  



\---



\## Why it works

Group sizes are deterministic, so we can safely process each independently.



\---



\## Complexity

\- Time: O(N)  

\- Space: O(1)



\---



\## LeetCode

https://leetcode.com/problems/reverse-nodes-in-even-length-groups/solutions/8369015/reverse-nodes-in-even-length-groups-by-9-g6xb

