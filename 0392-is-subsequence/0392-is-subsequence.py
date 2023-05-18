class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == '':
            return True
        
        temp = []
        
        cnt = 0
        
        for word in t:
            if word == s[cnt]:
                cnt += 1
        
                if cnt == len(s):
                    return True
        
        return False
                
            
            
        