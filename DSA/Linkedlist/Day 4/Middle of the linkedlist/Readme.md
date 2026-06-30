\# Linked List 1: Middle of the Linked List



\## Pattern



\*\*Tortoise and Hare (Slow \& Fast Pointer)\*\*



\---



\## Problem Statement



Given the head of a singly linked list, return the \*\*middle node\*\* of the linked list.



If there are \*\*two middle nodes\*\*, return the \*\*second middle node\*\*.



\---



\## Constraints



\* The number of nodes in the list is in the range \*\*\[1, 100]\*\*.

\* `1 <= Node.val <= 100`



\---



\## Optimal Approach (Slow \& Fast Pointer)



1\. Initialize two pointers:



&#x20;  \* `slow = head`

&#x20;  \* `fast = head`

2\. Traverse the linked list while:



&#x20;  ```text

&#x20;  fast != None and fast.next != None

&#x20;  ```

3\. In each iteration:



&#x20;  \* Move `slow` one step forward.

&#x20;  \* Move `fast` two steps forward.

4\. When the loop ends:



&#x20;  \* `slow` will be pointing to the middle node.

5\. Return `slow`.



> \*\*Why it works:\*\*

> Since the `fast` pointer moves twice as fast as the `slow` pointer, by the time `fast` reaches the end of the list, `slow` will be at the middle.



\---



\## Complexity Analysis



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\---



\## LeetCode Problem



\* \*\*Middle of the Linked List:\*\* https://leetcode.com/problems/middle-of-the-linked-list/solutions/8365002/middle-of-the-linkedlist-by-9w0hwvxjmq-3mvi

