class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return '0'
        
        sign = ''
        result = ''
        
        if num == '0':
            return '0'
        elif num < 0:
            sign = '-'
            num = -num
            
        while num:
            result = str(num % 7) + result
            num //= 7
            
        return sign + result
            
        
        
        
        