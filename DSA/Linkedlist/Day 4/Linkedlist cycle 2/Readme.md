\# Linked List 3: Linked List Cycle II



\---



\## Pattern



\*\*Cycle detection\*\*



\---



\## Problem Statement



Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.



\---



\## Constraints



\- The number of nodes in the list is in the range `\[0, 10^4]`

\- `-10^5 <= Node.val <= 10^5`

\- `pos` is `-1` or a valid index in the linked list



\---



\## Optimal Approach



1\. Initialize `slow` and `fast` pointers at the head.

2\. Move `slow` by one step and `fast` by two steps to detect a cycle.

3\. If `slow` and `fast` never meet, return `None` (no cycle exists).

4\. Reset `slow` to the head after the first meeting point.

5\. Move both pointers one step at a time until they meet again.

6\. Return the meeting node as the starting node of the cycle.



\---



\## Complexity Analysis



\### Time Complexity

\- \*\*O(N)\*\*



\### Space Complexity

\- \*\*O(1)\*\*



\---



\## LeetCode Problem



\- \*\*Linked List Cycle II:\*\* https://leetcode.com/problems/linked-list-cycle-ii/solutions/8367783/linkedlist-cycle-2-by-9w0hwvxjmq-owic
