# Linked List 1: Middle of the Linked List

## Pattern

**Tortoise and Hare (Slow & Fast Pointer)**

---

## Problem Statement

Given the head of a singly linked list, return the **middle node** of the linked list.

If there are **two middle nodes**, return the **second middle node**.

---

## Constraints

- The number of nodes in the list is in the range **[1, 100]**
- `1 <= Node.val <= 100`

---

## Optimal Approach (Slow & Fast Pointer)

1. Initialize two pointers:
   - `slow = head`
   - `fast = head`

2. Traverse the linked list while:
   ```
   fast != None and fast.next != None
   ```

3. In each iteration:
   - Move `slow` one step forward
   - Move `fast` two steps forward

4. When the loop ends:
   - `slow` will be at the middle node

5. Return `slow`

> Why it works:  
The fast pointer moves twice as fast as the slow pointer. When fast reaches the end, slow will be at the middle.

---

## Complexity Analysis

### Time Complexity
- O(N)

### Space Complexity
- O(1)

---

## LeetCode Problem

- Middle of the Linked List: https://leetcode.com/problems/middle-of-the-linked-list/solutions/8365002/middle-of-the-linkedlist-by-9w0hwvxjmq-3mvi