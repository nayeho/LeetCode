class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #repeat
        wordSet = set(wordDict)

        @functools.lru_cache(None)
        def wordBreak(s: str) -> List[str]:
            result = []

            for i in range(1, len(s)):
                prefix = s[0:i]
                suffix = s[i:]
                if prefix in wordSet:
                    for word in wordBreak(suffix):
                        result.append(prefix + ' ' + word)

            if s in wordSet:
                result.append(s)

            return result

        return wordBreak(s)