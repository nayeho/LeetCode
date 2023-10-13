class Solution:
    def removeStars(self, s: str) -> str:
        
        count_star = s.count('*')
        
        for i in range(count_star):
            
            idx = s.index('*')
            
            s = s[ : idx - 1] + s[idx + 1 : ]

        return s
            
            
            
        
        