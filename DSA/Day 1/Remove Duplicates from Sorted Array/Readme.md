Array 4: 

Pattern :  in place marking

Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.


Optimal approach:

1.First intialize the variables i and j
2.Iterate the loop
3.Check if the i-th element is equal to j-th element
4.Then move only j-th variable by one place
5.Otherwise,update the i+1-th element and move both i-th and j-th variable

Time complexity  : O(N)
space complexity : O(1)

leetcode link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/8357631/remove-all-duplicates-from-sorted-array-q5667
