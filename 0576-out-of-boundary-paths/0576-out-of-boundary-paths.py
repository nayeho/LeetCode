class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        kMod = 1_000_000_007

        @functools.lru_cache(None)
        def dp(k: int, i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if k == 0:
                return 0
            return (dp(k - 1, i + 1, j) + dp(k - 1, i - 1, j) + dp(k - 1, i, j + 1) + dp(k - 1, i, j - 1)) % kMod

        return dp(maxMove, startRow, startColumn)