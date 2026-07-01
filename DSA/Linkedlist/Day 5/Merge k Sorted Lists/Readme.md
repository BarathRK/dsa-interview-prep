\# Linked List 7: Merge K Sorted Lists



\---



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

\- Each lists\[i] is sorted in ascending order

\- Total number of nodes across all lists will not exceed 10000



\---



\## Optimal Approach



1\. Push the head of each linked list into a min heap

2\. While heap is not empty:

&#x20;  - Extract the smallest node

&#x20;  - Attach it to result list

&#x20;  - Push next node from same list (if exists)

3\. Continue until heap becomes empty



\---



\## Why it works



A min heap always gives the smallest available node among all k lists.



So at every step:

\- We pick the smallest node

\- Maintain sorted order naturally

\- Build final merged list incrementally



\---



\## Complexity Analysis



\### Time Complexity

\- O(N log K)



\### Space Complexity

\- O(K)



\---



\## LeetCode Problem



https://leetcode.com/problems/merge-k-sorted-lists/solutions/8369342/merge-k-sorted-lists-by-9w0hwvxjmq-gimr

