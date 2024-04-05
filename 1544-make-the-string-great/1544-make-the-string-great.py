class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if result and self._is_bad_pair(result[-1], c):
                result.pop()
            else:
                result.append(c)
        return ''.join(result)

    def _is_bad_pair(self, a: str, b: str) -> bool:
        return a != b and a.lower() == b.lower()