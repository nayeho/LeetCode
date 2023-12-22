class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        kMaxBit = 30
        result = 0

        for i in range(kMaxBit):
            if c >> i & 1:
                result += (a >> i & 1) == 0 and (b >> i & 1) == 0
            else:  # (c >> i & 1) == 0
                result += (a >> i & 1) + (b >> i & 1)

        return result