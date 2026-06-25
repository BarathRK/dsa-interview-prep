Array 2:

Pattern : kadane's algorithm 

Problem : Finding the maximum profit for the following n days.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Brute force approach:

1. Compare each element price with the adjacent elements
2. Pick the maximum profit
3. Return the maximum

Time complexity : O(N^2)
Space complexity : O(1)

Optimal approach:

1. Initiliase the variables minimum,maximum_profit
2. Keep track of minimum selling price in minimum variable
3. calculate and compare the profit among themselves
4. Return the maximum profit

Algorithm : Kadane's algorithm

Time complexity : O(N)
Space complexity : O(1)