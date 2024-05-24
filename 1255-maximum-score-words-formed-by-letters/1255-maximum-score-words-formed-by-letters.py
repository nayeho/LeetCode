class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = collections.Counter(letters)
        
        # repeat

        def useWord(i: int) -> int:
            isValid = True
            earned = 0
            for c in words[i]:
                count[c] -= 1
                if count[c] < 0:
                    isValid = False
                earned += score[ord(c) - ord('a')]
            return earned if isValid else -1

        def unuseWord(i: int) -> None:
            for c in words[i]:
                count[c] += 1

        def dfs(s: int) -> int:
            result = 0
            for i in range(s, len(words)):
                earned = useWord(i)
                if earned > 0:
                    result = max(result, earned + dfs(i + 1))
                unuseWord(i)
            return result

        return dfs(0)