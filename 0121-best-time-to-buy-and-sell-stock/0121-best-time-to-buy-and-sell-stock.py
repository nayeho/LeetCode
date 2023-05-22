class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i, price in enumerate(prices):
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, price)
            
        return maxProfit
            
        