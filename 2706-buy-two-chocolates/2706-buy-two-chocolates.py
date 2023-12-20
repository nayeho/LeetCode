class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        
        price = prices[0] + prices[1]
        
        change = money - price
        
        if change >= 0:
            return change
        else:
            return money
        
        