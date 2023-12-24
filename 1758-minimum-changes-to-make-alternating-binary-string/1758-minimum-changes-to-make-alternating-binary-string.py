class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s)
        
        zeros_start = 0
        ones_start = 0
        
        # index : even
        for i in range(0, length, 2):
            if s[i] == '1':
                zeros_start += 1
            else:
                ones_start += 1
        
                
        for i in range(1, length, 2):
            if s[i] == '0':
                zeros_start += 1
            else:
                ones_start += 1
                
        return min(zeros_start, ones_start)