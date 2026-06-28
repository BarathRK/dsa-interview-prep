# Sorting 1 - Custom sort String


## Problem

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

---

## Constraints

1 <= order.length <= 26  
1 <= s.length <= 200  
order and s consist of lowercase English letters.  
All the characters of order are unique.

---

## Brute force

1. Traverse each character in order.  
2. For every character, scan the entire string s.  
3. Append matching characters.  
4. After processing order, append remaining characters.  

Time complexity: O(M*N)  
Space complexity: O(1)

---

## Optimal Approach

1. First, initialise the frequency array of size 26 and calculate the occurence of each character in s  
2. Iterate the order variable and add the characters to the result variable with its occurence.  
3. Iterate the frequency array to add it to the result variable until it exhausted.

---

## Time Complexity

**O(N+M)**

---

## Space Complexity

**O(1)**

---

## LeetCode Link

- https://leetcode.com/problems/custom-sort-string/solutions/8363150/custom-sort-string-by-9w0hwvxjmq-o92i