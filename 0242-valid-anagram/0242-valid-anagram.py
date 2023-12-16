class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        
        new_s = ''.join(sorted(s))
        new_t = ''.join(sorted(t))
        
        if new_s == new_t:
            return True
        else:
            return False
        
        