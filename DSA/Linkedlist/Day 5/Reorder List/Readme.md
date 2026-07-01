\# Linked List 6: Reorder List



\---



\## Pattern



Divide and Reconnect



\---



\## Problem Statement



You are given the head of a singly linked list. The list can be represented as:



L0 → L1 → … → Ln - 1 → Ln



Reorder the list to be in the following form:



L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …



You may not modify the values in the list's nodes. Only nodes themselves may be changed.



\---



\## Constraints



\- 1 <= number of nodes <= 50000  

\- 1 <= Node.val <= 1000  



\---



\## Optimal Approach



1\. Find the middle of the linked list using slow and fast pointers  

2\. Reverse the second half of the list  

3\. Split the list into two halves  

4\. Merge both halves by alternating nodes  

5\. Carefully reconnect nodes while merging  

6\. Return the modified head  



\---



\## Why it works



The problem reduces to rearranging nodes from two directions:



\- First half (start → middle)

\- Reversed second half (end → middle)



By reversing the second half, we align the ends so we can merge alternately in O(1) space.



This ensures correct ordering without extra memory.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



\- Reorder List  

https://leetcode.com/problems/reorder-list/solutions/8369116/reorder-list-by-9w0hwvxjmq-bl5h

