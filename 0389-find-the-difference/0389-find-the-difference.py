class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp_s = list(s)
        temp_t = list(t)
        
        temp_s.sort()
        temp_t.sort()
        
        for i in range(len(temp_s)):
            if temp_s[i] != temp_t[i]:
                return temp_t[i]

            
        return temp_t[-1]