class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        minVal = min(a, b)
        result = 0
        
        for i in range(1, minVal + 1):
            if a % i == 0 and b % i == 0:
                result += 1
        
        return result