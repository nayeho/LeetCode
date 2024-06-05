class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        result = []
        commonCount = [math.inf] * 26

        for a in words:
            count = [0] * 26
            for c in a:
                count[ord(c) - ord('a')] += 1
            for i in range(26):
                commonCount[i] = min(commonCount[i], count[i])

        for c in string.ascii_lowercase:
            for j in range(commonCount[ord(c) - ord('a')]):
                result.append(c)

        return result

    
    
    