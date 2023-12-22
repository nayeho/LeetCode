class Solution:
    def maxScore(self, s: str) -> int:
        
        length = len(s)
        
        maximum = -1
        
        for i in range(1, length):
            left = s[:i]
            right = s[i:]
            
            zeros_left = left.count('0')
            ones_right = right.count('1')
            
            score = zeros_left + ones_right
            
            if score > maximum:
                maximum = score
            
        return maximum
        
        
        