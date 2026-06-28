# Sorting 3 - Count Inversions

**Pattern:** Merge Sort

---

## Problem

Count the number of pairs (i, j) in an array such that i < j and arr[i] > arr[j].

---

## Constraints

1 ≤ n ≤ 10^5  
-10^9 ≤ arr[i] ≤ 10^9  

---

## Optimal Approach

1. Divide the array into two halves.
2. Recursively count inversions in the left half.
3. Recursively count inversions in the right half.
4. Count cross inversions while merging.
5. Sum all three counts.

---

## Time Complexity

**O(N log N)**

---

## Space Complexity

**O(N)**
```