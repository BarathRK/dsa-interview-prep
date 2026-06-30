# Interval 1 - Merge Intervals

## Pattern
**Merge Intervals**

## Problem

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## Constraints

- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10⁴`

---

## Optimal Approach

1. Sort the intervals based on their starting time.
2. Traverse each interval.
3. If the result array is not empty or the last interval in the result does not overlap with the current interval, append the current interval.
4. Otherwise, merge the intervals by updating the end time to the maximum of the current interval's end time and the last interval's end time in the result.
5. Return the result array.

---


### Time Complexity

- **O(N log N)**

### Space Complexity

- **O(N)**

---

## LeetCode Link

- https://leetcode.com/problems/merge-intervals/solutions/8359325/merge-interval-by-9w0hwvxjmq-sfri