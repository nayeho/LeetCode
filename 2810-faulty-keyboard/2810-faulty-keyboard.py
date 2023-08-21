class Solution:
    def finalString(self, s: str) -> str:
        
        result = ''
        
        for word in s:
            if word == 'i':
                result = self.reverseStr(result)
            else:
                result += word
                
        return result
        
        
        
    def reverseStr(self, s: str) -> str:
        
        result = ''
        length = len(s)
        
        for i in range(length):
            result = s[i] + result
        
        
        return result
        
        
        