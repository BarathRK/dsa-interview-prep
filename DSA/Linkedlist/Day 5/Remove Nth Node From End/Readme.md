\# Linked List 4: Remove Nth Node From End



\---



\## Pattern



Gap technique with dummy node



\---



\## Problem Statement



Given the head of a linked list, remove the nth node from the end of the list and return its head.



\---



\## Constraints



\- Number of nodes in the list is sz

\- 1 <= sz <= 30

\- 0 <= Node.val <= 100

\- 1 <= n <= sz



\---



\## Brute Force Approach



1\. Reverse the linked list

2\. Traverse to the nth node from beginning

3\. Remove it

4\. Reverse again



\---



\## Optimal Approach



1\. Create dummy node pointing to head

2\. Use slow and fast pointers at dummy

3\. Move fast pointer n+1 steps ahead

4\. Move both until fast reaches end

5\. Slow will be before target node

6\. Skip target using slow.next = slow.next.next

7\. Return dummy.next



\---



\## Why it works



Fast pointer creates a fixed gap so when it reaches the end,

slow pointer is exactly before the node to delete.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/8368933/remove-nth-node-from-the-end-by-9w0hwvxj-hvpz

