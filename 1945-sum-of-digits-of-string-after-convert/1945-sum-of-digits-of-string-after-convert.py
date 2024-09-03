class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        result = self._convert(s)
        for _ in range(k):
            result = self._getDigitSum(result)
        return result

    def _convert(self, s: str) -> int:
        return int(''.join(str(string.ascii_lowercase.index(c) + 1) for c in s))

    def _getDigitSum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))