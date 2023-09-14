class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        length = len(indices)
        
        result = [None] * length
        
        for i in range(length):
            result[indices[i]] = s[i]
            
        return ''.join(result)
            