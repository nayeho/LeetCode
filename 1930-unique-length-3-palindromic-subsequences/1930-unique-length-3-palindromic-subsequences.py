class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0
        first = [len(s)] * 26
        last = [0] * 26

        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            first[index] = min(first[index], i)
            last[index] = i

        for f, l in zip(first, last):
            if f < l:
                answer += len(set(s[f + 1:l]))

        return answer