class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) < 2 or result[-1] != c or result[-2] != c:
                result.append(c)
        return ''.join(result)