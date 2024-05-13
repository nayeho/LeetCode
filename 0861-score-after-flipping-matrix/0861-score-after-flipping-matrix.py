class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = m

        for j in range(1, n):
            onesCount = sum(grid[i][j] == grid[i][0] for i in range(m))
            result = result * 2 + max(onesCount, m - onesCount)

        return result
