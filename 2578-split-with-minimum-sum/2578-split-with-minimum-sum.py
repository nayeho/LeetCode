class Solution:
    def splitNum(self, num: int) -> int:
        
        s = list(str(num))
        s.sort(reverse = True)
        
        n1 = 0
        n2 = 0
        
        weight1 = 1
        weight2 = 1
        
        for i in range(len(s)):
            if i % 2 == 0:
                n1 += int(s[i]) * weight1
                weight1 *= 10
            else:
                n2 += int(s[i]) * weight2
                weight2 *= 10
            
        return n1 + n2
        