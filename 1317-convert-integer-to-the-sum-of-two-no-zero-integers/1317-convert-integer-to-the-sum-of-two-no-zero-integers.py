class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        a = 1
        b = n - a
        
        while 1:
            if not self.isContainZero(a) and not self.isContainZero(b):
                return [a, b]
            else:
                a += 1
                b -= 1
        
        return None
        
    def isContainZero(self, n: int) -> bool:
        
        s = str(n)
        cnt = s.count('0')
        
        return cnt > 0
        
        
        
        