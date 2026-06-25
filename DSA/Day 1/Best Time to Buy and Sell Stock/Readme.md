\# Array 2 - Best Time to Buy and Sell Stock



\## Pattern



\*\*Kadane's Algorithm\*\*



\## Problem



Find the maximum profit that can be achieved from stock prices over `n` days.



\## Constraints



\* `1 <= prices.length <= 10^5`

\* `0 <= prices\[i] <= 10^4`



\## Brute Force Approach



\* Compare each element price with the adjacent elements.

\* Compute the profit for every possible transaction.

\* Pick the maximum profit.

\* Return the maximum profit.



\### Time Complexity



\* \*\*O(N²)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\## Optimal Approach



1\. Initialize the variables `minimum` and `maximum\_profit`.

2\. Keep track of the minimum buying price in the `minimum` variable.

3\. For each day, calculate the current profit as `prices\[i] - minimum`.

4\. Compare it with `maximum\_profit` and update if needed.

5\. Return the maximum profit.



\## Algorithm



\*\*Kadane's Algorithm / Running Minimum Technique\*\*



\### Time Complexity



\* \*\*O(N)\*\*



\### Space Complexity



\* \*\*O(1)\*\*



\## LeetCode Link



\* \[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/8357286/best-time-to-buy-and-sell-stock-by-9w0hw-y34z)



