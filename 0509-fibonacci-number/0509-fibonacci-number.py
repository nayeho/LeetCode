class Solution:
    def fib(self, n: int) -> int:
        
        result = [0, 1]
        
        for i in range(2, n + 1):
            result.append(result[-1] + result[-2])
            
        return result[n]
        