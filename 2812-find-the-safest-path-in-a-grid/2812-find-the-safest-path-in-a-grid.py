class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        n = len(grid)
        distToThief = self._getDistToThief(grid, n)

        def hasValidPath(safeness: int) -> bool:
            if distToThief[0][0] < safeness:
                return False

            q = collections.deque([(0, 0)])
            seen = {(0, 0)}

            while q:
                i, j = q.popleft()
                if distToThief[i][j] < safeness:
                    continue
                if i == n - 1 and j == n - 1:
                    return True
                for dx, dy in self.dirs:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                        q.append((x, y))
                        seen.add((x, y))

            return False

        return bisect.bisect_left(range(n * 2), True,
                                  key=lambda m: not hasValidPath(m)) - 1

    def _getDistToThief(self, grid: List[List[int]], n: int) -> List[List[int]]:
        distToThief = [[float('inf')] * n for _ in range(n)]
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    distToThief[i][j] = 0

        while q:
            i, j = q.popleft()
            for dx, dy in self.dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and distToThief[x][y] == float('inf'):
                    distToThief[x][y] = distToThief[i][j] + 1
                    q.append((x, y))

        return distToThief
