class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = ''
        count = collections.Counter(s)

        while True:
            addOne = result and self._shouldAddOne(result, count)
            c = self._getLargestChar(result, count)
            if c == ' ':
                break
            repeats = 1 if addOne else min(count[c], repeatLimit)
            result += c * repeats
            count[c] -= repeats

        return result

    def _shouldAddOne(self, result: str, count: collections.Counter) -> bool:
        for c in reversed(string.ascii_lowercase):
            if count[c]:
                return result[-1] == c
        return False

    def _getLargestChar(self, result: str, count: collections.Counter) -> int:
        for c in reversed(string.ascii_lowercase):
            if count[c] and (not result or result[-1] != c):
                return c
        return ' '