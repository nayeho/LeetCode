class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        num1 = sum(x for x in range(1, n + 1) if x % m != 0)
        S = n * (n + 1) // 2
        num2 = S - num1
        
        return num1 - num2
