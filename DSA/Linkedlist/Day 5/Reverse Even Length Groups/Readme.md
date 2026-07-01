\# Linked List 5: Reverse Even Length Groups



\---



\## Pattern



Reverse groups



\---



\## Problem Statement



Nodes are grouped in sizes:

1, 2, 3, 4, ...



Reverse only groups with even length.



\---



\## Constraints



\- 1 <= number of nodes <= 100000

\- 0 <= Node.val <= 100000



\---



\## Optimal Approach



1\. Start with group\_size = 1

2\. Traverse list group by group

3\. Count actual nodes in current group

4\. If group size is even → reverse group

5\. Else → keep as it is

6\. Move to next group and increment size



\---



\## Why it works



Each group size is predefined.

We only modify groups with even sizes,

keeping structure consistent.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



https://leetcode.com/problems/reverse-nodes-in-even-length-groups/solutions/8369015/reverse-nodes-in-even-length-groups-by-9-g6xb

