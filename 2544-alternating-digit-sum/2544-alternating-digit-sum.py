class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        sign = 1
        result = 0
        
        s = str(n)
        
        for i in s:
            result += int(i) * sign
            sign *= -1
            
        return result
        
        