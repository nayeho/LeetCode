class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        length = len(strs)
        sub_length = len(strs[0])
        result = 0
        
        for i in range(sub_length):
            temp = ''
            for j in range(length):
                temp += strs[j][i]
                
            if not self.isSorted(temp):
                result += 1
                
        
        return result
        
        
    def isSorted(self, s : str) -> bool:
        length = len(s)
        
        if length == 1:
            return True
        
        s_asc = ''.join(sorted(s))		        
        
        if s_asc == s:
            return True
        
        return False
        