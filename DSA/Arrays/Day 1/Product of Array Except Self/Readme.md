Array 3: 

Pattern :  Prefix\Suffix

Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30

Brute force  approach:

1. First prepare a suffix and prefix product array
2. Get the i-1th index value from prefix array
3. Get the i+1th index value from suffix array
4. Multiply both and store it in an answer array ith index
5. Return an answer array

Time complexity  : O(N)
space complexity : O(2*N)

Optimal approach:

1.First initialise the variables prefix and suffix to one.
2.Iterate the first loop to make the contribution of prefix variable (0,n-1)
3.Iterate the second loop to make the contribution of suffix variable (n-2,0)
4.Finally return an answer array

Time complexity  : O(N)
space complexity : O(1)

leetcode link : https://leetcode.com/problems/product-of-array-except-self/solutions/8357495/product-of-array-except-self-by-9w0hwvxj-brxa
