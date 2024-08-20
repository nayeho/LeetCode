class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        mem = [[0] * n for _ in range(n)]
        suffix = piles[:]

        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]

        return self._stoneGameII(suffix, 0, 1, mem)

    def _stoneGameII(self, suffix, i, M, mem):
        if i + 2 * M >= len(mem):
            return suffix[i]
        if mem[i][M] > 0:
            return mem[i][M]

        opponent = suffix[i]

        for X in range(1, 2 * M + 1):
            opponent = min(opponent, self._stoneGameII(suffix, i + X, max(M, X), mem))

        mem[i][M] = suffix[i] - opponent
        return mem[i][M]