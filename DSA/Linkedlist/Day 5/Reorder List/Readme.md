\# Linked List 6: Reorder List



\---



\## Pattern



Divide and Reconnect



\---



\## Problem Statement



Given a singly linked list:



L0 → L1 → … → Ln



Reorder it as:



L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …



\---



\## Constraints



\- 1 <= number of nodes <= 50000

\- 1 <= Node.val <= 1000



\---



\## Optimal Approach



1\. Find middle using slow and fast pointers

2\. Reverse second half

3\. Split list into two halves

4\. Merge both halves alternately

5\. Return head



\---



\## Why it works



Reversing second half aligns end elements,

allowing alternate merging from both ends.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



https://leetcode.com/problems/reorder-list/solutions/8369116/reorder-list-by-9w0hwvxjmq-bl5h

