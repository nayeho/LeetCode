class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ''
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in order:
            while count[ord(c) - ord('a')] > 0:
                result += c
                count[ord(c) - ord('a')] -= 1

        for c in string.ascii_lowercase:
            for _ in range(count[ord(c) - ord('a')]):
                result += c

        return result