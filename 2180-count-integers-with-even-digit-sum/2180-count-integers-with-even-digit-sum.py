class Solution:
    def countEven(self, num: int) -> int:
        
        result = 0
        
        for i in range(2, num + 1):
            if self.isSumEven(i):
                result += 1
            
        return result
    
    def isSumEven(self, num: int) -> bool:
        
        digit1000 = num // 1000
        digit100 = num % 1000 // 100
        digit10 = num % 100 // 10
        digit1 = num % 10
        
        totalDigit = digit1000 + digit100 + digit10 + digit1
        
        return totalDigit % 2 == 0
        
        