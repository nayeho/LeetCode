class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        while 1:
            
            if n == 1:
                return True
            elif n == -1:
                return False
            
            if n % 3 == 0:
                n = n // 3
                continue
            else:
                return False
        