Array 4: 

Pattern :  index mapping

Problem: Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Brute force  approach:

1. Iterate the loop to calculate frequency of each element
2. Check the elements appears twice and append it to an array
3. Return an answer array

Time complexity  : O(N)
space complexity : O(2*N)

Optimal approach:

1. Iterate an array
2. Store element-1 to index
3. check if the index-th element has a negative sign
4. Then,take an absolute of the current element and append it to answer array
5. Otherwise mark the negative sign to that element.
6. Finally,return an array

Time complexity  : O(N)
space complexity : O(1)

leetcode link : https://leetcode.com/problems/find-all-duplicates-in-an-array/solutions/8357600/find-all-duplications-in-an-array-by-9w0-tlk9
