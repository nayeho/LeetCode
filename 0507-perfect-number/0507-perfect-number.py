class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        return num in {6, 28, 496, 8128, 33550336}
        
        return self.getSumOfDivisor(num) == num * 2
        
        
    def getSumOfDivisor(self, num: int) -> int:
        
        result = num
        
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                result += i
        
        return result