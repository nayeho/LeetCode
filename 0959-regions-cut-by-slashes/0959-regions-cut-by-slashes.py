class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        g = [[0] * (n * 3) for _ in range(n * 3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i * 3][j * 3 + 2] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    g[i * 3][j * 3] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3 + 2] = 1

        result = 0

        def dfs(g, i, j):
            if i < 0 or i == len(g) or j < 0 or j == len(g[0]):
                return
            if g[i][j] != 0:
                return

            g[i][j] = 2
            dfs(g, i + 1, j)
            dfs(g, i - 1, j)
            dfs(g, i, j + 1)
            dfs(g, i, j - 1)

        for i in range(n * 3):
            for j in range(n * 3):
                if g[i][j] == 0:
                    dfs(g, i, j)
                    result += 1

        return result
