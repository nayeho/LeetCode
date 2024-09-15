class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        kVowels = 'aeiou'
        result = 0
        prefix = 0
        prefixToIndex = {0: -1}

        for i, c in enumerate(s):
            index = kVowels.find(c)
            if index != -1:
                prefix ^= 1 << index
            prefixToIndex.setdefault(prefix, i)
            result = max(result, i - prefixToIndex[prefix])

        return result