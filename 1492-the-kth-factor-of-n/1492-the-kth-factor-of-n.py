class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                factor.append(i)
            
        factor.append(n)
        
        length = len(factor)
        
        if k > length:
            return -1
        else:
            return factor[k - 1]
        