\# Sorting 2 - Count Inversions



\*\*Pattern:\*\* Merge sort



\---



\## Problem



Count the number of pairs (i, j) in an array such that i < j and arr\[i] > arr\[j].



\---



\## Constraints



1 ≤ n ≤ 10^5  

\-10^9 ≤ arr\[i] ≤ 10^9  



\---



\## Optimal Approach



1\. Divide array into two halves.

2\. Recursively count inversions in left half.

3\. Recursively count inversions in right half.

4\. Count cross inversions while merging.

5\. Sum all three.



\---



\## Time Complexity



\*\*O(N log N)\*\*



\---



\## Space Complexity



\*\*O(N)\*\*

```

