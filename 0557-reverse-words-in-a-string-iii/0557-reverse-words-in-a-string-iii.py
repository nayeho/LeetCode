class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(' ')
        
        for i in range(len(s_list)):
            s_list[i] = self.reverseString(s_list[i])
        
        result = ' '.join(s_list)
        return result
        
    def reverseString(self, s: str) -> str:
        
        s = list(s)

        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        result = ''.join(s)
        return result