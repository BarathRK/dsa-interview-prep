Array 1: 

Pattern :  Frequency/Counting

Problem: Find a element appears more than n/3 times in an array

n = size of an array.

Constraints:

1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Brute force  approach:

1. Find frequency of all element in an array
2. Re-iterate the array to find the elements greater than n/3 occurrence
3. Return the majority elements

Time complexity  : O(N)
space complexity : O(N)

Optimal approach:

1. First initialise the variables candidate1,candidate2,count1,count2
2.candidate1 and candidate2 is the possible majority elements
3.Iterate a first pass to eliminate non majority elements
4.Iterate second pass to verify count of the two candidates
5.Finally check the candidates are majority element
6.Append the majority element to the list and return the results

Time complexity  : O(N)
space complexity : O(1)

Algorithm : Boyer–Moore Voting Algorithm.
leetcode link : https://leetcode.com/problems/majority-element-ii/solutions/8357226/majority-element-by-9w0hwvxjmq-f8ix
