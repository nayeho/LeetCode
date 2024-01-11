class Solution:
    def pivotInteger(self, n: int) -> int:
        
        S = n * (n + 1) // 2
        
        left = 1
        right = S
        
        for i in range(1, n + 1):
            if left == right:
                return i
            else:
                left += (i + 1)
                right -= i
                
        return -1
        