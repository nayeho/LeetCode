class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        oddIndex = -1
        length = len(num)
        for i in range(length - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                oddIndex = i
                break
                
        if oddIndex == -1:
            return ""
        else:
            return num[ : oddIndex + 1]
        
        return None
        
        
        