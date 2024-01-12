class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        cs = list(str(num))
        c_min = list(str(num))
        
        p = cs[0]
        q = c_min[0]
        
        for i in range(len(cs)):
            if cs[i] != '9':
                p = cs[i]
                break
                
        for i in range(len(cs)):
            if cs[i] == p:
                cs[i] = '9'
                
        for i in range(len(c_min)):
            if c_min[i] == q:
                c_min[i] = '0'
                
        return int(''.join(cs)) - int(''.join(c_min))
