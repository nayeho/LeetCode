class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        cnt1 = s.count('1')
        cnt0 = s.count('0')
        
        if cnt1 == 1:
            return '0' * cnt0 + '1'
        
        return '1' * (cnt1 - 1) + '0' * cnt0 + '1'        