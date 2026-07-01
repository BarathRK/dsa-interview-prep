\# Linked List 7: Merge K Sorted Lists



\## Pattern

Merge lists (Heap / Priority Queue)



\---



\## Problem Statement

You are given an array of k linked lists, where each linked list is sorted in ascending order.



Merge all the linked lists into one sorted linked list and return it.



\---



\## Constraints

\- k == lists.length  

\- 0 <= k <= 10000  

\- 0 <= lists\[i].length <= 500  

\- -10000 <= lists\[i]\[j] <= 10000  

\- Each list is sorted  

\- Total nodes ≤ 10000  



\---



\## Optimal Approach

1\. Push all list heads into a min heap  

2\. Extract smallest node  

3\. Attach to result list  

4\. Push next node from same list  

5\. Repeat until heap is empty  



\---



\## Why it works

A min heap always gives the smallest available node across all lists, ensuring sorted order.



\---



\## Complexity

\- Time: O(N log K)  

\- Space: O(K)



\---



\## LeetCode

https://leetcode.com/problems/merge-k-sorted-lists/solutions/8369342/merge-k-sorted-lists-by-9w0hwvxjmq-gimr

