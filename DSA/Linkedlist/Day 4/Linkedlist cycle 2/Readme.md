# Linked List 3: Linked List Cycle II

---

## Pattern

**Cycle Detection (Floyd’s Tortoise and Hare)**

---

## Problem Statement

Given the head of a linked list, return the **node where the cycle begins**. If there is no cycle, return `null`.

---

## Constraints

- The number of nodes in the list is in the range **[0, 10^4]**
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list

---

## Optimal Approach

1. Initialize two pointers:
   - `slow = head`
   - `fast = head`

2. Move pointers:
   - `slow` moves 1 step at a time
   - `fast` moves 2 steps at a time

3. If `slow` and `fast` never meet:
   - Return `null` (no cycle exists)

4. If they meet:
   - A cycle is confirmed

5. Reset `slow` to `head`

6. Move both pointers one step at a time

7. The node where they meet again is the **start of the cycle**

8. Return that node

---

## Why it works

After detection, resetting one pointer to head aligns distances such that both pointers meet exactly at the cycle entry point.

---

## Complexity Analysis

### Time Complexity
- **O(N)**

### Space Complexity
- **O(1)**

---

## LeetCode Problem

- Linked List Cycle II: https://leetcode.com/problems/linked-list-cycle-ii/solutions/8367783/linkedlist-cycle-2-by-9w0hwvxjmq-owic