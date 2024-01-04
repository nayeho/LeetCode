class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = str(n)
        print(s)
        length = len(s)
        
        while length > 1:
            temp = 0
            for i in range(length):
                temp += int(s[i])**2
            
            s = str(temp)
            length = len(s)
            
        return s == '1' or s == '7'
        