class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        cvt1 = ''.join(word1)
        cvt2 = ''.join(word2)
        
        return cvt1 == cvt2
        