class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        dictD = dict()
        result = ''
        
        cnt = 97
        
        
        for k in key:
            if k not in dictD and k != ' ':
                dictD[k] = chr(cnt)
                cnt += 1
                
        for m in message:
            if m != ' ':
                result += dictD[m]
            else:
                result += ' '
        
        
        return result
        