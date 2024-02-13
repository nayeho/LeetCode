class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(word: str) -> bool:
            temp = word[::-1]
            return temp == word
        
        for word in words:
            if isPalindrome(word):
                return word
            
        return ''
        