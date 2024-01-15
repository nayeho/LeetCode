class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        digit1 = purchaseAmount % 10
        if digit1 >= 5:
            purchaseAmount -= digit1
            purchaseAmount += 10
        else:
            purchaseAmount -= digit1
        
        return 100 - purchaseAmount