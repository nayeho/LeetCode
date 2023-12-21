class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        length = len(word)
        if length == 1:
            return True
        
        # check1 : All letters in this word are capitals
        if word.upper() == word:
            return True
        
        # check2 : All letters in this word are not capitals
        if word.lower() == word:
            return True
        
        # check3 : Only the first letter in this word is capital
        first = word[0]
        other = word[1:]
        
        if first.isupper():
            if other.lower() == other:
                return True
            
        return False
        
        
        
        