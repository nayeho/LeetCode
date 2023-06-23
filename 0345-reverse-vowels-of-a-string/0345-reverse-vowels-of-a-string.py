class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel_set = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        
        # two pointer
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] in vowel_set and s[j] in vowel_set:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            elif s[i] not in vowel_set:
                i += 1
            
            elif s[j] not in vowel_set:
                j -= 1
            
        
        return "".join(s)