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

2\. Traverse to the nth node from the beginning  

3\. Remove that node by changing the previous node's next pointer  

4\. Reverse the linked list again  



\---



\## Complexity Analysis



\### Time Complexity

\- O(3N)



\### Space Complexity

\- O(1)



\---



\## Optimal Approach



1\. Create a dummy node and point its next to head  

2\. Initialize slow and fast pointers to dummy  

3\. Move fast pointer n + 1 steps forward  

4\. Move both pointers one step at a time until fast reaches the end  

5\. Slow pointer will be just before the node to delete  

6\. Skip the nth node using slow.next = slow.next.next  

7\. Return dummy.next  



\---



\## Why it works



We use a fast-slow pointer with a fixed gap so that when fast reaches the end, slow lands exactly before the node to delete.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



\- Remove Nth node from End: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/8368933/remove-nth-node-from-the-end-by-9w0hwvxj-hvpz

