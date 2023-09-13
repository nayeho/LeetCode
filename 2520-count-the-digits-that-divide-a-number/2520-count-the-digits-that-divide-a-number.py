class Solution:
    def countDigits(self, num: int) -> int:
        
        s = str(num)
        length = len(s)
        cnt = 0
        
        for digit in s:
            if num % int(digit) == 0:
                cnt += 1
        
        return cnt