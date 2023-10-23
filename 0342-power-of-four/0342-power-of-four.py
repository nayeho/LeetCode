class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        dicFour = {}
        
        for i in range(-16, 16 + 1):
            dicFour[str(i)] = pow(4, i)
            
        if n in dicFour.values():
            return True
        else:
            return False
        