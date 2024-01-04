class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        weight = 1
        result = 0
        
        columnTitle = columnTitle[::-1]
        
        for s in columnTitle:
            result += (ord(s) - 64) * weight
            weight *= 26
            
        return result
        