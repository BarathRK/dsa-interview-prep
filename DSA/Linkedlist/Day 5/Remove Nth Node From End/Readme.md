# Linked List 4: Remove Nth Node From End



## Pattern

Gap technique with dummy node



---



## Problem Statement

Given the head of a linked list, remove the nth node from the end.



---



## Constraints

- 1 <= sz <= 30  

- 1 <= n <= sz  



---



## Optimal Approach

1. Create dummy node  

2. Move fast pointer n+1 steps  

3. Move slow and fast together  

4. Slow stops before target node  

5. Delete node using slow.next  



---



## Why it works

Fast pointer creates a fixed gap so slow lands exactly before the node to delete.



---



## Complexity

- Time: O(N)  

- Space: O(1)



---



## LeetCode

https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/8368933/remove-nth-node-from-the-end-by-9w0hwvxj-hvpz

