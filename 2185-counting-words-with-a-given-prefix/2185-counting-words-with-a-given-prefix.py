class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        result = 0
        
        for word in words:
            if len(word) < length:
                pass
            else:
                if word[:length] == pref:
                    result += 1
                else:
                    pass
        
        return result