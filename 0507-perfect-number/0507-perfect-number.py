class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        # return num in {6, 28, 496, 8128, 33550336}
        
        if num == 1:
            return False
        
        return self.getSumOfDivisor(num) == num
        
        
    def getSumOfDivisor(self, num: int) -> int:
        
        result = 1
        
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                result += i + num / i
                
        return int(result)
    
