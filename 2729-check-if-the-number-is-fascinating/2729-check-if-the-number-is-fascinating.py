class Solution:
    def isFascinating(self, n: int) -> bool:
        
        if n >= 333:
            return False
        
        n2 = n * 2
        n3 = n * 3
        
        concat = str(n) + str(n2) + str(n3)
        digit = [str(x) for x in range(1, 10)]
        
        for s in concat:
            if s in digit:
                digit.remove(s)
            else:
                return False
        
        return True
        
        
        