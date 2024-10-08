class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])

        def dfs(i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if grid2[i][j] != 1:
                return 1

            grid2[i][j] = 2

            return (dfs(i + 1, j) & dfs(i - 1, j) & dfs(i, j + 1) & dfs(i, j - 1) & grid1[i][j])

        result = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    result += dfs(i, j)

        return result