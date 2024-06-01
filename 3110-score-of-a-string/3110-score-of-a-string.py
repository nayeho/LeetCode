class Solution:
    def scoreOfString(self, s: str) -> int:

        temp = []
        result = 0
        for c in s:
            temp.append(ord(c))
        print(temp)
        
        for i in range(1, len(temp)):
            result += abs(temp[i] - temp[i - 1])
        
        return result
        