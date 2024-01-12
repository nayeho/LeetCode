class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        delimiter = len(s) // 2
        a = s[:delimiter]
        b = s[delimiter:]
        
        cnt_a = 0
        cnt_b = 0
        
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        for i in range(delimiter):
            if a[i] in vowels:
                cnt_a += 1
            if b[i] in vowels:
                cnt_b += 1
                
        return cnt_a == cnt_b