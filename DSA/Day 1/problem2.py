class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = -100000
        minimum = 1000000
        for price in prices:
            minimum = min(price,minimum)
            maximum_profit = max(maximum_profit,(price-minimum))
        return maximum_profit
            
        