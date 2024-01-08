class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        check = 1
        
        while 1:
            if n > check:
                n -= check
                check += 1
            elif n == check:
                return check
            else:
                return check - 1
        