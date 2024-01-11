class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        result = 0
        
        temp = []
        
        for i in range(len(s) + 1 - k):
            temp.append(s[i:i+k])
            
        for n in temp:
            if int(n) == 0:
                pass
            elif num % int(n) == 0:
                result += 1
            else:
                pass
        
        return result
        