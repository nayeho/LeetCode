class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(' ')
        
        temp = {}
        temp2 = {}
        p_len = len(pattern)
        s_len = len(list_s)
        
        if p_len != s_len:
            return False
        
        for i in range(s_len):
            if pattern[i] not in temp:
                temp[pattern[i]] = list_s[i]
            else:
                if temp[pattern[i]] != list_s[i]:
                    return False
                
        for i in range(s_len):
            if list_s[i] not in temp2:
                temp2[list_s[i]] = pattern[i]
            else:
                if temp2[list_s[i]] != pattern[i]:
                    return False
            
        return True
        