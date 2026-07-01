\# Linked List 5: Reverse Even Length Groups



\---



\## Pattern



Reverse groups



\---



\## Problem Statement



You are given the head of a linked list.



The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of natural numbers (1, 2, 3, 4, ...).



\- The 1st node is assigned to group 1

\- The next 2 nodes are assigned to group 2

\- The next 3 nodes are assigned to group 3, and so on



If the last group has fewer nodes than required, it contains all remaining nodes.



Reverse the nodes in each group that has an even length, and return the modified linked list.



\---



\## Constraints



\- 1 <= number of nodes <= 100000

\- 0 <= Node.val <= 100000



\---



\## Optimal Approach



1\. Initialize:

&#x20;  - dummy node

&#x20;  - prev\_group\_end pointer

&#x20;  - curr pointer

&#x20;  - group\_size = 1



2\. Traverse the list while curr is not null



3\. For each group:

&#x20;  - Count actual nodes using a temporary pointer



4\. If group size is even:

&#x20;  - Reverse exactly those nodes



5\. Reconnect the reversed group with previous and next parts



6\. If group size is odd:

&#x20;  - Move pointers without reversing



7\. Update prev\_group\_end and curr



8\. Increment group\_size



9\. Return dummy.next



\---



\## Why it works



Each group is formed with increasing sizes (1, 2, 3, ...).  

We only reverse groups with even sizes, so we:



\- Identify group boundaries

\- Measure group length

\- Reverse only when required



This keeps the structure intact while modifying only valid groups.



\---



\## Complexity Analysis



\### Time Complexity

\- O(N)



\### Space Complexity

\- O(1)



\---



\## LeetCode Problem



\- Reverse Nodes in Even Length Groups  

https://leetcode.com/problems/reverse-nodes-in-even-length-groups/solutions/8369015/reverse-nodes-in-even-length-groups-by-9-g6xb

