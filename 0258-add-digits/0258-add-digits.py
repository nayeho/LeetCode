class Solution:
    def addDigits(self, num: int) -> int:
        
        s = str(num)
        
        length = len(s)
        
        while length > 1:
            temp = 0
            for i in range(length):
                temp += int(s[i])
                
            s = str(temp)
            length = len(s)
            
        return int(s)
        