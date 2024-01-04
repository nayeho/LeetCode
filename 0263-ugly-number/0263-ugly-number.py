class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        while 1:
            if n == 1:
                return True
            elif n % 2 == 0:
                n = n // 2
                continue
            elif n % 3 == 0:
                n = n // 3
                continue
            elif n % 5 == 0:
                n = n // 5
                continue
            else:
                return False
        
        
        