\# Linked List 2: Palindrome Linked List



\## Pattern



\*\*Reverse a Linked List\*\*



\---



\## Problem Statement



Given the head of a singly linked list, return `true` if it is a palindrome; otherwise, return `false`.



\---



\## Constraints



\- The number of nodes in the list is in the range \*\*\[1, 10<sup>5</sup>]\*\*.

\- `0 <= Node.val <= 9`



\---



\## Optimal Approach (Slow \& Fast Pointer)



1\. Initialize both the `slow` and `fast` pointers to the `head`.

2\. Find the middle node of the linked list using the slow and fast pointer technique.

3\. Reverse the second half of the linked list.

4\. Compare the values of the first half and the reversed second half.

5\. If any corresponding values do not match, return `false`.

6\. If all values match, return `true`.



\---



\## Complexity Analysis



\### Time Complexity



\- \*\*O(N)\*\*



\### Space Complexity



\- \*\*O(1)\*\*



\---



\## LeetCode Problem



\- \*\*Palindrome Linked List:\*\*  

&#x20; https://leetcode.com/problems/palindrome-linked-list/solutions/8367693/palindrome-linkedlist-by-9w0hwvxjmq-79jw

