class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            sign = -1
            x = x * -1
        else:
            sign = 1
            
        x = str(x)
        x = x[::-1]
        x = int(x)
        result = sign * x
        
        return result if -2**31 <= result <= 2**31 - 1 else 0
            
        