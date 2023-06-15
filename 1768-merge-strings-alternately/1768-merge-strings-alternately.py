class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)
        
        result = ''
        
        if len1 == len2:
            for i in range(len1):
                result += word1[i]
                result += word2[i]
        elif len1 > len2:
            for i in range(len2):
                result += word1[i]
                result += word2[i]
            result += word1[-(len1 - len2):]
        else:
            for i in range(len1):
                result += word1[i]
                result += word2[i]
            result += word2[-(len2 - len1):]           
                
        return result
        