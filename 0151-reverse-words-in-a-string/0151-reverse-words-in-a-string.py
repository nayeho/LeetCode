class Solution:
    def reverseWords(self, s: str) -> str:
        
        s.strip()
        
        temp = s.split()
        temp.reverse()
        return ' '.join(temp)
        