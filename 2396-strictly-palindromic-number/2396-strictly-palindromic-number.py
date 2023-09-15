class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        s = str(n)
        
        for i in range(2, n - 1):
            
            check = self.convert(int(s),i)
            
            if self.isPalindromic(check):
                pass
            else:
                return False
        return True
            
    def convert(self, num, base) :
        tmp = string.digits + string.ascii_lowercase    
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return self.convert(q, base) + tmp[r]
        
    def isPalindromic(self, check):
        
        length = len(check)
        
        low = 0
        high = length - 1
        
        while low <= high:
            if check[low] != check[high]:
                return False
            else:
                low += 1
                high -= 1
        return True
        
        
        
        